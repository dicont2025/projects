from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("서디콘 하잉");

def create(request):
    content = request.GET['memoContent']
    return HttpResponse("사용자 입력 = "+content)
