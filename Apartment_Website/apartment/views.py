from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import Email_Details

def index(request):
    if request.method == "POST":
        first_name = request.POST["f_name"]
        last_name = request.POST ["l_name"]
        email = request.POST["email"]
        message = request.POST["message"]
        form = Email_Details(first_name =first_name , last_name = last_name ,email = email)
        form.save()
        
    # sending mail => subject , message , from email , to email
        send_mail(
            first_name +' ' +last_name,
            message ,
            email ,
            ["networkdelta47@gmail.com"]
        )
        return render (request , "index.html" ,{"f_name":first_name })
    else:
        return render (request ,"index.html" , {})