from django.contrib import admin
from django.urls import path, include
from order import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Api/', include(views.route_toshop)),
]
