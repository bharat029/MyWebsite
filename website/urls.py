from django.urls import path, re_path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.AboutMeListView.as_view(), name='index'),
    path('download/', views.download, name='download'),
    path('projects/', views.ProjectListView.as_view(), name='projects'),
    re_path(r'^projects/(?P<pk>[0-9]+)/$', views.ProjectDetailView.as_view(), name='project_details'),
    path('cv/', views.cv, name='cv'),
    path('skillset/', views.SkillsetListView.as_view(), name='skillset')
]
