# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Place'
        db.create_table(u'schedule_place', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('room_place', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('floor', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'schedule', ['Place'])

        # Adding model 'HierarchyUnit'
        db.create_table(u'schedule_hierarchyunit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type_value', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['schedule.HierarchyUnit'], null=True, blank=True)),
        ))
        db.send_create_signal(u'schedule', ['HierarchyUnit'])

        # Adding model 'Block'
        db.create_table(u'schedule_block', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'schedule', ['Block'])

        # Adding model 'Subject'
        db.create_table(u'schedule_subject', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type_value', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('block', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['schedule.Block'], null=True, blank=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['schedule.HierarchyUnit'], null=True, blank=True)),
        ))
        db.send_create_signal(u'schedule', ['Subject'])

        # Adding model 'Department'
        db.create_table(u'schedule_department', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'schedule', ['Department'])

        # Adding model 'Teacher'
        db.create_table(u'schedule_teacher', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['schedule.Department'], null=True, blank=True)),
        ))
        db.send_create_signal(u'schedule', ['Teacher'])

        # Adding M2M table for field subjects on 'Teacher'
        m2m_table_name = db.shorten_name(u'schedule_teacher_subjects')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('teacher', models.ForeignKey(orm[u'schedule.teacher'], null=False)),
            ('subject', models.ForeignKey(orm[u'schedule.subject'], null=False))
        ))
        db.create_unique(m2m_table_name, ['teacher_id', 'subject_id'])

        # Adding model 'Event'
        db.create_table(u'schedule_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type_value', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True)),
            ('inserted', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 11, 1, 0, 0))),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['schedule.Place'], null=True, blank=True)),
            ('date_start', self.gf('django.db.models.fields.DateTimeField')()),
            ('date_end', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 11, 1, 0, 0))),
            ('repeatable', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('duratation', self.gf('django.db.models.fields.IntegerField')()),
            ('subject', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['schedule.Subject'], null=True, blank=True)),
            ('teacher', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['schedule.Teacher'], null=True, blank=True)),
        ))
        db.send_create_signal(u'schedule', ['Event'])

        # Adding model 'Student'
        db.create_table(u'schedule_student', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('fac_number', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['schedule.HierarchyUnit'], null=True, blank=True)),
        ))
        db.send_create_signal(u'schedule', ['Student'])

        # Adding M2M table for field events on 'Student'
        m2m_table_name = db.shorten_name(u'schedule_student_events')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('student', models.ForeignKey(orm[u'schedule.student'], null=False)),
            ('event', models.ForeignKey(orm[u'schedule.event'], null=False))
        ))
        db.create_unique(m2m_table_name, ['student_id', 'event_id'])

        # Adding model 'Comment'
        db.create_table(u'schedule_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_user', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['schedule.Student'], null=True, blank=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['schedule.Event'], null=True, blank=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
            ('dtstamp', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 11, 1, 0, 0))),
            ('desc', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'schedule', ['Comment'])


    def backwards(self, orm):
        # Deleting model 'Place'
        db.delete_table(u'schedule_place')

        # Deleting model 'HierarchyUnit'
        db.delete_table(u'schedule_hierarchyunit')

        # Deleting model 'Block'
        db.delete_table(u'schedule_block')

        # Deleting model 'Subject'
        db.delete_table(u'schedule_subject')

        # Deleting model 'Department'
        db.delete_table(u'schedule_department')

        # Deleting model 'Teacher'
        db.delete_table(u'schedule_teacher')

        # Removing M2M table for field subjects on 'Teacher'
        db.delete_table(db.shorten_name(u'schedule_teacher_subjects'))

        # Deleting model 'Event'
        db.delete_table(u'schedule_event')

        # Deleting model 'Student'
        db.delete_table(u'schedule_student')

        # Removing M2M table for field events on 'Student'
        db.delete_table(db.shorten_name(u'schedule_student_events'))

        # Deleting model 'Comment'
        db.delete_table(u'schedule_comment')


    models = {
        u'schedule.block': {
            'Meta': {'object_name': 'Block'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'schedule.comment': {
            'Meta': {'object_name': 'Comment'},
            'desc': ('django.db.models.fields.TextField', [], {}),
            'dtstamp': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 11, 1, 0, 0)'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['schedule.Event']", 'null': 'True', 'blank': 'True'}),
            'from_user': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['schedule.Student']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        u'schedule.department': {
            'Meta': {'object_name': 'Department'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'schedule.event': {
            'Meta': {'object_name': 'Event'},
            'date_end': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 1, 0, 0)'}),
            'date_start': ('django.db.models.fields.DateTimeField', [], {}),
            'duratation': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inserted': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 11, 1, 0, 0)'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['schedule.Place']", 'null': 'True', 'blank': 'True'}),
            'repeatable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['schedule.Subject']", 'null': 'True', 'blank': 'True'}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['schedule.Teacher']", 'null': 'True', 'blank': 'True'}),
            'type_value': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'schedule.hierarchyunit': {
            'Meta': {'object_name': 'HierarchyUnit'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['schedule.HierarchyUnit']", 'null': 'True', 'blank': 'True'}),
            'type_value': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'schedule.place': {
            'Meta': {'object_name': 'Place'},
            'floor': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'room_place': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'schedule.student': {
            'Meta': {'object_name': 'Student'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'events': ('django.db.models.fields.related.ManyToManyField', [], {'default': 'None', 'to': u"orm['schedule.Event']", 'null': 'True', 'symmetrical': 'False', 'blank': 'True'}),
            'fac_number': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['schedule.HierarchyUnit']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'schedule.subject': {
            'Meta': {'object_name': 'Subject'},
            'block': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['schedule.Block']", 'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['schedule.HierarchyUnit']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type_value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'schedule.teacher': {
            'Meta': {'object_name': 'Teacher'},
            'department': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['schedule.Department']", 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'subjects': ('django.db.models.fields.related.ManyToManyField', [], {'default': 'None', 'to': u"orm['schedule.Subject']", 'null': 'True', 'symmetrical': 'False', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['schedule']