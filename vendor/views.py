from django.shortcuts import render


def vprofile(request):
    return render(request, 'vendor/vprofile.html')


def menu_builder(request):
    return render(request, 'vendor/vprofile.html')
