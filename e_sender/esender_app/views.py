from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
    send_mail(
        'Hello its testing',
        'Hello its testing message for django app',
        'forappsofbarkhayot@gmail.com',
        ['barkhayotoff@gmail.com'],
        fail_silently=False
    )
    return render(request, 'index.html')
