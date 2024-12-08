from django.shortcuts import render

# Create your views here.

def jinja_print(request):
    d= {'name':'Gaurav','age': 23}
    return render(request,'jinja_print.html',context=d)  

def conditions(request):
    d= {'name':'Desai','age': 23}
    return render(request,'conditions.html',context=d) 
           
