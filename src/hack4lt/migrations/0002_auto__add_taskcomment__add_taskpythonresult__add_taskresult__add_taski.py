# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TaskComment'
        db.create_table(u'hack4lt_taskcomment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hack4lt.TaskResult'], null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hack4lt.Hacker'], null=True, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
        ))
        db.send_create_signal(u'hack4lt', ['TaskComment'])

        # Adding model 'TaskPythonResult'
        db.create_table(u'hack4lt_taskpythonresult', (
            (u'taskresult_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['hack4lt.TaskResult'], unique=True, primary_key=True)),
            ('repository', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'hack4lt', ['TaskPythonResult'])

        # Adding model 'TaskResult'
        db.create_table(u'hack4lt_taskresult', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hack4lt.TaskInfo'], null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hack4lt.Hacker'], null=True, blank=True)),
            ('total_points', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('got_extra_points', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('done', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('should_check', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'hack4lt', ['TaskResult'])

        # Adding model 'TaskInfo'
        db.create_table(u'hack4lt_taskinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=900)),
            ('points', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('extra_points', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('deadline', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('criterias', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('badge', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hack4lt.Hacker'], null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('slug', self.gf('django.db.models.fields.CharField')(unique=True, max_length=90)),
        ))
        db.send_create_signal(u'hack4lt', ['TaskInfo'])

        # Adding model 'TaskAplinkaResult'
        db.create_table(u'hack4lt_taskaplinkaresult', (
            (u'taskresult_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['hack4lt.TaskResult'], unique=True, primary_key=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'hack4lt', ['TaskAplinkaResult'])


    def backwards(self, orm):
        # Deleting model 'TaskComment'
        db.delete_table(u'hack4lt_taskcomment')

        # Deleting model 'TaskPythonResult'
        db.delete_table(u'hack4lt_taskpythonresult')

        # Deleting model 'TaskResult'
        db.delete_table(u'hack4lt_taskresult')

        # Deleting model 'TaskInfo'
        db.delete_table(u'hack4lt_taskinfo')

        # Deleting model 'TaskAplinkaResult'
        db.delete_table(u'hack4lt_taskaplinkaresult')


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
        }
    }

    complete_apps = ['hack4lt']