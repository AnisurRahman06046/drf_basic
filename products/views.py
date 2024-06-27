from django.shortcuts import render,HttpResponse
from .models import Products
from .serializers import ProductsSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import io 
from django.http import JsonResponse
# Create your views here.
def allProducts(request):
    # complex dataset
    products = Products.objects.all()
    # convert to native python data type 
    serialized = ProductsSerializer(products,many=True)
    # convert to json data
    jsonData = JSONRenderer().render(serialized.data)
    return HttpResponse(jsonData,content_type='application/json')


def singleProduct(request,title):
    # query set
    querySet = Products.objects.get(title=title)
    # convert to native python
    serialized = ProductsSerializer(querySet)
    # convert to json 
    data = JSONRenderer().render(serialized.data)
    return HttpResponse(data,content_type='application/json')

# @csrf_exempt
# def create_product(request):
#     if request.method=='POST':
#         data = request.body
#         streamed = io.BytesIO(data)
#         parsedData = JSONParser().parse(streamed)
#         serialiazed = ProductsSerializer(data=parsedData)
#         if serialiazed.is_valid():
#             return HttpResponse('parsed successfully')
#         else:
#             return HttpResponse("Failed")
@csrf_exempt
def create_product(request):
    if request.method == 'POST':
        data = request.body
        streamed = io.BytesIO(data)
        parsedData = JSONParser().parse(streamed)
        serializer = ProductsSerializer(data=parsedData)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'status': 'success', 'message': 'Product created successfully'}, status=201)
        else:
            return JsonResponse({'status': 'error', 'errors': serializer.errors}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
        

@csrf_exempt  
def updateProduct(request,title):
    if request.method=='PUT':
        # find data from model
        querySet = Products.objects.get(title=title)
        data = request.body 
        streamed = io.BytesIO(data)
        parsed = JSONParser().parse(streamed)
        serialized = ProductsSerializer(querySet,data=parsed,partial=True)
        
        if serialized.is_valid():
            serialized.save()
            return JsonResponse({'status': 'success', 'message': 'Product updated successfully'}, status=201)
        else:
            return JsonResponse({'status': 'error', 'errors': serialized.errors}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)



@csrf_exempt 
def deleteProduct(request,title):
    if request.method=='DELETE':
        query = Products.objects.get(title=title)
        # streamed = io.BytesIO(query)
        # parsed = JSONParser().parse(streamed)
        query.delete()
        return JsonResponse({'status': 'success', 'message': 'Product deleted successfully'}, status=201)
        