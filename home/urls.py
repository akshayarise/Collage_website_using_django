from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("index", views.index, name='index'),
    path("aboutus", views.aboutus, name='aboutus'),
    path("chairmanmessage", views.chairmanmessage, name='chairmanmessage'),
    path("secreterymessage", views.secreterymessage, name='secreterymessage'),
    path("directormessage", views.directormessage, name='directormessage'),
    path("orgenizationchar", views.orgenizationchar, name='orgenizationchar'),
    path("aicteapproval", views.aicteapproval, name='aicteapproval'),
    path("affiliation", views.affiliation, name='affiliation'),
    path("achivement", views.achivement, name='achivement'),
    path("program", views.program, name='program'),
    path("btech", views.btech, name='btech'),
    path("polytechnic", views.polytechnic, name='polytechnic'),
    path("department", views.department, name='department'),
    path("ash", views.ash, name='ash'),
    path("cseit", views.cseit, name='cseit'),
    path("me", views.me, name='me'),
    path("ce", views.ce, name='ce'),
    path("ece", views.ece, name='ece'),
    path("eee", views.eee, name='eee'),
    path("dp", views.dp, name='dp'),
    path("admission", views.admission, name='admission'),
    path("facility", views.facility, name='facility'),
    path("wifi", views.wifi, name='wifi'),
    path("library", views.library, name='library'),
    path("computercenter", views.computercenter, name='computercenter'),
    path("communicationlab", views.communicationlab, name='communicationlab'),
    path("hostals", views.hostals, name='hostals'),
    path("sports", views.sports, name='sports'),
    path("gausthouse", views.gausthouse, name='gausthouse'),
    path("fee", views.fee, name='fee'),
    path("contectus", views.contectus, name='contectus'),
    path("careerideal", views.careerideal, name='careerideal'),
    path("photogallery", views.photogallery, name='photogallery'),
    path("lifeideal", views.lifeideal, name='lifeideal')
    # path("", views., name='')

    

    
    

]