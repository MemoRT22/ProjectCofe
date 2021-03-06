"""cafe URL Configuration

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
from django.urls import path, include
from django.conf import settings
from core import views
from recipe.urls import recipe_patterns
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('visit/', views.visit_us, name="visit_us"),
    path('services/', include('services.urls')),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
    path('recipe/', include(recipe_patterns)),
    path('page/', include('pages.urls')),
    path('social-auth/', include('social_django.urls', namespace="social")),
    # Paths de autenticación
    path('accounts/', include('django.contrib.auth.urls')),
    # Aumentar la lista de posibles urls en la raiz de la aplicación
    path('accounts/', include('registration.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
