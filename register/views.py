from django.shortcuts import render,redirect
from .forms import modForm
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Polls,Choice
from django.urls import reverse
from django.utils import timezone


def SignUp(request):
	if request.method == 'POST':
		form = modForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
		
	
	else:
		form = modForm()
	
	return(render(request, 'signup.html', {'forms':form}))
	
	
def vote_index(request):
	#elections=Polls.objects.filter(date_of_election__lte=timezone.now())
	elections=Polls.objects.order_by('-date_of_election')[:3]
	return render(request,'vote_index.html',{'elections':elections})
def vote_view(request):
	
	elections=Polls.objects.order_by('-date_of_election')[:3]
	#latest_elections=Polls.objects.get(id=3)
	
	return render(request,'vote_index.html',{'elections':elections})

def details(request,id):
	#cands=get_object_or_404(Polls.objects.get(pk=id))
	cands=(Polls.objects.get(pk=id))
	return render(request,'registration/voting1.html',{'cands':cands})
	#return HttpResponse("this : %s" %id)
	
def vote_results(request, id):
	cands=get_object_or_404(Polls,pk=id)
	return render(request,'registration/vote_results.html',{'cands':cands})
def vote(request,id):
	cands=get_object_or_404(Polls,pk=id)
	#pk=request.POST['choice']
	#selected_cand=cands.choice_set.get(3)
	#selected_cand=cands.choice_set.get(pk=request.POST['choice'])
	#return HttpResponse("this is : %s" %pk)
	
	try:
		selected_cand=cands.choice_set.get(pk=request.POST['choice'])
	except:
		return render(request,'registration/voting1.html',{'cands':cands,'error_message':"please select a choice"})
	else:
		selected_cand.cand_count+=1
		selected_cand.save()
		
		return HttpResponseRedirect(reverse('vote_results',args=(cands.id,)))
	
