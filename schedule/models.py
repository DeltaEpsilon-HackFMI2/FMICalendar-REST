# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime


class Place(models.Model):
    """
    Holder object for basic info about the rooms
    in the university.
    """
    room_place = models.CharField(max_length=10)
    floor = models.IntegerField()

    def __unicode__(self):
        return self.room_place


class HierarchyUnit(models.Model):
    PROGRAM = 'PR'
    YEAR = 'YR'
    GROUP = 'GR'
    TYPES = (
        (PROGRAM, u"Специалност"),
        (YEAR, u"Курс"),
        (GROUP, u"Група"),
    )

    type_value = models.CharField(max_length=10, choices=TYPES)
    value = models.CharField(max_length=50)
    parent = models.ForeignKey("schedule.HierarchyUnit", null=True, blank=True)

    def get_all_childs(self):
        return HierarchyUnit.objects.filter(parent=self)

    def __unicode__(self):
        return self.value



class Block(models.Model):
    """
    Group representing a set of optional subjects.
    Example: Core of Computer Science.
    """
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Subject(models.Model):
    """
    Representation of all subjects.
    Example: Calculus 1.
    """
    MANDATORY = 'MN'
    OPTIONAL = 'OP'
    TYPES = (
        (MANDATORY, u"Задължителен"),
        (OPTIONAL, u"Избираем"),
    )

    type_value = models.CharField(max_length=12, choices=TYPES)
    name = models.CharField(max_length=60)
    block = models.ForeignKey(Block, null=True, blank=True)
    group = models.ForeignKey(HierarchyUnit, null=True, blank=True, limit_choices_to={'type_value': HierarchyUnit.GROUP})

    def __unicode__(self):
        return self.name


class Department(models.Model):
    """
    Group representing a set of lecturers
    grouped by field of teaching.
    """
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    full_name = models.CharField(max_length=50)
    position = models.CharField(max_length=30)
    subjects = models.ManyToManyField(Subject)
    department = models.ForeignKey(Department)

    def __unicode__(self):
        return self.name


class Event(models.Model):
    WEEKLY = 'WKL'
    TYPES = (
        (WEEKLY, u'Седмично'),
    )

    type_value = models.CharField(max_length=30, null=True, blank=True)
    inserted = models.DateField(default=datetime.now())
    name = models.CharField(max_length=60)
    place = models.ForeignKey(Place)
    date_start = models.DateField()
    date_end = models.DateField(null=True, blank=True)
    repeatable = models.BooleanField()
    duratation = models.IntegerField(null=True, blank=True)
    subject = models.ForeignKey(Subject)
    teacher = models.ForeignKey(Teacher)

    def __unicode__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=30)
    fac_number = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    group = models.ForeignKey(HierarchyUnit)
    subjects = models.ManyToManyField(Subject)

    def __unicode__(self):
        return self.name

class Comment(models.Model):
    from_user = models.ForeignKey(Student)
    event = models.ForeignKey(Event)
    start_date = models.DateField()
    end_date = models.DateField()
    dtstamp = models.DateField(default=datetime.now())
    desc = models.TextField()
