from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    lists = Memo.objects.all()
    data = {'lists':lists}
    return render(request, "main.html", data)
   
def create(request):
    content = request.POST['memoContent']
    usermemo = Memo(text = content)
    usermemo.save()
    return HttpResponse("사용자 입력 = "+content)

def editPage(request, idx):
    article = Memo.objects.get(id=idx)
    data = {'article': article}
    return render(request, 'edit.html', data)
