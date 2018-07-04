# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
# Create your models here.

class GitUserInfo(models.Model):
    """
    This model contains the GitHub user info
    """
    id = models.IntegerField(primary_key=True)
    login = models.CharField(_('User name'), max_length=64)
    node_id = models.CharField(_("Node ID"), null=True, blank=True, max_length=255)
    avatar_url = models.URLField(_("Avathar URL"), null=True, blank=True, max_length=255)
    gravatar_id = models.CharField(_("Gravatar ID"),null=True, blank=True, max_length=255)
    git_url = models.URLField(_("Git URL"), null=True, blank=True, max_length=255)
    html_url = models.URLField(_("HTML URL"), null=True, blank=True, max_length=255)
    followers_url = models.URLField(_("Followers Url"), null=True, blank=True, max_length=255)
    following_url = models.URLField(_("Following Url"), null=True, blank=True, max_length=255)
    gists_url = models.URLField(_("Gists Url"), null=True, blank=True, max_length=255)
    starred_url = models.URLField(_("Starred Url"), null=True, blank=True, max_length=255)
    subscriptions_url = models.URLField(_("Subscription Url"), null=True, blank=True, max_length=255)
    organizations_url = models.URLField(_("Org. Url"), null=True, blank=True, max_length=255)
    repos_url = models.URLField(_("Repos Url"), null=True, blank=True, max_length=255)
    events_url = models.URLField(_("Events Url"), null=True, blank=True, max_length=255)
    received_events_url = models.URLField(_("Received Events Url"), null=True, blank=True, max_length=255)
    is_site_admin = models.BooleanField(default=False)
    score = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s-%s-%s"%(self.login, self.id, self.created)

    def image_tag(self):
        return mark_safe('<img src="%s" width="75" height="75" />' % (self.avatar_url))


class APIStatistics(models.Model):
    """
    Track the API statistics.
    """
    api_call = models.DateTimeField(auto_now_add=True)
    saved_objects = models.IntegerField(default=0)
    # user = models.ForeignKey(User)