from django.http import HttpResponse
from django.shortcuts import render
from . models import Place, Team
# Create your views here.


def demo(request):
    name="India"
    return render(request, "home.html",{"obj":name})
def contact(request):
    return render(request, "contact.html")

def dispaly(request):
    return HttpResponse("Hello! You are welcome")
def index(request):
    obj = Place.objects.all()
    people = Team.objects.all()
    return render(request, "index.html", {'result': obj, 'team':people})