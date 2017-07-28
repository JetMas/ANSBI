from django.shortcuts import get_object_or_404, render, HttpResponse, HttpResponseRedirect
from . import models
from .forms import AttachmentForm, ApplicationForm
from django.core.mail import send_mail
from django.utils import timezone
from django.forms.formsets import formset_factory
# Create your views here.

def index(request):
    jobPost = models.JobPost.objects.all().order_by("post_date")
    context = {'jobPost' : jobPost}
    return render(request, 'Employment/Index.html', context)

def detail(request, job_id):
    job = get_object_or_404(models.JobPost, pk=job_id)
    return render(request, 'Employment/Detail.html', {'job' : job})


def apply(request):
    applied = False
    guideLines = models.GuideLine.objects.all().order_by('date')
    AttachmentFormset = formset_factory(AttachmentForm)
    if request.method == 'POST':
        applicationForm = ApplicationForm(request.POST, request.FILES)
        attachment_formset = AttachmentFormset(request.POST, request.FILES)
        if applicationForm.is_valid() and attachment_formset.is_valid():
            application = applicationForm.save(commit=False)
            application.apply_date = timezone.now()
            application.save()
            for forms in attachment_formset:
                attachment = forms.save(commit=False)
                if attachment.file:
                    attachment.link = application
                    attachment.save()
            applied = True
    else:
        applicationForm = ApplicationForm()
        attachment_formset = AttachmentFormset()
    context = {'guideLines':guideLines, 'form':applicationForm, 'attachment_formset':attachment_formset, 'applied':applied}
    return render(request, 'Employment/Apply.html', context=context)

'''
def createJobPost(request):
    posted = False
    valid = True
    if request.method == 'POST':
        jobForm = forms.JobForm(data=request.POST)
        if jobForm.is_valid():
            job = jobForm.save(commit=False)
            job.post_date = timezone.now()
            job.save()
            posted = True
        else:
            valid = False
    else:
        jobForm = forms.JobForm()
    context = {'form':jobForm, 'posted':posted, 'valid':valid}
    return render(request, 'Employment/PostJob.html', context=context)
'''