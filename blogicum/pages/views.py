from django.shortcuts import render


# Create your views here.
def about(request):
    tempalate = 'pages/about.html'
    return render(request, tempalate)


def rules(request):
    template = 'pages/rules.html'
    return render(request, template)
