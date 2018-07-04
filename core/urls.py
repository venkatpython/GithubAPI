from django.conf.urls import url
from core.views import getGitHubUserData, getGitHubAccessToken

urlpatterns = [
    url(r'^$', getGitHubUserData, name='home'),
    url(r'^callback/$', getGitHubAccessToken, name='getGitHubAccessToken')
]
