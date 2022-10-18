from turtle import home
from urllib import response
from django.shortcuts import render,redirect,reverse
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect

# Create your views here.


def userlogin(request):

  if 'username' in request.session and 'username' in request.COOKIES:
    if request.session['username']==request.COOKIES['username']:
      return redirect(result)
  
  if request.method=='POST':

    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username = username,password = password)
    response=redirect('result')

    if user is not None:

      response.set_cookie('username', username)

      request.session['username']= username
      
      return response
    else:

      return render(request,'login.html')

  return render(request,'login.html')


def result(request):

  if 'username' in request.session and 'username' in request.COOKIES:
    return render(request, 'result.html')
  return redirect(userlogin)


def userlogout(request):

  response =HttpResponseRedirect(reverse('login'))

  request.session.flush()
  response.delete_cookie('username')
  return response

