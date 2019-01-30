from django.forms import ModelForm
from .models import Vote, Candidate, Position

class VoteModelForm(ModelForm):
    class Meta:
        model = Candidate
        exclude = ['id']


class VoteModelForm1(ModelForm):
    class Meta:
        model = Position
        exclude = ['id']



class VoteModelForm2(ModelForm):
    class Meta:
        model = Vote
        exclude = ['id']
