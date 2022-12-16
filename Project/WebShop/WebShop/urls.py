"""WebShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

# Functional Requirement 1 (Site Architecture)
# Adding Landing page and React app on '/shop' URL
from django.views.generic import TemplateView
from home.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    # React
    path('shop/', TemplateView.as_view(template_name='index.html')),
    # Landing Page
    # path('', TemplateView.as_view(template_name='home.html')),
    path('', index),
    # APIs
    path("api/auth/", include('accounts.api.urls')),
    path("api/items/", include('items.api.urls')),
    path("api/cart/", include('cart.api.urls')),
]
