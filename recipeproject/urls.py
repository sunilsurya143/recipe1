"""recipeproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import TemplateView
from recipeapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/',include('django.contrib.auth.urls')),
    url(r'^$',views.index),
    url(r'^check/',views.checkuser),
    url(r'^register/',views.register),
    url(r'^addrecipe/',views.AddRecipe),
    url(r'^delete/(?P<id>\d+)',views.afterdeleted),
    url(r'^detail/(?P<id>\d+)',views.detailsofrecipie),
    url(r'^backtolist/',views.backtolist,name='backtolist'),
    url(r'^backtoaddrecipe/',views.backtoaddrecipe,name='backtoaddrecipe'),
    url(r'^logout/',views.logoutpage,name='logout')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

