from django.urls import path
from . import views
urlpatterns = [

    # path("all/",views.allProducts,name='allProducts'),
    path("add/",views.create_product,name='add'),
    path("create/",views.fetchProducts,name='create'),
    path("get-data/",views.fetchProducts,name='products'),
    path("get-data/<str:title>/",views.fetchProducts,name='product'),
    path("edit/<str:title>/",views.fetchProducts,name='product'),
    path("remove/<str:title>/",views.fetchProducts,name='remove'),
    path("update/<str:title>/",views.updateProduct,name='update'),
    path("delete/<str:title>/",views.deleteProduct,name='delete'),
]