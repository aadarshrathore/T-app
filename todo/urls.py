from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from app.views import TagViewSet, TodoItemViewSet


router = routers.DefaultRouter()
router.register(r'tags', TagViewSet)
router.register(r'todoitems', TodoItemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('',include('app.urls'))
]
