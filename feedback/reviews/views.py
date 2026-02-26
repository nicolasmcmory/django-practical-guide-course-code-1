#views: reviews
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def review(request):
    return render(request,"reviews/review.html")
