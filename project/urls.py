"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/',include(('accounts.urls', 'accounts'),namespace='accounts')),
    path('admin/', admin.site.urls),
    path('blog/',include(('blog.urls', 'blog'), namespace='blog')),
    path('home/',include(('home.urls', 'home'), namespace='home')),
    path('cart/',include(('cart.urls', 'cart'), namespace='cart')),
    path('contact/',include(('contact.urls', 'contact'), namespace='contact')),
    path('product/',include(('product.urls', 'product'), namespace='product')),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 
  # ... the rest of your URLconf goes here ...

urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
