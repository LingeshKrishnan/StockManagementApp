from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .forms import *
from .models import *
# Create your views here.
def index(request):
    return render(request,'index.html')

def displayNighty(request):
    items = Nighty.objects.all()

    context = {
       'items' : items,
       'header' : "Nighty",
    }

    return render(request,'index.html',context)

def displayInskirt(request):
   items = Inskirt.objects.all()

   context = {
      'items' :items,
      'header' : "Inskirt",
   }

   return render(request,'index.html',context)

def displayBlouse(request):
   items = Blouse.objects.all()

   context = {
      'items' : items,
      'header' : "Blouse",
   }

   return render(request, 'index.html', context)

def displaySaree(request):
   items = Saree.objects.all()

   context = {
      'items' : items,
      'header' : "Saree",
   }

   return render(request, 'index.html', context)


def addItem(request,cls):
   if request.method == 'POST':
      form = cls(request.POST)

      if form.is_valid():
         form.save()
         return redirect('index')

   else :
      form = cls()
      return render(request, 'add_new.html', {'form':form})

def addNighty(request):
   return addItem(request,Nightyform)

def addInskirt(request):
   return addItem(request,Inskirtform)

def addBlouse(request):
   return addItem(request,Blouseform)

def addSaree(request):
   return addItem(request,Sareeform)

def editItem(request,pk,model,cls):
   item = get_object_or_404(model,pk=pk)

   if request.method == "POST":
      form = cls(request.POST,instance=item)
      if form.is_valid():
         form.save()
         return redirect('index')

   else:
      form = cls(instance=item)

      return render(request,'edit_item.html',{ 'form':form })

def editNighty(request,pk):
   return editItem(request,pk,Nighty,Nightyform)

def editInskirt(request,pk):
   return editItem(request,pk,Inskirt,Inskirtform)

def editBlouse(request,pk):
   return editItem(request, pk, Blouse, Blouseform)

def editSaree(request,pk):
   return editItem(request,pk,Saree,Sareeform)
      

def deleteNighty(request,pk):

   Nighty.objects.filter(id=pk).delete()

   items = Nighty.objects.all()

   context = {
      'items': items,
   }

   return render(request,'index.html',context)

def deleteInskirt(request,pk):
   Inskirt.objects.filter(id=pk).delete()

   Inskirt.objects.all()

   context = {
      'items' : items,
   }

   return render(request,'index.html',context)

def deleteBlouse(request,pk):
   Blouse.objects.filter(id=pk).delete()

   Blouse.objects.all()

   context = {
      'items' : items,
   }

   return render(request,'index.html',context)

def deleteSaree(request,pk):
   Saree.objects.filter(id=pk).delete()

   Saree.objects.all()

   context = {
      'items' : items,
      }
   return render(request,'index.html',context)