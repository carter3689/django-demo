from django.conf.urls import url
from prework_app.views import IndexView,index,users,form_name_view

app_name = 'prework_app'
urlpatterns = [
    url(r'^$',form_name_view, name='form_view'),
    url(r'^$',users,name = 'users'),
]
