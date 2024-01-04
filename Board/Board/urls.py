"""
URL configuration for Board project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include, re_path
from django.contrib.auth.decorators import login_required
from ckeditor_uploader.views import upload, browse
from django.views.decorators.cache import never_cache
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('bboard/', include('bboard.urls')),
    path('', include('protect.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    re_path(r'^upload/', login_required(upload), name='ckeditor_upload'),
    re_path(r'^browse/', login_required(never_cache(browse)), name='ckeditor_browse'),


    # path('', include('django.contrib.flatpages.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
