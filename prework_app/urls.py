from django.conf.urls import url
from prework_app.views import IndexView,users,form_name_view,UserView

app_name = 'prework_app'
urlpatterns = [
    url(r'^$',form_name_view, name='form_view'),
    url(r'^$',users,name = 'users'),
    url(r'^$', UserView.as_view(), name='user')
]
