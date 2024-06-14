from django.shortcuts import render
from LibApp.models import LibraryDB
from LibApp.serializers import LibrarySerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
# Create your views here.


@csrf_exempt
def LibraryAPI(request, id=0):
    if request.method=="GET":
        lib = LibraryDB.objects.all()
        lib_serializer = LibrarySerializer(lib, many=True)
        return JsonResponse(lib_serializer.data, safe=False)
    elif request.method=="POST":
        lib_data = JSONParser().parse(request)
        obj = LibrarySerializer(data=lib_data)
        if obj.is_valid():
            obj.save()
            return JsonResponse("Data saved successfully..", safe=False)
        return JsonResponse("Invalid data..", safe=False)
    elif request.method=="PUT":
        lib_data = JSONParser().parse(request)
        lib = LibraryDB.objects.get(BookID=lib_data['BookID'])
        obj = LibrarySerializer(lib, data=lib_data)
        if obj.is_valid():
            obj.save()
            return JsonResponse("Updated..", safe=False)
        return JsonResponse("Failed to update..", safe=False)
    elif request.method=="DELETE":
        lib_data = JSONParser().parse(request)
        li = LibraryDB.objects.get(BookID=lib_data['BookID'])
        li.delete()
        return JsonResponse("Data deleted..", safe=False)
@csrf_exempt
def savefile(request):
    img = request.FILES['UploadImage']
    file_name = default_storage.save(img.name,img)
    return JsonResponse(file_name, safe=False)