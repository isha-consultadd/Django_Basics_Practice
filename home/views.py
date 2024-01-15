from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    peoples = [{'Name':'Isha' , 'Age':21},
               {'Name':'Goldy' , 'Age':17},
               {'Name':'Shubham' , 'Age':25},
               {'Name':'Tara' , 'Age':16},]
    text = """
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Sunt eum dolore esse ut enim fuga maiores doloribus, veritatis corporis, assumenda tempora ad, molestias quis praesentium labore dolor asperiores suscipit deserunt.
     """
    vegetables = ['tomato' , 'potato' , 'chilli']
    return render(request, "home/index.html" , context = {'peoples':peoples , 'text': text , 'vegetables': vegetables })

def about(request):
    return render(request , "home/about.html")

def contacts(request):
    return render(request , "home/contacts.html")

def success_page(request):
    return HttpResponse("<h2>Hi this is Success Page</h2>")
# Create your views here.
