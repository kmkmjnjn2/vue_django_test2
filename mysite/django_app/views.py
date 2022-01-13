from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.http import JsonResponse
from .boookinfo_serializers import bookinfoListSerializer
from .lineinfo_serializers import lineinfoListSerializer
import json


# 解决前端post请求 crsf问题
from django.views.decorators.csrf import csrf_exempt

from .models import BookInfo,LineInfo



@csrf_exempt
def testapi(request):
    # return HttpResponse("Hello World")
    print(request)
    print(request.method)
    if request.method == 'GET':
        print(request.GET.get('aa'))

        resp = {'reeorcode': 100, 'type': 'Get',
                'data': {'main': request.GET.get('aa')}}
        return HttpResponse(json.dumps(resp), content_type="application/json")
    else:
        print(request.POST)
        print(request.body)
        str1 = str(request.body, encoding="utf-8")
        data = eval(str1)
        print(data)
        print(data['aa'])
        print(type(request.body))
        resp = {'reeorcode': 100, 'type': 'POST',
                'data': {'main': data['aa']}}
        return HttpResponse(json.dumps(resp), content_type="application/json")


# def test(request):
#     return HttpResponse("Hello World")

@csrf_exempt
def Books(request):
    # 查询所有图书

    #序列化数据
    bookinfo = BookInfo.objects.all()
    serializer = bookinfoListSerializer(bookinfo,many=True)
    print("drf框架数据已经生成：",serializer.data)
    return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def Line(request):
    # 查询地板机械化数据

    #序列化数据
    lineinfo = LineInfo.objects.all()
    serializer = lineinfoListSerializer(lineinfo,many=True)
    print("drf框架数据已经生成：",serializer.data)
    return JsonResponse(serializer.data,safe=False)


