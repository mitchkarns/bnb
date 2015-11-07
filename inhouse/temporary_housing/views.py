from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def index(request):
    return HttpResponse("You found my secret place!")

@login_required(login_url='/temp/login/')
def view_all_users(request):
    username = request.user.username
    return HttpResponse("Swag" + username)
#    allUsers = UserProfile.objects.all()
#    return render(request, "temporary_housing/users.html", {'allUsers':allUsers})

def logout_view(request):
    logout(request)
    return HttpResponse("You logged out")
# Create your views here.
