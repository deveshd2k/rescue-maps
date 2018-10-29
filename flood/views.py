from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Coordinates,Profile,userInfo,userData,rescueCenter
from .forms import userForm,SignUpForm,userInfoform
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
from django.db.models import Sum,Avg
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
import Features, EntitiesOptions, KeywordsOptions

# Create your views here.

def index(request):
	return render(request,'index.html',{})

def signup(request):
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():	
			addProfile = Profile()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			addProfile.username = form.cleaned_data['username']
			addProfile.orgName = form.cleaned_data['orgName']
			addProfile.bedsno = form.cleaned_data['bedsno']
			addProfile.rescueHome = form.cleaned_data['rescueHome']
			addProfile.contact = form.cleaned_data['contact']
			addProfile.save()
			form.save()
			user = authenticate(username=username, password=raw_password)
			login(request,user)
			return HttpResponseRedirect('org_map')
	else:
		form = SignUpForm()
	return render(request,'signup.html',{'form':form})

@login_required(login_url='/login')
@csrf_exempt
def org_map(request):
	queryset = Coordinates.objects.all()
	if request.method == "POST":
		lattitude = request.POST['lattitude']
		longitude = request.POST['longitude']
		if request.user.is_authenticated:
			username = request.user.username
		instance1 = Profile.objects.get(username=username)
		instance1.lattitude = lattitude
		instance1.longitude = longitude
		instance1.save()
		Coordinates.objects.filter(lattitude=lattitude).delete()
	instance = Profile.objects.all()
	return render(request,'org_map.html',{'instance':instance,'queryset':queryset})

@login_required(login_url='/login')
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/')

def user_map(request):
	instance = Profile.objects.all()
	keys = range(1,21)
	values = zip(instance,keys)
	if request.method == "POST":
		form = userInfoform(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
		else:
			print(form.errors)
	else:
		form = userInfoform()
	return render(request,'individual-map.html',{'values':values,'form':form})

def survey(request):
	instance  = Profile.objects.all()
	if request.method == "POST":
		form = userForm(request.POST)
		feedback = request.POST['feedback']
		print(feedback)
		natural_language_understanding = NaturalLanguageUnderstandingV1(
		  username='768a0850-17e8-4466-910a-06e4c27da917',
		  password='e7Eszx2G322K',
		  version='2018-03-16')

		response = natural_language_understanding.analyze(
		  text= feedback,
		  features=Features(
		    entities=EntitiesOptions(
		      emotion=True,
		      sentiment=True,
		      limit=2),
		    keywords=KeywordsOptions(
		      emotion=True,
		      sentiment=True,
		      limit=2))).get_result()
		value = response['keywords'][0]['sentiment']['score']
		updated_data = request.POST.copy()
		updated_data.update({'degree': value}) 
		form = userForm(data=updated_data)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
		else:
			print(form.errors)
	else:
		form = userForm()
	return render(request,'survey.html',{'form':form,'instance':instance})

@login_required(login_url='/login')
@csrf_exempt
def orgdash(request):
	if request.user.is_authenticated:
		username = request.user.username
		rescueHome = Profile.objects.filter(username=username).values('rescueHome')[0]['rescueHome']
		tsum = userInfo.objects.filter(username=username).aggregate(Sum('family'))['family__sum']
		if tsum == None:
			tsum=0
		avg = userData.objects.filter(rescueHome=rescueHome).aggregate(Avg('degree'))['degree__avg']
		if avg==None:
			avg = 0
		avg = int((avg+1)*50)
		bedsno = Profile.objects.filter(username=username).values('bedsno')
		total = int(bedsno[0]['bedsno']) - tsum
		instance = Profile.objects.get(username=username)
		queryset = userInfo.objects.filter(username=username)
	return render(request,'orgdash.html',{'instance':instance,'queryset':queryset,'total':total,'avg':avg})

@login_required(login_url='/login')
def rescueCenter(request):
	if request.method == "POST":
		rescueCenter = rescueCenter()
		lattitude = request.POST['lattitude']
		longitude = request.POST['longitude']
		if request.user.is_authenticated:
			username = request.user.username
			rescueCenter.username = username
			rescueCenter.lattitude = lattitude
			rescueCenter.longitude = longitude
			rescueCenter.save()
			return HttpResponseRedirect('dashboard')
	return render(request,'rescueCenter.html',{})