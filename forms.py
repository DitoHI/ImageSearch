from django import forms

class picForm(forms.Form):
    CHOICES = [('query/china.jpg' , 'China'),
               ('query/denmark.png', 'Denmark'),
               ('query/Indonesia.png', 'Indonesia'),
               ('query/united_states.png', 'United States')]
    name = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())