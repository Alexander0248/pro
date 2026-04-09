from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.core.files.storage import FileSystemStorage


def process_get_view(request: HttpRequest) -> HttpResponse:
    a = request.GET.get("a", "")
    b = request.GET.get("b", "")
    result =a + b
    context = {
        "a": a,
        "b": b,
        "result": result,
    }
    return render(request, "requestdataapp/request-query-params.html", context=context)


def user_form(request: HttpRequest) -> HttpResponse:
    return render(request, "requestdataapp/user-bio-form.html")


def handle_file_upload(request: HttpRequest) -> HttpResponse:
    if request.method == "POST" and request.FILES.get("myfile"):
        myfile = request.FILES["myfile"]
        max_size_file = 1024 * 1024
        if myfile.size > max_size_file:
            return HttpResponse ("The maximum file size for import is 1 MB.")
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        print("saved file", filename)
    return render(request, "requestdataapp/file-upload.html")
# Create your views here.
