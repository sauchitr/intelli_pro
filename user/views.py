from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile, UserSearch, UserProfile
from django.contrib.auth import get_user_model
from django.db import models


# def profile(request):
#     return render(request, 'user/profile.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Your account is created. Kindly login")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, "user/register.html", {"form": form})

@login_required
def profile(request):
    # user = get_object_or_404(get_user_model())
    # profile = user.profile
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)

        if u_form.is_valid():
            u_form.save()
            messages.success(request, f"Your account has been updated!")
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
    context = {
        'u_form': u_form,
    }
    return render(request, "user/profile.html", context)



def search(request):
    query = request.GET.get('q')

    if query:
        results = get_user_model().objects.filter(
            models.Q(name__icontains=query) |
            models.Q(mobile__icontains=query) |
            models.Q(email__icontains=query)
        ).exclude(id=request.user.id)
    else:
        results = []

    return render(request, 'user/search.html', {'results': results, 'query': query})