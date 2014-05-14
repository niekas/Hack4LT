# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Hacker.final_mark'
        db.add_column(u'hack4lt_hacker', 'final_mark',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Hacker.exam_date'
        db.add_column(u'hack4lt_hacker', 'exam_date',
                      self.gf('django.db.models.fields.DateTimeField')(default=None, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Hacker.final_mark'
        db.delete_column(u'hack4lt_hacker', 'final_mark')

        # Deleting field 'Hacker.exam_date'
        db.delete_column(u'hack4lt_hacker', 'exam_date')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'hack4lt.hacker': {
            'Meta': {'object_name': 'Hacker'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254'}),
            'email_verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'exam_date': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'final_mark': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'repository': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'stackoverflow_user': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'hack4lt.task1': {
            'Meta': {'object_name': 'Task1'},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hack4lt.Hacker']"})
        },
        u'hack4lt.task2': {
            'Meta': {'object_name': 'Task2'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'repository': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hack4lt.Hacker']"})
        },
        u'hack4lt.taskaplinkaresult': {
            'Meta': {'object_name': 'TaskAplinkaResult', '_ormbases': [u'hack4lt.TaskResult']},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'taskresult_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['hack4lt.TaskResult']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'hack4lt.taskcomment': {
            'Meta': {'object_name': 'TaskComment'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hack4lt.TaskResult']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hack4lt.Hacker']", 'null': 'True', 'blank': 'True'})
        },
        u'hack4lt.taskinfo': {
            'Meta': {'object_name': 'TaskInfo'},
            'badge': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'criterias': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'deadline': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'extra_points': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'points': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '90'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '900'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hack4lt.Hacker']", 'null': 'True', 'blank': 'True'})
        },
        u'hack4lt.taskpythonresult': {
            'Meta': {'object_name': 'TaskPythonResult', '_ormbases': [u'hack4lt.TaskResult']},
            'description': ('django.db.models.fields.TextField', [], {}),
            'repository': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'taskresult_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['hack4lt.TaskResult']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'hack4lt.taskresult': {
            'Meta': {'object_name': 'TaskResult'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'done': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'got_extra_points': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'should_check': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hack4lt.TaskInfo']", 'null': 'True', 'blank': 'True'}),
            'total_points': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hack4lt.Hacker']", 'null': 'True', 'blank': 'True'})
        },
        u'hack4lt.taskseminarasresult': {
            'Meta': {'object_name': 'TaskSeminarasResult', '_ormbases': [u'hack4lt.TaskResult']},
            'date': ('django.db.models.fields.CharField', [], {'default': "'2014-05-05'", 'max_length': '20', 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'presentation': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'repository': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '900'}),
            u'taskresult_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['hack4lt.TaskResult']", 'unique': 'True', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '900'})
        },
        u'hack4lt.topic': {
            'Meta': {'object_name': 'Topic'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '900'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '900'})
        }
    }

    complete_apps = ['hack4lt']