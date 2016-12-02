"""apartmentexample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from demo import views
from demo.forms import AptWiz_1, AptWiz_2, AptWiz_3, AptWiz_4
urlpatterns = [
    url(r'^$', views.homepage, name="embed"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^embed/', views.embed, name="embed"),
    url(r'^login/$', login, name="login"),
    url(r'^logout/$', logout,{'next_page': '/'}),
    url(r'^apartments/create/', views.ApartmentCreate.as_view()),
    url(r'^apartment_contacts/create/', views.ApartmentContactCreate.as_view(success_url="/")),
    url(r'^apartment_buildings/create/', views.ApartmentBuildingCreate.as_view(success_url="/")),
    url(r'^apartments/delete/(?P<pk>\d+)$', views.ApartmentDelete.as_view()),
    url(r'^apartments/wizard/', lambda request: views.ApartmentWizard.as_view([AptWiz_1, AptWiz_2, AptWiz_3, AptWiz_4],user=request.user)(request)),
]
