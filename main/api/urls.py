from rest_framework import routers
from main.api.views import PersonViewSet
from django.urls import path

router = routers.SimpleRouter()
router.register('person', PersonViewSet, basename='person')

urlpatterns = []
urlpatterns += router.urls
