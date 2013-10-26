# -*- coding: utf-8 -*-

from django.db import models


class Place(models.Model):
    """ Holder object for basic info about the rooms
    in the university.
    """
    room_place = models.CharField(max_length=10)
    floor = models.IntegerField()


class HierarchyUnit(models.Model):
    TYPES = (
        (u"PROGRAM", u"Специалност"),
        (u"YEAR", u"Курс"),
        (u"GROUP", u"Група"),
    )

    type = models.CharField(max_length=10, choices=TYPES)
    value = models.CharField(max_length=50)
    parent = models.ForeignKey("schedule.HierarchyUnit", null=True, blank=True)


class Block(models.Model):
    """ Group representing a set of optional subjects.
    Example: Core of Computer Science.
    """
    name = models.CharField(max_length=50)


class Subject(models.Model):
    """ Representation of all subjects.
    Example: Calculus 1.
    """
    TYPES = (
        (u"MANDATORY", u"Задължителен"),
        (u"OPTIONAL", u"Избираем"),
    )

    type = models.CharField(max_length=12, choices=TYPES)
    name = models.CharField(max_length=60)
    block = models.ForeignKey(Block)


class Department(models.Model):
    """ Group representing a set of lecturers
    grouped by field of teaching.
    """
    name = models.CharField(max_length=30)


class Lecturer(models.Model):
    name = models.CharField(max_length=30)
    subjects = models.ManyToManyField(Subject)
    department = models.ForeignKey(Department)
