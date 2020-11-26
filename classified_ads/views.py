from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Ad, PoorUser
from django.db import connection

def index(request):
  try:
    request.session['user']
  except:  
    return redirect('/login')
  ads = Ad.objects.filter()
  context = { 'ads': ads, 'user': request.session['user'] }
  return render(request, 'classified_ads/index.html', context)

def addView(request):
  new_ad = request.POST.get('new_ad')
  with connection.cursor() as cursor:
    cursor.executescript("INSERT INTO classified_ads_ad (creator, text) VALUES('{}','{}')".format(request.session['user'], new_ad))
  return redirect('/')

def loginView(request):
  return render(request, 'classified_ads/login.html')

def login(request):
  username = request.POST.get('username')
  password = request.POST.get('password')
  try:    
    user = PoorUser.objects.get(username = username)
    print(user.password)
    if(user.password == password):
      request.session['user'] = user.username
      print("Success")   
      return redirect('/')
  except:
    print("Failure") 
  
  return redirect('/login')
  
  
  
    
   

def newPassword(request):
  return render(request, 'classified_ads/new_password.html', { 'user': request.session['user'] })

def setPassword(request):
  user = request.session['user']
  if(user):
    user = PoorUser.objects.get(username = user)
    new_password = request.POST.get('new_password')
    user.password = new_password
    user.save()
    
  return redirect('/')