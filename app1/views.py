from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseForbidden
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from startup.settings import EMAIL_HOST_USER
from smtplib import SMTPConnectError
from .models import Post
from .forms import PostForm


def home(request): 
    return render(request,'index.html')

def about(request): 
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        
        email_body = f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"

       
        msg = EmailMultiAlternatives(
            subject=subject,
            body=email_body,
            from_email=email,
            to=['hallotechofficial@gmail.com']
        )
        msg.send()
    return render(request,'about.html')

def feature(request): 
    return render(request,'feature.html')
def blog(request): 
    return render(request,'blog.html')

def contact(request): 
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Construct the email body to include name, email, subject, and message
        email_body = f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"

        # Send the email
        msg = EmailMultiAlternatives(
            subject=subject,
            body=email_body,
            from_email=email,
            to=['hallotechofficial@gmail.com']
        )
        msg.send()

    # Regardless of whether the form was submitted or not, render the contact.html template
    return render(request, 'contact.html')

def detail(request): 
    return render(request,'detail.html')
def price(request): 
    return render(request,'price.html')
def quote(request): 
    return render(request,'quote.html')

def service(request): 
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        service = request.POST.get('service')
        message = request.POST.get('message')
        
        # Construct the email body to include name, email, subject, and message
        email_body = f"Name: {name}\nEmail: {email}\nService: {service}\nMessage: {message}"

        # Create EmailMultiAlternatives instance
        msg = EmailMultiAlternatives(
            subject='Service Request',  # Set the subject here
            body=email_body,
            from_email=email,
            to=['hallotechofficial@gmail.com']
        )

        # Send the email
        msg.send()

    return render(request, 'service.html')

def team(request): 
    return render(request,'team.html')
def testimonial(request): 
    return render(request,'testimonial.html')
def web_price(request): 
    return render(request,'w_price.html')
def iot_price(request): 
    return render(request,'iot_price.html')
def ai_price(request): 
    return render(request,'ai_price.html')
def hardware_price(request): 
    return render(request,'h_price.html')
def media_price(request): 
    return render(request,'m_price.html')

def project(request):
    Posts = Post.objects.all()
    return render(request, 'projects.html', {'Posts': Posts})