from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.http.response import HttpResponse
from django.core import serializers
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.models import Group
import json


# Create your views here.


def users(request):
    return render(request, 'users.html')


def groups(request):
    return render(request, 'group.html')


def creategroup(request):
    nama = request.POST.get("groupname", None)
    group = Group(name=nama)
    hasil = {
        "success": True,
        "message": "Group Created !"
    }

    return JsonResponse(hasil, safe=False)


def get_alluser(request):
    draw = request.POST.get('draw', None)
    search = request.POST.get('search', None)
    length = int(request.POST.get('length', None))
    start = int(request.POST.get('start', None))
    User = get_user_model()
    listall = list(User.objects.all()[start:length].values('id', 'username', 'email', 'last_login', 'is_superuser', 'is_staff', 'is_active'))
    print(len(listall))
    hasil = {
        "draw": draw,
        "recordsTotal": len(listall),
        "recordsFiltered": len(listall),
        "data": listall
    }

    return JsonResponse(hasil, safe=False)
