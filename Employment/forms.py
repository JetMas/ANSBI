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
        fields = ['first_name', 'last_name', 'application', 'resume', 'letter_of_interest', 'transcript', 'certificate_or_license', 'certificate_of_indian_blood',]

class AttachmentForm(forms.ModelForm):
    class Meta:
        model = Attachment
        fields = ['file',]