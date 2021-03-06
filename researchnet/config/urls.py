
"""researchnet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings


from core import views
import dashboard.views



urlpatterns = [
    url(r'^$', dashboard.views.index, name='home'),
    url(r'^enrollments/$', dashboard.views.enrollment),
    url(r'^export_submissions/$', dashboard.views.export_submissions),
    url(r'^export_enrollees/$', dashboard.views.export_enrollees),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^accounts/login/$', dashboard.views.login_view, name='login'),
    url(r'^logout/$', dashboard.views.logout_view, name='logout'),
    url('', include('django.contrib.auth.urls')),
    url(r'^heartbeat/$', views.HeartBeat, name='ambition.heartbeat')

]  

urlpatterns += format_suffix_patterns([
    url(r'^submission/$', views.SubmissionList.as_view()),
    url(r'^submission/(?P<pk>[0-9]+)/$', views.SubmissionDetail.as_view()), 
    url(r'^consent/$', views.ConsentList.as_view()),
    url(r'^users/$', views.UserViewSet),
    url(r'^participant/$', views.ParticipantList.as_view()),
    url(r'^participant/(?P<pk>[0-9]+)/$', views.ParticipantDetail.as_view()), 
])


from rest_framework.authtoken import views
urlpatterns += [
    url(r'^api-token-auth/', views.obtain_auth_token)
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

# Needed until the static file deployment situation is figured out
urlpatterns += staticfiles_urlpatterns()




