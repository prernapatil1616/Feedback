# forms.py
from django import forms
from .models import FeedbackQuestion, FeedbackAnswer

class FeedbackForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        questions = FeedbackQuestion.objects.all()
        for question in questions:
            choices = [(answer.answer, answer.answer) for answer in question.feedbackanswer_set.all()]
            self.fields[question.question_text] = forms.ChoiceField(
                choices=choices,
                widget=forms.Select(attrs={'class': 'form-control'}),
            )
