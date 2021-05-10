from django.shortcuts import render
from .forms import UserForm


def registeration(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request, 'regitration.html', {'r_regis': user_form,
                                                 'registered': registered})

# Create your views here.
