from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.utils import timezone
from recipeapp.models import Login,Recipe
from django.contrib.auth.models import User
from recipeapp.forms import RegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'recipeapp/index.html')


def checkuser(request):
    if request.method== 'POST':
        un=request.POST.get('un')
        pw=request.POST.get('pw')
        qs=Login.objects.filter(username=un,password=pw)
        if qs:
            request.session['surya']= 'Surya'
            return render(request, 'recipeapp/add_recipe.html')
        else:
            return render(request, 'recipeapp/index.html', {'mess': 'please Check Username and Password'})
    else:
        return render(request, 'recipeapp/index.html')




def register(request):
    form=RegisterForm()
    if request.method=='POST':
        f1=RegisterForm(request.POST)
        if f1.is_valid():
            f1.save()
            return render(request,'recipeapp/index.html',{'mess':'Thank you for Registration,Please Login to access services'})
    return render(request,'recipeapp/register.html',{'form':form})




def AddRecipe(request):
    if request.session['surya']=='Surya':
        recipe_name=request.POST.get('rname')
        cook_name=request.POST.get('cname')
        recipe_ingrediants=request.POST.get('ring')
        recipe_process=request.POST.get('rproc')
        qs=Recipe.objects.filter(recipe_name=recipe_name,cook_name=cook_name)
        if len(qs)==0:
            Recipe(recipe_name=recipe_name,cook_name=cook_name,recipe_ingrediants=recipe_ingrediants,recipe_process=recipe_process).save()
        qs=Recipe.objects.all()
        return render(request,'recipeapp/recipe_list.html',{'data':qs})
    else:
        return redirect('/')



def afterdeleted(request,id):
    Recipe.objects.get(id=id).delete()
    qs=Recipe.objects.all()
    return render(request,'recipeapp/recipe_list.html',{'data':qs})



def detailsofrecipie(request,id):
    obj=Recipe.objects.get(id=id)
    return render(request,'recipeapp/recipe_detail.html',{'obj':obj})



def backtolist(request):
    qs=Recipe.objects.all()
    return render(request,'recipeapp/recipe_list.html',{'data':qs})


def backtoaddrecipe(request):
    return render(request,'recipeapp/add_recipe.html')





def logoutpage(request):
    print('ok')
    request.session['surya']='Thanks'
    print(request.session['surya'])
    return redirect('/')