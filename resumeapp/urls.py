from django.urls import path,include
from .views import *
from django.contrib import admin
#django admin header customization
admin.site.site_header = "Login to Developer Ashiq"
admin.site.site_title = "Welcome to Asiq's Dashboard"
admin.site.index_title = "Welcome to this Portal"


urlpatterns = [
    path('', home),
]
