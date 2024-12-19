from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('blog/', include('blog.urls')),  # 잘못된 따옴표 수정
    path('admin/', admin.site.urls),
]