from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from models import TestProfile, Post

count = 0

def index(request):
    return HttpResponse("You found my secret place!")

@login_required(login_url='/temp/login/')
def test(request):
    invite = Invitation.create('mitchkarns@gmail.com', inviter=request.user)
    invite.send_invitation(request)

@login_required(login_url='/temp/login/')
def invite_users(request):
    user = TestProfile.objects.get(email=request.user.email)
    if user.is_admin:
        x = 1
    else:
        return redirect('/temp')


@login_required(login_url='/temp/login/')
def view_all_or_search(request):
    posts = Post.objects.all().order_by('region')
    context = {'posts': posts}
    return render(request, 'temporary_housing/all_posts.html', context)


@login_required(login_url='/temp/login/')
def view_all_users(request):
    username = request.user.email
    user = TestProfile.objects.get(email=request.user.email)
    return HttpResponse(
        "You have logged in: " + username + " " + "\tthis is user: " + user.first_name + ' ' + user.last_name)


#    allUsers = UserProfile.objects.all()
#    return render(request, "temporary_housing/users.html", {'allUsers':allUsers})

@login_required(login_url='/temp/login/')
def edit_or_create_post(request):
    try:
        user = TestProfile.objects.get(email=request.user.email)
        post = Post.objects.get(user=user)
    except Post.DoesNotExist:
        post = None
    except TestProfile.DoesNotExist:
        user = None

    print('this is num of posts ' + str(user.num_posts))
    if request.GET.get('add'):
        if user is not None and post is None:
            user.num_posts += 1
            post = Post(user=user, region=user.region, sub_region='Berkeley', distance='', house_type='Floor',
                        provided='Pillows', proximity='10 minute walk', num_people=1)
            post.save()
    elif request.GET.get('delete'):
        if user.num_posts > 0:
            user.num_posts -= 1
        if post is not None:
            post.delete()
    user.save()
    context = {'user': user, 'post': post}
    return render(request, 'temporary_housing/edit_or_create_post.html', context)


@login_required(login_url='/temp/login/')
def logout_view(request):
    logout(request)
    return HttpResponse("You logged out")

# Create your views here.
