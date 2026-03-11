from django.shortcuts import render
from django.views import View


# Create your views here.
class UploadFile(View):
    def get(self, request):
        return render(request, "profiles/upload_file.html")
    
    def post(self,request):
        file = request.FILES["file_upload"]
        if file:
            # Handle the uploaded file here
            pass
        return render(request, "profiles/upload_file.html")
