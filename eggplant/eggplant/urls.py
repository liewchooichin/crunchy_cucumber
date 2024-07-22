"""
URL configuration for eggplant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Namespcae
# The namespace is added to the include(). It is clearer
# to add namespace in include() because it can be seen
# in one glance this include file is associated with this
# namespace.
urlpatterns = [
    # default admin
    path(route='admin/', view=admin.site.urls, name="admin"),
    # django_browser_reload
    path(route="__reload__/", 
         view=include("django_browser_reload.urls")),
    # index homepage
    path(route="polls/", 
         view=include("polls.urls", namespace="polls")),
    
]


# Only serve uploaded files this way if you are in DEBUG=True mode.
# Add the new route returned by static() into urlpatterns.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, 
                          document_root=settings.STATIC_ROOT)