from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
   return render(request, "main.html")

def create(request):
    content = request.POST['memoContent']
    return HttpResponse("사용자 입력 = "+content)
