"""Kiwi Pycon 2017 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from kiwi_pycon_2017_demo import views

router = routers.SimpleRouter()
router.register(r'example', views.WidgetViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^docs/', include_docs_urls(title='Kiwi Pycon 2017 Demo API')),
    url(r'^admin/', admin.site.urls),
]
