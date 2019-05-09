<<<<<<< HEAD
"""todo_back URL Configuration
=======
"""mysite URL Configuration
>>>>>>> 9eada6e416fa4b1441eaf9455c6ea41dac34afa4

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
from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include

=======
from django.urls import path
from api import views
from django.conf.urls import include
>>>>>>> 9eada6e416fa4b1441eaf9455c6ea41dac34afa4
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
<<<<<<< HEAD
=======



>>>>>>> 9eada6e416fa4b1441eaf9455c6ea41dac34afa4
