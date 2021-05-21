#-*- coding: utf-8 -*-

from django.db import models

class Question(models.Model):
    class Meta:
        pass

    question_text = models.CharField()
    pub_date = models.DateField(auto_now=True)


