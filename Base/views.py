from django.shortcuts import render, render_to_response

# Create your views here.

def home(request):
    return render_to_response("Base/Home.html")


def aboutUs(request):
    return render_to_response("Base/AboutUs.html")

def contactUs(request):
    return render_to_response("Base/ContactUs.html")


def administration(request):
    return render_to_response("Base/Administration/Administration.html")

def administration_facilities(request):
    return render_to_response("Base/Administration/Administration_Facilities.html")

def administration_forestry(request):
    return render_to_response("Base/Administration/Administration_Forestry.html")

def administration_kabr(request):
    return render_to_response("Base/Administration/Administration_KABR.html")

def administration_waterdept(request):
    return render_to_response("Base/Administration/Administration_WaterDept.html")


def communityServices(request):
    return render_to_response("Base/CommunityServices/CommunityServices.html")

def communityServices_FinancialAid(request):
    return render_to_response("Base/CommunityServices/CommunityServices_FinancialAid.html")

def communityServices_Programs(request):
    return render_to_response("Base/CommunityServices/CommunityServices_Programs.html")


def earlyChildhood(request):
    return render_to_response("Base/EarlyChildhood/EarlyChildhood.html")

def earlyChildhood_FAQ(request):
    return render_to_response("Base/EarlyChildhood/EarlyChildhood_FAQ.html")

def earlyChildhood_Governance(request):
    return render_to_response("Base/EarlyChildhood/EarlyChildhood_Governance.html")

def earlyChildhood_Programs(request):
    return render_to_response("Base/EarlyChildhood/EarlyChildhood_Programs.html")


def healthServices(request):
    return render_to_response("Base/HealthServices/HealthServices.html")

def healthServices_Dental(request):
    return render_to_response("Base/HealthServices/HealthServices_Dental.html")

def healthServices_EMS(request):
    return render_to_response("Base/HealthServices/HealthServices_EMS.html")

def healthServices_Lab(request):
    return render_to_response("Base/HealthServices/HealthServices_Lab.html")

def healthServices_Pharmacy(request):
    return render_to_response("Base/HealthServices/HealthServices_Pharmacy.html")

def healthServices_Services(request):
    return render_to_response("Base/HealthServices/HealthServices_Services.html")


def school(request):
    return render_to_response("Base/School/School.html")

def school_Elementary(request):
    return render_to_response("Base/School/School_Elementary.html")

def school_Middle(request):
    return render_to_response("Base/School/School_Middle.html")

def school_High(request):
    return render_to_response("Base/School/School_High.html")

def wellness(request):
    return render_to_response("Base/Wellness/Wellness.html")