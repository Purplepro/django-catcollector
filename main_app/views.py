from django.shortcuts import render
from django.urls.resolvers import URLPattern
from .models import Cat
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect

# Create your views here.

def about(request):
    return render(request, 'about.html')

   
def index(request):
    return render(request, 'index.html')


# class Cat:
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age



# cats = [
#     Cat('Lolo', 'tabby', 'foul little demon', 3),
#     Cat('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
#     Cat('Raven', 'black tripod', '3 legged cat', 4)
# ]
def cats_index(request):
    cats = Cat.objects.all()
    data = { 'cats': cats }
    return render(request, 'cats/index.html', data)


def cats_show(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    data = { 'cat': cat }
    return render(request, 'cats/show.html', data)



class CatCreate(CreateView):
  model = Cat
  fields = '__all__'
  success_url = '/cats'

class CatUpdate(UpdateView):
  model = Cat
  fields = ['name', 'breed', 'description', 'age']

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.save()
    return HttpResponseRedirect('/cats/' + str(self.object.pk))

class CatDelete(DeleteView):
  model = Cat
  success_url = '/cats'
