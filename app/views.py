from django.shortcuts import render
from . import forms
from django.http import HttpResponse
from app.models import Post
import requests
from django.utils import timezone

# Create your views here.
def blog(request):
    try:
        res = requests.get('https://08ad1pao69.execute-api.us-east-1.amazonaws.com/dev/random_ten')
    
        joke= res.json()
        time = timezone.now()
        for me in joke:
            jokes = joke
            setup = me["setup"]
            punchline = me["punchline"]
            type = me["type"]
        joking = True
    except:
        jokes = 0
        setup = 0
        punchline = 0
        type=0
        time = 0
        joking = False
    
    model_view = Post.objects.all()
    return render(request,'app/blog.html',{'model_view':model_view,'setup':setup,'punchline':punchline,'jokes':jokes,'time':time,'type':type,'joking':joking})



def about(request):
    return render(request,'app/about.html')

def post(request):
    if request.method == 'GET':
        form = forms.PostForm()
    
        return render(request,'app/post.html', {'form':form})

    elif request.method == 'POST':

        form = forms.PostForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        
            return render(request,'app/blog.html')

def index(request):
  
    return render(request,'app/index.html')

def contact(request):
    return render(request,'app/contact.html')


