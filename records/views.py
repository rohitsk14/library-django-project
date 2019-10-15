from django.shortcuts import render,redirect
from .models import record
from books.models import books
from datetime import datetime

# Create your views here.
def records(request):
    return render(request,'records.html')

def book_issue_form(request):
    return render(request,'book_issue_form.html',{"success":False,"no_copies":False,"book_not_found":False})

def book_return_form(request):
    return render(request,'book_return_form.html')

def issue_book(request):
    rec=record()
    book=books.objects.all()
    rec.book_id = request.POST["book_id"]
    rec.student_id = request.POST["student_id"]
    rec.year = request.POST["year"]
    rec.student_name = request.POST["student_name"]
    rec.issue_date = datetime.now()
    for b in book:
        if rec.book_id == b.book_id:
            if b.no_of_copies>0:
                b.no_of_copies-=1
                b.save()
                rec.save()
                return render(request, 'book_issue_form.html',{"success":True,"no_copies":False,"book_not_found":False})
            else:
                return render(request, 'book_issue_form.html',{"no_copies":True,"success":False,"book_not_found":False})
    else:
        return render(request, 'book_issue_form.html', {"book_not_found": True,"no_copies":True,"success":False})




def return_book(request):
    book = books.objects.all()
    rec = record.objects.all()
    b_id = request.POST["book_id"]
    s_id = request.POST["student_id"]
    yr = request.POST["year"]
    s_name = request.POST["student_name"]
    for r in rec:
        if b_id==r.book_id and s_id==r.student_id:
            r.return_date = datetime.now()
            for b in book:
                if b_id==b.book_id:
                    b.no_of_copies+=1
                    b.save()
            r.save()
            return render(request, 'book_return_form.html',{"success":True,"record_not_found": False})
    else:
        return render(request, 'book_return_form.html', {"record_not_found": True,"success":False})
    # return redirect('/records/book_return_form')

def display_records(request):
    rec = record.objects.all()
    list=[]
    for r in rec:
        list.append(r)
    return render(request,'display_records.html',{"list":list})