from django.shortcuts import render,redirect
from .models import Book
from .forms import Form_Book
# Create your views here.
def create_book(request):
    form=Form_Book(request.POST or None)
    context={
        'forms':form,
    }
    if request.method=='POST':
        if form.is_valid():
            created_book=form.save()
            context['forms']=Form_Book()
            context['object']=created_book
            context['created']=True
    
    
    return render(request,'book_form.html',context)


def index(request):
    data=Book.objects.all()
    context={
        'All__data':data
    }
    return render (request,'index.html',context)


def update(request,pk):
    book = Book.objects.get(id=pk)
    if request.method=='POST':
        form = Form_Book(request.POST,instance=book)
        if form.is_valid():
             form.save()
             return redirect('/') 
    else:
        form = Form_Book(instance=book)
    
    context={
        'form':form
    }
    return render(request,'edit.html',context)

def delete(request,id):
    book=Book.objects.get(id=id)
    book.delete()
    return redirect('/')
    
   