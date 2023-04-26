from django.urls import path
from . import views

urlpatterns = [
    # **************************AGATTI**************************
    path('agatti/',views.agatti,name ='agatti'),
    path('leader_details/<int:team_id>/',views.leader_details,name='leader_details'),
    path('download_agatti/<int:team_id>/<str:field_name>/', views.download_agatti, name='download_agatti'),
    path('team/<int:team_id>/member/<int:member_id>/download/<str:field_name>/', views.download_member_file_agatti, name='download_member_file_agatti'),
    path('statusagatti/<int:status_id>',views.statusagatti,name='statusagatti'),
    path('team/<int:team_id>/edit/', views.room_edit, name='room_edit'),
    path('permitagatti/<int:permit_id>/',views.permitagatti,name = 'permitagatti'),
    path('loginagatti',views.loginagatti,name='loginagatti'),
    path('logoutagatti',views.logoutagatti,name='logoutagatti'),
    #**************************END**************************

    #****************************KADMAT**************************
    path('kadmat/',views.kadmat,name='kadmat'),
    path('leader_details_kadmat/<int:team_id>/',views.leader_details_kadmat,name='leader_details_kadmat'),
    path('download_kadmat/<int:team_id>/<str:field_name>/', views.download_kadmat, name='download_kadmat'),
    path('team/<int:team_id>/member/<int:member_id>/download/<str:field_name>/', views.download_member_file_kadmat, name='download_member_file_kadmat'),
    path('statuskadmat/<int:status_id>',views.statuskadmat,name='statuskadmat'),
    path('kadmat_room_edit/<int:team_id>/', views.kadmat_room_edit, name='kadmat_room_edit'),    
    path('permitkadmat/<int:permit_id>/',views.permitkadmat,name = 'permitkadmat'),
    path('logoutkadmat',views.logoutkadmat,name='logoutkadmat'),
    path('loginkatmat',views.loginkatmat,name='loginkatmat'),
    #**************************END**************************

    # **************************** MINICOY **************************
    path('minicoy/',views.minicoy,name='minicoy'),
    path('leader_details_mincoy/<int:team_id>/',views.leader_details_mincoy,name='leader_details_mincoy'),
    path('download_minicoy/<int:team_id>/<str:field_name>/', views.download_minicoy, name='download_minicoy'),
    path('team/<int:team_id>/member/<int:member_id>/download/<str:field_name>/', views.download_member_file_minicoy, name='download_member_file_minicoy'),
    path('statusminicoy/<int:status_id>',views.statusminicoy,name='statusminicoy'),
    path('minicoy_room_edit/<int:team_id>/', views.minicoy_room_edit, name='minicoy_room_edit'),    
    path('permitminicoy/<int:permit_id>/',views.permitminicoy,name = 'permitminicoy'),
    path('logoutminicoy',views.logoutminicoy,name='logoutminicoy'),
    path('loginminicoy',views.loginminicoy,name='loginminicoy'),
    # **************************** END *******************************

    # **************************** KALPENI ******************************
    path('kalpeni',views.kalpeni,name='kalpeni'),
    path('leader_details_kalpeni/<int:team_id>/',views.leader_details_kalpeni,name='leader_details_kalpeni'),
    path('download_kalpeni/<int:team_id>/<str:field_name>/', views.download_kalpeni, name='download_kalpeni'),
    path('team/<int:team_id>/member/<int:member_id>/download/<str:field_name>/', views.download_member_file_kalpeni, name='download_member_file_kalpeni'),
    path('statuskalpeni/<int:status_id>',views.statuskalpeni,name='statuskalpeni'),
    path('kalpeni_room_edit/<int:team_id>/', views.kalpeni_room_edit, name='kalpeni_room_edit'),    
    path('permitkalpeni/<int:permit_id>/',views.permitkalpeni,name = 'permitkalpeni'),
    path('logoutkalpeni',views.logoutkalpeni,name='logoutkalpeni'),
    path('loginkalpeni',views.loginkalpeni,name='loginkalpeni'),
    # **************************** END **********************************
]
