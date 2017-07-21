from django.conf.urls import url
from . import views

app_name = "Employment"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<job_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^apply/$', views.apply, name='apply'),
]