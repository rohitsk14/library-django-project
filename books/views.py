from django.shortcuts import render
from .models import books
# Create your views here.

def index(request):
    return render(request,'index.html')

def search(request):
    string=request.POST["query"]

    book = books.objects.all()
    searched_records=[]
    for b in book:
        if b.title in string or b.publisher in string or b.author in string:
            searched_records.append(b)

    return render(request,'searched.html',{"list" : searched_records })

