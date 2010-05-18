
from django.forms import Form,CharField, BooleanField, DateField

class Poll(Form):
       
    description = CharField(
        max_length = 50,
        label      = "Poll description",
        required   = False,
        initial    = '2010: the revenge of the theatrico-lawyers')

    question = CharField(
        max_length = 50,
        label      = 'The question',
        initial    = 'Which ones do we want to play?')

    choices = CharField(
        max_length = 50,
        initial    = "Romeo and Juliette,Phedre",
        label      = "Choices")

    # number_of_point = IntegerField(label=10)
    # name            = CharField(max_length=10,null=True)    
    # passwd          = PasswdField

    
class Voter(Form):
    name = CharField(
        max_length = 50,
        label      = 'name',
        initial    = 'milou')

    prefs = CharField(
        max_length = 50,
        label      = 'prefs',
        initial    = '8,2')

    comment = CharField(
        max_length = 50,
        label      = 'comment',
        initial    = 'Romeo, O Romeo',
        required   = False) 

