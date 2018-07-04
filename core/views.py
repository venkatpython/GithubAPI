# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import json
import urllib
import requests

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.template import RequestContext
from .models import GitUserInfo, APIStatistics

# Create your views here.
GITHUB_URL = 'https://api.github.com/'


def getGitHubUserData(request):
    """
    This function is responsible pulling out the user data
    from the GitHub using Github Rest services.

    :param request:
    :return: Github users data
    """
    if request.method == 'GET':
        print request.session.get('access_token'), " -------- TTT ---------- "
        git_auth_url = settings.GIT_AUTH_URL
        querystring = urllib.urlencode({'client_id': settings.CLIENT_ID, 'scope':'user.email'})
        # context = RequestContext()
        return render(request, 'home.html', {'git_auth_url': '{}?{}'.format(git_auth_url, querystring),
                                                'is_access_given': True if request.session.get('access_token') else False},
                                                RequestContext(request))
    else:
        # Get Search Term and store user info on DB.
        search_term = request.POST.get('search_pattern')
        API_ENDPOINT = 'search/users'
        API_URL = os.path.join(GITHUB_URL, API_ENDPOINT)
        headers = {
            'content-type': 'application/json',
            'Accept': 'application/json'
        }
        payload = {'q': search_term}
        response = requests.get(API_URL, params=payload, headers=headers)
        print response.json()
        user_data = response.json().get('items', [])
        APIStatistics.objects.create(saved_objects=response.json().get('total_count', 0))
        for user in user_data:
            git_user, created = GitUserInfo.objects.get_or_create(id=user.get('id'))
            if git_user:
                git_user.login = user.get("login", '')
                git_user.node_id = user.get('node_id', 0)
                git_user.avatar_url = user.get('avatar_url')
                git_user.gravatar_id = user.get('gravatar_id', 0)
                git_user.git_url = user.get('url', '')
                git_user.html_url = user.get('html_url', '')
                git_user.followers_url = user.get('followers_url', '')
                git_user.following_url = user.get('following_url', '')
                git_user.gists_url = user.get('gists_url', '')
                git_user.starred_url = user.get('starred_url', '')
                git_user.subscriptions_url = user.get('subscriptions_url', '')
                git_user.organizations_url = user.get('organizations_url', '')
                git_user.repos_url = user.get('repos_url', '')
                git_user.events_url = user.get('events_url', '')
                git_user.received_events_url = user.get('received_events_url', '')
                git_user.is_site_admin = user.get('site_admin', False)
                git_user.score = user.get('score', '')
                git_user.save()
        users = GitUserInfo.objects.all()

        return render(request, 'home.html', {'users': users})


def getGitHubAccessToken(request):
    """
    3-way hand shake with Github.

    :param request:
    :return:
    """
    print request.GET.get('code'), " ----- CODE ------ "
    print settings.GIT_ACCESS_TOKEN_URL
    headers = {
        'content-type': 'application/json',
        'Accept': 'application/json'
    }
    payload = {
        'client_id': settings.CLIENT_ID,
        'client_secret': settings.CLIENT_SECRET,
        'code': request.GET.get('code', ''),
        # 'state': True
    }
    print payload
    response = requests.post(settings.GIT_ACCESS_TOKEN_URL, headers=headers, params=payload)
    print response.content
    access_token = response.json().get('access_token', None)
    # Set Access token in session and keep use it in APIs.
    # (Using Session for access token storage since we don't the django auth user system as of now.)
    request.session['access_token'] = access_token
    return redirect('/')
