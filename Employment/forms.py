from django import forms
from .models import Application, JobPost, Attachment


class JobForm(forms.ModelForm):
    due_date = forms.DateTimeField()
    class Meta:
        model = JobPost
        fields = ["job_title", "job_overview", 'qualifications', "due_date", ]

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['first_name', 'last_name',]

class AttachmentForm(forms.ModelForm):
    class Meta:
        model = Attachment
        fields = ['file',]