#-*- coding: utf-8 -*-

from django.db import models

class Choice(models.Model):
    class Meta:
        pass

    question = None
    choice_text = None
    votes = undefined(default=0)


