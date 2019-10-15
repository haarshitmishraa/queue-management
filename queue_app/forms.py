from django import forms

class queueForm(forms.Form):
    CHOICES=(
        ('Accounts','Accounts'),
        ('Loans','Loans'),
        ('Internet Banking','Internet Banking'),
        ('Mobile Banking','Mobile Banking'),
    )
    select = forms.CharField(widget=forms.Select(choices=CHOICES,attrs={
    'class':'input100'}))

    phone = forms.CharField(max_length=20,
        widget= forms.TextInput(attrs={
            'class': 'input100'
        }))
