from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
app_name = "learning_logs"
urlpatterns = [
    #home page
    path('',views.index,name='index'),
    #show all topics
    path('topics/',views.topics,name='topics'),
    #show detail page
    #url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'), 
    path('topics/<int:topic_id>/',views.topic,name='topic'),
    #new theme page
    path('new_topic/',views.new_topic,name='new_topic'),
    #add new page
    #url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'), 
    path('new_entry/<int:topic_id>/',views.new_entry,name='new_entry'),
]
