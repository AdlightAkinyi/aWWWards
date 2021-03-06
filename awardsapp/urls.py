"""awardsapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from django.conf.urls import url
from django.urls import include, re_path as url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
# from django.urls import path
from django.contrib.auth import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
   
  
    # # url(r'^accounts/', include('registration.backends.simple.urls')),
    # # url(r'^logout/$', views.logout, {"next_page":'/'}),
    # #  url(r'^accounts/', include('registration.backends.simple.urls')),
    # url('logout/', auth_views.LogoutView.as_view(next_page = '/')),
    # url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
    url(r'^admin/', admin.site.urls),
    url(r'',include('awardsproject.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    # url('logout/', auth_views.LogoutView.as_view(next_page = '/')),
    # url(r'^logout/$', views.logout,{"next_page":'/'}),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings')),
]

if settings.DEBUG: 
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
