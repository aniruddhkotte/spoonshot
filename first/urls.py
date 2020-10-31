"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from books.views import book_create_view
from books.views import books_list_view
from books.views import book_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapi.urls')),
    path('create/', book_create_view),
    path('', books_list_view),
    path('books/<int:my_id>/', book_detail_view, name='book'),
]
