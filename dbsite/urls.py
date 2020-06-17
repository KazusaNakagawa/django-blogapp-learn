from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import include
from django.urls import path
# from django.urls import re_path
# from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    # 非推奨 gunicorn, localで疎通確認 nginx -> NG NOT FOUND
    # re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

