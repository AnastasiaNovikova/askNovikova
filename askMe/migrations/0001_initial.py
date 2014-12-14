# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Question'
        db.create_table(u'askMe_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('adding_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'askMe', ['Question'])

        # Adding model 'Answer'
        db.create_table(u'askMe_answer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('adding_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('flag', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['askMe.Question'])),
        ))
        db.send_create_signal(u'askMe', ['Answer'])

        # Adding model 'Tag'
        db.create_table(u'askMe_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'askMe', ['Tag'])

        # Adding M2M table for field question on 'Tag'
        m2m_table_name = db.shorten_name(u'askMe_tag_question')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tag', models.ForeignKey(orm[u'askMe.tag'], null=False)),
            ('question', models.ForeignKey(orm[u'askMe.question'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tag_id', 'question_id'])


    def backwards(self, orm):
        # Deleting model 'Question'
        db.delete_table(u'askMe_question')

        # Deleting model 'Answer'
        db.delete_table(u'askMe_answer')

        # Deleting model 'Tag'
        db.delete_table(u'askMe_tag')

        # Removing M2M table for field question on 'Tag'
        db.delete_table(db.shorten_name(u'askMe_tag_question'))


    models = {
        u'askMe.answer': {
            'Meta': {'object_name': 'Answer'},
            'adding_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'flag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['askMe.Question']"})
        },
        u'askMe.question': {
            'Meta': {'object_name': 'Question'},
            'adding_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'askMe.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['askMe.Question']", 'null': 'True', 'blank': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['askMe']