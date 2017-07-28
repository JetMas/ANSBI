from django.db import models
from django.utils import timezone
from . import validators
# Create your models here.

class GuideLine(models.Model):
    name = models.CharField(max_length=300)
    file = models.FileField(upload_to='./guidelines/')
    date = models.DateField(default=None)

class JobPost(models.Model):
    job_title = models.CharField(max_length=300)
    job_overview = models.TextField(default='')
    qualifications = models.TextField(default='')
    job_PD = models.FileField(upload_to='./job_pd', blank=True)
    post_date = models.DateField('post date')
    due_date = models.DateField('due date')

class Application(models.Model):
    first_name = models.CharField('*First Name', max_length=200)
    last_name = models.CharField('*Last Name', max_length=200)

    application = models.FileField('*Application', upload_to='./applications/', blank=False, validators=[validators.validate_file_extension])
    resume = models.FileField('*Resume', upload_to='./resumes/', blank=False, validators=[validators.validate_file_extension])
    letter_of_interest = models.FileField('*Letter of Interest for the position',upload_to='./letter_of_interest/', blank=False, validators=[validators.validate_file_extension])    
    transcript = models.FileField('Official College Transcripts, official transcripts must be submitted upon employment',upload_to='./transcripts/', blank=True, validators=[validators.validate_file_extension])
    certificate_or_license = models.FileField('Certificate or License applicable to the position',upload_to='./certificates_or_licenses', blank=True, validators=[validators.validate_file_extension])
    certificate_of_indian_blood = models.FileField('Certificate of Indian Blood, required if you are claiming Indian preference', upload_to='./certificate_of_indian_blood', blank=True, validators=[validators.validate_file_extension])

    '''
    certificate_of_indian_blood = models.FileField(upload_to='./certificate_of_indian_blood/', blank=True, validators=[validators.validate_file_extension])
    first_letter_of_recommendation = models.FileField(upload_to='./first_letter_of_recommendation/', blank=True, validators=[validators.validate_file_extension])
    second_letter_of_recommendation = models.FileField(upload_to='./second_letter_of_recommendation/', blank=True, validators=[validators.validate_file_extension])
    third_letter_of_recommendation = models.FileField(upload_to='./third_letter_of_recommendation/', blank=True, validators=[validators.validate_file_extension])
    personal_growth = models.FileField('Personal Growth (Teachers Only)',upload_to='./personal_growth/', blank=True, validators=[validators.validate_file_extension])
    certificate_of_completion = models.FileField('Certificate of Completion - 16 hours Employable Skills Training (if no college degree)',upload_to='./certificate_of_completion', blank=True, validators=[validators.validate_file_extension])
    '''

    apply_date = models.DateField('apply date')

class Attachment(models.Model):
    link = models.ForeignKey(Application, on_delete=models.CASCADE)
    file = models.FileField(upload_to='./attachments/', validators=[validators.validate_file_extension])