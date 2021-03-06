"""python_prework_base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin

from prework_app import views
from userauth.views import user_login


urlpatterns = [
    url(r'^$', views.UserView.as_view(template_name='prework_app/index.html'), name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^users/',include('prework_app.urls')),
    url(r'^formpage/',include('prework_app.urls')),
    url(r'^userauth/',include('userauth.urls')),
    url(r'logout/$',user_login,name = 'logout'),
]


''' Note to self - If I need to use a template not created by django, say for Example
    index.html, inserting the template name will allow me to use the template I created)
'''
