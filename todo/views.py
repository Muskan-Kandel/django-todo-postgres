from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Todo
from .forms import TodoForm

# Create your views here.
def register(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                    messages.error(request, "Email taken")
                    return redirect('register')
            else:   
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print("User created")
                return redirect('login')
        else:
            messages.error(request, "Passwords do not match")
            return redirect('register')
        
    else:
        return render(request, 'todo/register.html')
    



def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')
    else:
        return render(request, 'todo/login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('login')

# to add items in todo list
def index(request):

    item_list = Todo.objects.filter(user=request.user).order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo_item = form.save(commit=False)
            todo_item.user = request.user # We manually attach the logged-in user
            todo_item.save() # save to Postgres
            return redirect('index')
    form = TodoForm()

    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'todo/index.html', page)

def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed!")
    return redirect('index')