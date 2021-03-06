"""onedaypack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

import main.views
import debug_toolbar
from call_log.views import AdviceViewSet


router = SimpleRouter()

router.register(r'api/call_log/advices', AdviceViewSet, basename='advice')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', main.views.index),
    path('__debug__/', include(debug_toolbar.urls)),
]

urlpatterns += router.urls
