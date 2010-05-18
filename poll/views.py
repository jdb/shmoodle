# Create your views here.

import models
import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist


def poll(r):
    return render_to_response('poll.html',{'poll':forms.Poll()})


def poll_handler(r):

    f = forms.Poll(r.POST)
    if f.is_valid():
        urlid = models.Poll.make_urlid()
        p=models.Poll(
            description = f.cleaned_data['description'],
            question    = f.cleaned_data['question'], 
            choices     = f.cleaned_data['choices'],
            urlid       = urlid)
        p.save()        
        return HttpResponseRedirect('/vote/'+urlid)
    else:
        return HttpResponseRedirect('/',)


def vote(r):

    # either the voter has just casted his ballot, in which case, the
    # post handler has appended a ?voter='name' and the models.Voter
    # should be passed to the template to present smart initials

    # or the voter has not just voted, she is unidentified, the
    # initial value for the form are the default values

    urlid = r.path.split('/')[-1]
    poll = models.Poll.objects.get(urlid=urlid)    


    if r.GET and r.GET.get('name'):
        name = r.GET.get('name')
        try:
            v = poll.voter_set.get(name=name)
        except ObjectDoesNotExist:
            v = models.Voter(name=name)
            

        voter = forms.Voter({
                'name':v.name,
                'prefs':v.prefs,
                'comment':v.comment})
    else:
        voter = forms.Voter()

    return render_to_response('vote.html',{
            'question':poll.question,
            'description':poll.description,
            'choices':poll.choice_list(),
            'voters':[(v.name,v.pref_list(),v.comment) for v in poll.voter_set.all()],
            'results':poll.results(),
            'form':voter,
            'urlid':urlid})
                                   
def vote_handler(r):

    # either the voter has already voted and his name is among the
    # voters of the poll, no new voter must be created, only his
    # choices must be updated

    # or the voter has never voted with this name and she must be created

    urlid = r.path.split('/')[-1]
    poll = models.Poll.objects.get(urlid=urlid)
    
    f = forms.Voter(r.POST)
    if f.is_valid():
        name = f.cleaned_data['name']
        if name in [ v.name for v in poll.voter_set.all()]:
            v = poll.voter_set.get(name=name)
        else:
            v = models.Voter(name=name)
            v.poll = poll

        v.prefs = f.cleaned_data['prefs']
        v.comment = f.cleaned_data['comment']
        v.save()

        return HttpResponseRedirect('/vote/'+urlid+'?name='+name)

    
