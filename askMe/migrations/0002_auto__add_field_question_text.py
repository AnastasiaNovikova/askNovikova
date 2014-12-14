# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Question.text'
        db.add_column(u'askMe_question', 'text',
                      self.gf('django.db.models.fields.CharField')(default='\xd1\x81\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xbe', max_length=256),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Question.text'
        db.delete_column(u'askMe_question', 'text')


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
            'text': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
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