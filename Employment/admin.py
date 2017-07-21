from django.contrib import admin
from . import models
# Register your models here.

class JobPostAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'post_date', 'due_date')
    list_filter = ['post_date', 'due_date',]
    search_fields = ['job_title']
    fieldsets = [
        (None, {'fields' : ['job_title']}),
        ('Job Information', {'fields' : ['job_overview', 'qualifications', 'job_PD']}),
        ('Date Information', {'fields': ['post_date', 'due_date']}),
    ]


class AttachmentInline(admin.TabularInline):
    model = models.Attachment
    extra = 3

class ApplicationAdmin(admin.ModelAdmin):
    inlines = [AttachmentInline]
    list_display = ('last_name', 'first_name', 'apply_date',)
    list_filter = ['apply_date',]
    search_fields = ['first_name', 'last_name',]

    # def application_link (self, obj):
    #     if obj.application:
    #         return "<a href='%s' download>Download</a>" % (obj.application.url,)
    #     else:
    #         return "No attachment"
    # application_link.allow_tags = True
    # application_link.allow_tags = True
    # application_link.short_description = 'File Download'

class GuideLineAdmin(admin.ModelAdmin):
    list_display = ('name', 'date',)
    list_filter = ['date',]
    search_fields = ['name',]

admin.site.register(models.JobPost, JobPostAdmin)
admin.site.register(models.Application, ApplicationAdmin)
admin.site.register(models.GuideLine, GuideLineAdmin)