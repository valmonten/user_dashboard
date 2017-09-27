# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..logreg.models import *

# Create your models here.
class Messages_Posted(models.Model):

    msg = models.TextField()
    user_from = models.ForeignKey(Users, related_name = "msg_from")
    user_to = models.ForeignKey(Users, related_name = "msg_to")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Comments_Posted(models.Model):
    cmt = models.TextField()
    on_msg = models.ForeignKey(Messages_Posted, related_name = "comments")
    user_from = models.ForeignKey(Users, related_name = "comments_from")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

