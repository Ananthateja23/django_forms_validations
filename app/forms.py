from django import forms

class StudentForm(forms.Form):
    g=[('MALE','male'),('FEMALE','female')]
    c=[['PYTHON','python'],('SQL','sql')]
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    email=forms.EmailField()
    date=forms.DateField()
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    address=forms.CharField(max_length=300,widget=forms.Textarea(attrs={'cols':5,'rows':3}))
    gender=forms.ChoiceField(choices=g)
    gend=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    course=forms.MultipleChoiceField(choices=c)
    cour=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)