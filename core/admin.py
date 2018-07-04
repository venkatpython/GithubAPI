# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.conf.urls import url
from django.template.response import TemplateResponse
from .models import GitUserInfo, APIStatistics
from datetime import datetime, timedelta

# Register your models here.


class GitUserInfoAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created', 'node_id', 'image_tag')
    list_display = ['id', 'login', 'score', 'git_url', 'created', 'image_tag']
    search_fields = ['id','following_url', 'gists_url', 'score', 'organizations_url', 'git_url', 'events_url', 'html_url',
                    'subscriptions_url', 'avatar_url', 'repos_url', 'received_events_url', 'gravatar_id', 'starred_url',
                    'is_site_admin', 'login', 'node_id', 'followers_url', 'created']
    list_filter = tuple(search_fields)

    def get_urls(self):
        urls = super(GitUserInfoAdmin, self).get_urls()
        print urls
        my_urls = [
            # url('report/get/(?P<report_period>[\w\-]+)/', self.get_users_report),
            url('report/(?P<report_type>[\w\-]+)/(?P<report_period>[\w\-]+)/', self.get_report),
        ]
        return my_urls + urls

    def get_report(self, request, report_type, report_period):
        context = dict(
            self.admin_site.each_context(request),
        )
        curr_date = datetime.now()
        if report_period == 'Day':
            start_date = curr_date - timedelta(days=1)
            end_date = curr_date
        elif report_period == 'Week':
            start_date = curr_date - timedelta(days=7)
            end_date = curr_date
        elif report_period == 'Month':
            start_date = curr_date - timedelta(days=30)
            end_date = curr_date
        if report_type == 'overall':
            users = GitUserInfo.objects.filter(created__lte=end_date, created__gte=start_date).count()
            api_count = APIStatistics.objects.filter(api_call__lte=end_date, api_call__gte=start_date).count()
            context.update({'users_added': users, 'api_count': api_count, "report_period": report_period, "overall": True})
        if report_type == 'user_report':
            users = GitUserInfo.objects.filter(created__lte=end_date, created__gte=start_date)
            context.update({'users': users, "report_period": report_period, "user_report": True})
        return TemplateResponse(request, 'report.html', context)

admin.site.register(GitUserInfo, GitUserInfoAdmin)
