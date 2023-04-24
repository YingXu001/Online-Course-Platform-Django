from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    click = forms.IntegerField(required=False)  # Add this line
    class Meta:
        model = Course
        fields = ['title', 'description', 'teacher', 'click', 'difficulty', 'comment']
        labels = {
            'title': 'Title',
            'description': 'Description',
            'teacher': 'Teacher',
            'click': 'Click',
            'difficulty': 'Difficulty',
            'comment': 'Comment',
        }

class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your comment here'}), required=True)


