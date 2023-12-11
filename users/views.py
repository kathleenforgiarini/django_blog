from django.shortcuts import redirect, render
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm

# Create your views here.

def register(request):

    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        # form = UserCreationForm()
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})



def profile(request):
    return render(request, 'users/profile.html')