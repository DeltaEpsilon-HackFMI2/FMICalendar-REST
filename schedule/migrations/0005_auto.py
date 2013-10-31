# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field events on 'Student'
        m2m_table_name = db.shorten_name(u'schedule_student_events')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('student', models.ForeignKey(orm[u'schedule.student'], null=False)),
            ('event', models.ForeignKey(orm[u'schedule.event'], null=False))
        ))
        db.create_unique(m2m_table_name, ['student_id', 'event_id'])


    def backwards(self, orm):
        # Removing M2M table for field events on 'Student'
        db.delete_table(db.shorten_name(u'schedule_student_events'))


    models = {
        u'schedule.block': {
            'Meta': {'object_name': 'Block'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'schedule.comment': {
            'Meta': {'object_name': 'Comment'},
            'desc': ('django.db.models.fields.TextField', [], {}),
            'dtstamp': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 10, 30, 0, 0)'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schedule.Event']"}),
            'from_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schedule.Student']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        u'schedule.department': {
            'Meta': {'object_name': 'Department'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'schedule.event': {
            'Meta': {'object_name': 'Event'},
            'date_end': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 30, 0, 0)'}),
            'date_start': ('django.db.models.fields.DateTimeField', [], {}),
            'duratation': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inserted': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 10, 30, 0, 0)'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schedule.Place']"}),
            'repeatable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schedule.Subject']"}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schedule.Teacher']"}),
            'type_value': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        },
        u'schedule.hierarchyunit': {
            'Meta': {'object_name': 'HierarchyUnit'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schedule.HierarchyUnit']", 'null': 'True', 'blank': 'True'}),
            'type_value': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'schedule.place': {
            'Meta': {'object_name': 'Place'},
            'floor': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'room_place': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'schedule.student': {
            'Meta': {'object_name': 'Student'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'events': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['schedule.Event']", 'null': 'True', 'blank': 'True'}),
            'fac_number': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schedule.HierarchyUnit']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'subjects': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['schedule.Subject']", 'symmetrical': 'False'})
        },
        u'schedule.subject': {
            'Meta': {'object_name': 'Subject'},
            'block': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schedule.Block']", 'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schedule.HierarchyUnit']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'type_value': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        },
        u'schedule.teacher': {
            'Meta': {'object_name': 'Teacher'},
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schedule.Department']"}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'subjects': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['schedule.Subject']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['schedule']