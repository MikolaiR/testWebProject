"""testWeb URL Configuration

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
from django.contrib import admin
from django.urls import path

from todo.views import NoteView, NoteCreateView, note_delete

app_name = "todo"

urlpatterns = [
    path("list", NoteView.as_view(), name='note_list'),
    path("create", NoteCreateView.as_view(), name='create'),
    path("delete/<int:note_id>", note_delete, name='delete'),
]
