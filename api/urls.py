from django.urls import include,path
from rest_framework import routers

import company_api
from api import views

router = routers.DefaultRouter()

router.register(r'customer', views.CustomerViewSet)
router.register(r'products' , views.ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),

]