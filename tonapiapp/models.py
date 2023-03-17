from django.db import models
from tonapi import settings
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
import os
from datetime import datetime


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20)
    specialty = models.CharField(max_length=20)
    interest = models.CharField(max_length=20)
    INTEREST_CHOICES = (
        ('AI', 'AI'),
        ('WEB3', 'WEB3'),
        ('DESIGN', 'DESIGN'),
        ('INVESTMENT', 'INVESTMENT'),
        ('SELF-IMPROVEMENT', 'SELF-IMPROVEMENT'),
    )
    img_url = models.URLField(max_length=200, default="https://unsplash.com/ko/%EC%82%AC%EC%A7%84/XHVpWcr5grQ")
    address_hub = models.TextField(max_length=100, null=True)  # wallet address for TonHub
    address_kpr = models.TextField(max_length=100, null=True)  # wallet address for TonKeeper


class Article(models.Model):
    title = models.CharField(max_length=100)
    # datetime_updated = models.DateTimeField(auto_now_add=True, default='')
    # datetime_created = models.DateTimeField(auto_now=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE, default='', null=True)
    translators = models.ManyToManyField(User, related_name='translators')
    contributors = models.ManyToManyField(User, related_name='contributors')

class Token(models.Model):
    key = models.CharField(_("Key"), max_length=40, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("User"))
    created = models.DateTimeField(_("Created"), auto_now_add=True)
