from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('boards.urls', namespace='boards')),
    path('admin/', admin.site.urls),

]
