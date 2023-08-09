from django.shortcuts import render

def page_1(request):

    return render(request, 'page_1.html', locals())
