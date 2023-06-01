from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('default/', views.default),
    path('about/', views.about),
    path('contact/', views.contact),
]
