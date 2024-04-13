from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin

from admins import views
admin.site.site_header = 'Sahachari Portal'
admin.site.index_title = 'Sahachari Kannur'
admin.site.site_title = 'Sahachari Kannur'

urlpatterns = [
    path('',include('django.contrib.auth.urls')),
    path('Dashboard/',views.adminpage, name='dashboard'),
    path('Dashboard/approv', views.approvd, name='approved'),
    path('Dashboard/refresh', views.refresh, name='refresh'),
    path('Dashboard/Pending', views.allpend, name='allpend'),
    path('Dashboard/view', views.viewedit, name='view'),
    path('Dashboard/<int:data_id>/', views.portdel, name='del'),
    path('Dashboard/medreset/<int:data_id>/', views.portreset, name='reset'),

    path('',views.home),
    path('delete/<int:mem_id>/', views.delete, name='delete'),
    path('update/<int:data_id>/',views.uapprove,name='uapprove'),
    path('reject/<int:data_id>/', views.ureject, name='ureject'),
    path('Dashboard/Unit',views.addunit, name='addunit'),
    path('Dashboard/Cluster',views.addcluster, name='addcluster'),
    path('Dashboard/Zone',views.addzone, name='addzone'),
    path('Dashboard/Centre',views.addcentre, name='addcentre'),
    path('Dashboard/MedicalShop', views.addmedshop, name='addmedshop'),
    path('Dashboard/Allocate/<int:data_id>/',views.allocate, name='allocate'),
    path('Dashboard/Relation/<int:data_id>/',views.unitrel, name='unitrel'),
    path('Dashboard/Medicine/Apply',views.unitmed, name='unitmed'),
    path('Dashboard/Medicine/View',views.unitmedapp, name='unitmedapp'),
    path('Dashboard/Medicine/Views', views.medview, name='distmedview'),
    path('Dashboard/Medicine/Reject/<int:data_id>/', views.medrej, name='medrej'),
    path('Dashboard/Medicine/Allocate/<int:data_id>/',views.medapprove, name='medallocate'),
    path('Dashboard/Medicine/Approve', views.medapprov, name='medapprove'),
    path('Dashboard/Medicine/Add', views.meddone, name='meddone'),
    path('Dashboard/Report', views.dylrep, name='dylrep'),
    path('Dashboard/Reports/<int:data_id>/', views.dylcentrerep, name='dylcentrerep'),
    path('Dashboard/Report/Patient/', views.dylpat, name='dylpat'),
    path('Dashboard/Otp/<int:data_id>/', views.otpcheck, name='otpcheck'),
    path('val', views.home),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
