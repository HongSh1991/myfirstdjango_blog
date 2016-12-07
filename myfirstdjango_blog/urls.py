"""myfirstdjango_blog URL Configuration

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
# from article import views as my_views

urlpatterns = [
    url(r'^$', include('article.urls')),
    # url(r'^detail/', include('article.urls')),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    # url(r'^article/(?P<my_args>\d+)/$', views.detail),
    # url(r'^(?P<my_args>\d+)/$', my_views.detail, name='detail'),
    # url(r'^test/$', my_views.test, name='test'),
]
