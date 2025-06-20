from django.urls import path
from . import views

urlpatterns = [
    path("api/all-blogs/", views.get_all_blogs),
    path("api/create-blog/", views.create_blog),
    path("api/get-single-blog/<int:id>/", views.get_single_blog),
    path("api/update-blog/<int:id>/", views.update_blog),
    path("api/delete-blog/<int:id>/", views.delete_blog),

    path("api/all-products/", views.get_all_products),
    path("api/create-product/", views.create_product),
    path("api/get-single-product/<int:id>/", views.get_single_product),
    path("api/update-product/<int:id>/", views.update_product),
    path("api/delete-product/<int:id>/", views.delete_product),

]
