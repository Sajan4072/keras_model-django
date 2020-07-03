from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    context={}
    return render(request,'index.html',context)
    
def classifier(request):
    fileObj=request.FILES['fileP']
    fs=FileSystemStorage()
    path=fs.save(fileObj.name,fileObj)
    path=fs.url(path)

    

    context={'path':path}
    return render(request,'index.html',context)

