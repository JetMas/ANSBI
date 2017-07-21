from django.conf.urls import url
from . import views

app_name = "Base"
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^aboutus/$',views.aboutUs, name='aboutus'),
    url(r'^contactus/$', views.contactUs, name='contactus'),
    url(r'^administration/$', views.administration, name='administration'),
    url(r'^administration/facilities/$', views.administration_facilities, name='facilities'),
    url(r'^administration/forestry/$', views.administration_forestry, name='forestry'),
    url(r'^administration/kabr/$', views.administration_kabr, name='kabr'),
    url(r'^administration/waterdept/$', views.administration_waterdept, name='waterdept'),
    url(r'^communityservices/$', views.communityServices, name='communityServices'),
    url(r'^communityservices/financialaid/$', views.communityServices_FinancialAid, name='financialAid'),
    url(r'^communityservices/programs/$', views.communityServices_Programs, name='communityServicesPrograms'),
    url(r'^earlychildhood/$', views.earlyChildhood, name='earlychildhood'),
    url(r'^earlychildhood/faq/$', views.earlyChildhood_FAQ, name='earlychildhood_faq'),
    url(r'^earlychildhood/governance/$', views.earlyChildhood_Governance, name='earlychildhood_governance'),
    url(r'^earlychildhood/programs/$', views.earlyChildhood_Programs, name='earlychildhood_programs'),
    url(r'^healthservices/$', views.healthServices, name='healthservices'),
    url(r'^healthservices/dental/$', views.healthServices_Dental, name='healthservices_dental'),
    url(r'^healthservices/ems/$', views.healthServices_EMS, name='healthservices_ems'),
    url(r'^healthservices/lab/$', views.healthServices_Lab, name='healthservices_lab'),
    url(r'^healthservices/pharmacy/$', views.healthServices_Pharmacy, name='healthservices_pharmacy'),
    url(r'^healthservices/services/$', views.healthServices_Services, name='healthservices_services'),
    url(r'^school/$', views.school, name='school'),
    url(r'^school/elementary/$', views.school_Elementary, name='school_elementary'),
    url(r'^school/middle/$', views.school_Middle, name='school_middle'),
    url(r'^school/high/$', views.school_High, name='school_high'),
    url(r'^wellness/$', views.wellness, name='wellness'),
]