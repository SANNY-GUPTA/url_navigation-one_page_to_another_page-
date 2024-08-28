from django.shortcuts import render


def loop(request):
    d={'name':'sanny'}
    return render(request,'loop.html',d)

def condition(request):
    d={'a':10,'b':20}
    return render(request,'condition.html',d)


# Create your views here.
