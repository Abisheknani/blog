from django.shortcuts import render


def custom_page_not_found(request,excption):
    return render(request,'404.html', status=404)
