# from django.conf.urls import url
from django.urls import re_path as url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^profile/(?P<user_id>\d+)?$', views.profile, name='profile'),
    url(r'^update/profile$', views.updateprofile, name='updateprofile'),
    url(r'^vote/(?P<post_id>\d+)?$', views.vote, name='vote'),    
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^api/post/$', views.PostList.as_view()),
    url(r'^api/profile/$', views.ProfileList.as_view()),
]
if settings.DEBUG: 
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
