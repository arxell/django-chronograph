# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Job'
        db.create_table(u'chronograph_job', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('frequency', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('params', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('command', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('shell_command', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('run_in_shell', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('args', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('disabled', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('next_run', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('adhoc_run', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('last_run', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('is_running', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('last_run_successful', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'chronograph', ['Job'])

        # Adding M2M table for field info_subscribers on 'Job'
        m2m_table_name = db.shorten_name(u'chronograph_job_info_subscribers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('job', models.ForeignKey(orm[u'chronograph.job'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['job_id', 'user_id'])

        # Adding M2M table for field subscribers on 'Job'
        m2m_table_name = db.shorten_name(u'chronograph_job_subscribers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('job', models.ForeignKey(orm[u'chronograph.job'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['job_id', 'user_id'])

        # Adding model 'Log'
        db.create_table(u'chronograph_log', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('job', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chronograph.Job'])),
            ('run_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('stdout', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('stderr', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('success', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'chronograph', ['Log'])

        # Adding model 'Hooks'
        db.create_table(u'chronograph_hooks', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('command', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'chronograph', ['Hooks'])


    def backwards(self, orm):
        # Deleting model 'Job'
        db.delete_table(u'chronograph_job')

        # Removing M2M table for field info_subscribers on 'Job'
        db.delete_table(db.shorten_name(u'chronograph_job_info_subscribers'))

        # Removing M2M table for field subscribers on 'Job'
        db.delete_table(db.shorten_name(u'chronograph_job_subscribers'))

        # Deleting model 'Log'
        db.delete_table(u'chronograph_log')

        # Deleting model 'Hooks'
        db.delete_table(u'chronograph_hooks')


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
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'chronograph.hooks': {
            'Meta': {'object_name': 'Hooks'},
            'command': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'chronograph.job': {
            'Meta': {'ordering': "('disabled', 'next_run')", 'object_name': 'Job'},
            'adhoc_run': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'args': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'command': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'frequency': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info_subscribers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'info_subscribers_set'", 'blank': 'True', 'to': u"orm['auth.User']"}),
            'is_running': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_run': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'last_run_successful': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'next_run': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'params': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'run_in_shell': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'shell_command': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'subscribers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'error_subscribers_set'", 'blank': 'True', 'to': u"orm['auth.User']"})
        },
        u'chronograph.log': {
            'Meta': {'ordering': "('-run_date',)", 'object_name': 'Log'},
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chronograph.Job']"}),
            'run_date': ('django.db.models.fields.DateTimeField', [], {}),
            'stderr': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'stdout': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'success': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['chronograph']