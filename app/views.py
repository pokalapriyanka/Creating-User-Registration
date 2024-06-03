from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.
def registration(request):
    d={'EUFO':UserForm(),'EPFO':ProfileForm()}
    if request.method=='POST' and request.FILES:
        NMUFDO=UserForm(request.POST)
        NMPFDO=ProfileForm(request.POST,request.FILES)
        if NMUFDO.is_valid() and NMPFDO.is_valid():
            MUFDO=NMUFDO.save(commit=False)
            pw=NMUFDO.cleaned_data['password']
            MUFDO.set_password(pw)
            MUFDO.save()
            send_mail('Registration',
            'Thank you for Registering',
            'p9584520@gmail.com',
            [MUFDO.email],
            fail_silently=False
            )
            MPFDO=NMPFDO.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()
            return HttpResponse('Registration is Successfull')
        else:
            return HttpResponse('Invalid data')

    return render(request,'registration.html',d)