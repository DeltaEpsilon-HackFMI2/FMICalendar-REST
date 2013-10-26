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
        self.room_place + ' ' + self.floor


class HierarchyUnit(models.Model):
    PROGRAM = u'PR'
    YEAR = u'YR'
    GROUP = u'GR'
    TYPES = (
        (PROGRAM, u"Специалност"),
        (YEAR, u"Курс"),
        (GROUP, u"Група"),
    )

    type_value = models.CharField(max_length=10, choices=TYPES)
    value = models.CharField(max_length=50)
    childs = models.ForeignKey("schedule.HierarchyUnit", null=True, blank=True)

    def __unicode(self):
        self.type_value + ' ' + self.value


class Block(models.Model):
    """
    Group representing a set of optional subjects.
    Example: Core of Computer Science.
    """
    name = models.CharField(max_length=50)


class Subject(models.Model):
    """
    Representation of all subjects.
    Example: Calculus 1.
    """
    MANDATORY = u'MN'
    OPTIONAL = u'OP'
    TYPES = (
        (MANDATORY, u"Задължителен"),
        (OPTIONAL, u"Избираем"),
    )

    type_value = models.CharField(max_length=12, choices=TYPES)
    name = models.CharField(max_length=60)
    block = models.ForeignKey(Block)

    def __unicode__(self):
        self.type_value + ' ' + self.name + ' ' + self.block


class Department(models.Model):
    """
    Group representing a set of lecturers
    grouped by field of teaching.
    """
    name = models.CharField(max_length=30)

    def __unicode__(self):
        self.name


class Teacher(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    full_name = models.CharField(max_length=50)
    position = models.CharField(max_length=30)
    subjects = models.ManyToManyField(Subject)
    department = models.ForeignKey(Department)

    def __unicode__(self):
        self.title + ' ' + self.name


class Event(models.Model):
    WEEKLY = u'WKL'
    TYPES = (
        (WEEKLY, u'Седмично'),
    )

    type_value = models.CharField(max_length=30, null=True, blank=True)
    inserted = models.DateField(default=datetime.now())
    name = models.CharField(max_length=60)
    place = models.ForeignKey(Place)
    date_start = models.DateField()
    date_end = models.DateField()
    repeatable = models.BooleanField()
    duratation = models.IntegerField()
    subject = models.ForeignKey(Subject)
    teacher = models.ForeignKey(Teacher)

    def __unicode__(self):
        self.name