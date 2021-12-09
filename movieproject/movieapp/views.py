
from django.shortcuts import redirect, render
from movieapp.form import movieform
from.models import movie
# Create your views here.

def home(request):
    movie_list=movie.objects.all()
    context={'movie':movie_list}
    return render(request,'index.html',context)

def detail(request,movie_id):
    movie1=movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'movie':movie1})

def add(request):
        if request.method=='POST':
            name=request.POST.get('name')
            des=request.POST.get('description')
            year=request.POST.get('year')
            image=request.FILES['image']
            movie2=movie(name=name,description=des,year=year,image=image)
            movie2.save()

        return render(request,'add.html')

def update(request,id):
    movie3=movie.objects.get(id=id)
    form=movieform(request.POST or None, request.FILES, instance=movie3) 
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'movie':movie3})

def delete(request,id):
    if request.method=='POST':
        movie4=movie.objects.get(id=id)
        movie4.delete()
        return redirect('/')

    return render(request,'delete.html')

