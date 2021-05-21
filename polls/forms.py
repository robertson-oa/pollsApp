from django import forms
from .models import Question

class ChoiceForm(forms.Form):
    question = forms.CharField(max_length = 100) #"Type in any question you want")
    choice_text = forms.CharField(max_length=100) #, default = "Provide some description here")
    

class QuestionForm(forms.ModelForm):
    
    class Meta:
        model = Question
        fields = "__all__"
        #exclude = ['slug']

class CreateQuestionForm(forms.ModelForm):
    
    class Meta:
        model = Question
        exclude = ['slug']