

from django.db.models import Model, ForeignKey
from django.db.models import CharField, BooleanField, DateField
from django.db.models import CommaSeparatedIntegerField, IntegerField

from time import strftime
from random import sample

# If django models can't store agregates, then let's just use custom
# aggregate fields for the fields and for the votes: strings of string
# separated by ^^. I know, I know, this is ugly, I would rather store
# multivalued column (list of choices)

_range = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

class Poll(Model):
       
    description = CharField(
        max_length = 50,
        null = True)

    question = CharField(
        max_length = 50,
        default    = 'Which?')

    choices = CharField(
        max_length = 50,
        default    = "Romeo and Juliette, Phedre")

    def choice_list(self):
        return self.choices.split(',')

    date = DateField(
        default = strftime('%Y-%m-%d'))

    number_of_point = IntegerField(
        default=10)

    urlid = CharField(
        max_length=10,
        null=True)

    def results(self):
        # prefs = [ v.pref_list() for v in Voter.objects.filter(poll=self) ]
        prefs = [ v.pref_list() for v in self.voter_set.all() ]
        print prefs
        return [ sum(l) for l in zip(*prefs) ]

    @classmethod
    def make_urlid(klass):
        return ''.join(sample(_range,6))

    def __unicode__(self):
        return '%s: %s' % (self.urlid, self.question)

class Voter(Model):
    name = CharField(
        max_length=50,
        default='milou')
 
    prefs = CommaSeparatedIntegerField(
        max_length=50,
        default='8,2')

    def pref_list(self):
        return [int(p) for p in self.prefs.split(',')]

    comment = CharField(
        max_length=50,
        default='Romeo, O Romeo', 
        null=True)    

    is_admin = BooleanField(
        default=False)
     
    hashed_password = CharField(
        max_length=50, 
        null=True)

    poll = ForeignKey(Poll)

    def hash_password(self):
        self.hashed_password = hashlib.new(
            'sha1',self.hashed_password).hexdigest()

    def __unicode__(self):
        return self.name



