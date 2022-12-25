from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from api.views import health_check

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    url(r'^healthcheck$', health_check, name='health_check')
]
