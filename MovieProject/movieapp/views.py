from django.shortcuts import render
from movieapp.forms import MovieForm
from movieapp.models import Movie

# Create your views here.
def index_view(request):
    return render(request,'movieapp/index.html')

def addmovie_view(request):
    form=MovieForm()
    if request.method=='POST':
        form=MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=TRUE)
        return index_view(request)
    return render(request,'movieapp/addmovie.html',{'form':form})

def movie_list_view(request):
    movie_list=Movie.objects.all()
    return render(request,'movieapp/listmovie.html',{'movie_list':movie_list})
