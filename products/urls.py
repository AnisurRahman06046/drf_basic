from django.urls import path
from . import views
urlpatterns = [

    path("all/",views.allProducts,name='allProducts'),
    path("add/",views.create_product,name='add'),
    path("single/<str:title>/",views.singleProduct,name='product'),
    path("update/<str:title>/",views.updateProduct,name='update'),
    path("delete/<str:title>/",views.deleteProduct,name='delete'),
]