from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from django.http import HttpResponse
# relative import of forms
from .models import Test1Model
from .forms import Test1Form



# Create your views here.
# def index(request):
#     return HttpResponse("Hello, world. You're at the test1 index.")


def create_view(request):
	# dictionary for initial data with
	# field names as keys
	context ={}

	# add the dictionary during initialization
	form = Test1Form(request.POST or None)
	if form.is_valid():
		form.save()
		
	context['form']= form
	return render(request, "test1/create_view.html", context)

def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = Test1Model.objects.all()
         
    return render(request, "test1/list_view.html", context)

# pass id attribute from urls
def detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["data"] = Test1Model.objects.get(id = id)
         
    return render(request, "test1/detail_view.html", context)

# update view for details
def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Test1Model, id = id)
 
    # pass the object as instance in form
    form = Test1Form(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/test1/"+id)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "test1/update_view.html", context)

# delete view for details
def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Test1Model, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/test1")
 
    return render(request, "test1/delete_view.html", context)
