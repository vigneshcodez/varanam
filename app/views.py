from django.shortcuts import render
from . models import Blog,Location,Testimonial

# Create your views here.

def index(request):
    blog = Blog.objects.all()
    location = Location.objects.all()
    testimonial = Testimonial.objects.all()
    return render(request,'pages/index.html',{'blog':blog,'location':location,'testimonial':testimonial})
