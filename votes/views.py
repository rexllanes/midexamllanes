from django.shortcuts import render
from .forms import VoteModelForm, VoteModelForm1, VoteModelForm2

# Create your views here.

def index(request):
    context = {}
    votes = Vote.objects.all()




def candidate_detail(request, vote_id):
    context = {}
    context ['vote'] = Vote.objects.get(id=post_id)
    context['candidate'] = Candidate.objects.filter(post=post_id) [::-1]
    conext['position'] = Position.objects

    return render(request, 'candetail.html', context)






def candidate_create(request, vote_id):
    context = {}

    if request.method == 'POST':
        form = VotesModelForm(request.POST)
        if form.is_Valid():
            form.save()
            return index(request)
        else:
            context['form'] = form
            return render(request, 'cancreate.html', context)
    else:
        context['form'] = VoteModelForm()
        return render(request, 'cancreate.html', context)




def candidate_update(request, vote_id):
    vote = Vote.objects.get(id=post_id)
    context = {}

    if request.method == 'POST':
        form = VoteModelForm(request.POST, instance=vote)
        if form.is_valid():
            form.save()
            return candetail(request, post_id)
        else:
            context['form'] = form
            return render(request, 'canupdate.html', context)
    else:
        context['form'] - VoteModelForm(instance = post)
        return render(request, 'canupdate.html', context)





def position_create(requestvote_id):
    context = {}

    if request.method == 'POST':
        form = VotesModelForm(request.POST)
        if form.is_Valid():
            form.save()
            return index(request)
        else:
            context['form'] = form
            return render(request, 'cancreate.html', context)
    else:
        context['form'] = VoteModelForm()
        return render(request, 'cancreate.html', context)



def vote(request, vote_id):
    context = {}
