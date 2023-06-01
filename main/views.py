from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda user: user.is_superuser)
def contact_view(request):
    return render(request, 'contact.html')

def default(request):
    return render(request, 'default.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

