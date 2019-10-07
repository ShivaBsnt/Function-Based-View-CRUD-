from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def register(request):

    if request.method == 'POST':
        first = request.POST.get('first_name')
        last = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('password_confirmation')

        if password == confirm_password:
            user = User.objects.create(username=username, email=email, first_name=first, last_name=last)
            user.set_password(password)
            user.save()
        # messages.success(request, f'Your data has been saved!Thanks for information)
        return redirect('login')

    return render(request, 'users/register.html', {'check': True})


@login_required()
def index(request):
    users = User.objects.all()
    return render(request, 'index.html', {'users': users})


def delete(request, pk):

    if request.method == 'POST':
        user = User.objects.get(id=pk)

        user.delete()
        return redirect('index')

    return render(request, 'delete.html')


def update(request, pk):

    user = User.objects.get(id=pk)
    if request.method == 'POST':
        first = request.POST.get('first_name')
        last = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        user.first_name = first
        user.last_name = last
        user.username = username
        user.email = email
        user.save()
        return redirect('index')

    return render(request, 'users/register.html', {'user': user})



