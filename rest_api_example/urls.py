from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # post
    path('post/', include('post.urls')),
    # customuser
    path('accounts/', include('customuser.urls'))
]
