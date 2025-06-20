from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseServerError
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Blog_post, Product
from django.forms.models import model_to_dict


#BLOG
@api_view(["GET"])
def get_all_blogs(request):
    all_blogs = Blog_post.objects.all()
    all_blogs_list = [model_to_dict(blog) for blog in all_blogs]
    return Response({'blogs': all_blogs_list}, status=200)

# Create your views here.

@api_view(["POST"])
def create_blog(request):
    title = request.data.get("title")
    author = request.data.get("author")
    published_date = request.data.get("published_date")
    description = request.data.get("description")

    if not title or not author or not published_date or not description:
        return Response({
            "message": "Incomplete data"
        }, status = status.HTTP_404_NOT_FOUND)
    
    new_blog = Blog_post.objects.create(
        title = title, 
        author = author,
        published_date = published_date,
        description = description
    )

    return Response({
        "message": "New blog successfully created!",
        "new_blog" : model_to_dict(new_blog)
    }, status = 200)


@api_view(["GET"])
def get_single_blog(request, id):
    try:
        single_blog = Blog_post.objects.get(pk = id)
        return Response({
            "Blog with id {id}": model_to_dict(single_blog)
        }, status = 200)
    except Blog_post.DoesNotExist:
        return Response({
            "message" : "Blog with id {id} does not exist"
        }, status = status.HTTP_404_NOT_FOUND)

@api_view(["PUT", "PATCH"])
def update_blog(request, id):
    try:
        blog = Blog_post.objects.get(pk = id)
        blog.title = request.data.get("title", blog.title)
        blog.author = request.data.get("author", blog.author)
        blog.published_date = request.data.get("published_date", blog.published_date)
        blog.description = request.data.get("description", blog.description)
        
        blog.save()
        
        return Response({
            "message": "Update completed successfully!",
            "Blog" : model_to_dict(blog)
        }, status = 200)
    except Blog_post.DoesNotExist:
        return Response({
            "message" : "Blog with id {id} does not exist"
        }, status = status.HTTP_404_NOT_FOUND)


@api_view(["DELETE"])
def delete_blog(request, id):
    blogs = Blog_post.objects.all()
    try:
        blog = Blog_post.objects.get(pk = id)
        
        blog.delete()

        pk = id
        
        return Response({
            "msg": "Product deleted successfully!",
            "blogs": model_to_dict(blogs)
        })
    except Blog_post.DoesNotExist:
        return Response({
            "message" : "Blog with id {id} does not exist",
            "blogs": [model_to_dict(blog) for blog in blogs]
        }, status = status.HTTP_404_NOT_FOUND)
    


# PRODUCTS

@api_view(["GET"])
def get_all_products(request):
    products = Product.objects.all()
    all_products = [model_to_dict(product) for product in products]
    return Response({'products': all_products}, status=200)

# Create your views here.

@api_view(["POST"])
def create_product(request):
    name = request.data.get("name")
    price = request.data.get("price")
    description = request.data.get("description")

    if not name or not price or not description:
        return Response({
            "message": "Incomplete data"
        }, status = status.HTTP_404_NOT_FOUND)
    
    new_product = Product.objects.create(
        name = name,
        price = price,
        description = description
    )

    return Response({
        "message": "New product successfully created!",
        "new_product" : model_to_dict(new_product)
    }, status = 200)


@api_view(["GET"])
def get_single_product(request, id):
    try:
        product = Product.objects.get(pk = id)
        return Response({
            "Blog with id {id}": model_to_dict(product)
        }, status = 200)
    except Product.DoesNotExist:
        return Response({
            "message" : "Product with id {id} does not exist"
        }, status = status.HTTP_404_NOT_FOUND)

@api_view(["PUT", "PATCH"])
def update_product(request, id):
    try:
        product = Product.objects.get(pk = id)
        product.name = request.data.get("name", product.name)
        product.price = request.data.get("price", product.price)
        product.description = request.data.get("description", product.description)
        
        product.save()
        
        return Response({
            "message": "Update completed successfully!",
            "product" : model_to_dict(product)
        }, status = 200)
    except Product.DoesNotExist:
        return Response({
            "message" : "Product with id {id} does not exist"
        }, status = status.HTTP_404_NOT_FOUND)



@api_view(["DELETE"])
def delete_product(request, id):
    products = Product.objects.all()
    try:
        product = Product.objects.get(pk = id)
        product.delete()
        return Response({
            "msg": "Product deleted successfully!"
        })
    except Product.DoesNotExist:
        return Response({
            "message" : "Product with id {id} does not exist",
            "products": [model_to_dict(product) for product in products]

        }, status = status.HTTP_404_NOT_FOUND)

