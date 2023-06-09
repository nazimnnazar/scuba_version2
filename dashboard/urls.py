from django.urls import path
from . import views
urlpatterns = [
    path('dashboard',views.dashboard,name='dashboard'),
    path('leader_all_data',views.leader_all_data,name='leader_all_data'),
    path('leader_member/<int:team_id>/',views.leader_member,name='leader_member'),
    path('adminstatus/<int:pk>/',views.adminstatus,name='adminstatus'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),

    # path('team/<int:team_id>/edit/', views.team_edit, name='team_edit'),
    
    path('dashboard/download_file/<int:team_id>/<str:field_name>/', views.download_file, name='download_file'),
    path('team/<int:team_id>/member/<int:member_id>/download/<str:field_name>/', views.download_member_file, name='download_member_file'),
    path('search',views.search_leaders,name="search"),
    
    path('statusu/<int:status_id>',views.statusur,name='statusur'),
    path('permitkavarathi/<int:permit_id>/',views.permitkavarathi,name = 'permitkavarathi'),
    path('balance/<int:balance_id>/', views.input_balance, name='input_balance'),
    path('todo/<int:todo_id>/', views.todo, name='todo'),
    # path('adminpermit/<int:team_id>/',views.adminpermit,name='adminpermit'),
    path('invoice',views.invoice,name='invoice'),
    path('pdf_invoice',views.pdf_invoice,name='pdf_invoice'),

    path('room_c',views.room_c,name='room_c'),
    path('room_rdu',views.room_rdu,name='room_rdu'),
    path('room_delete/<int:id>/',views.room_delete,name='room_delete'),
    path('room_update/<int:id>/',views.room_update,name='room_update'),
    path('demo',views.demo,name='demo'),


    path('invoice_download/<str:pk>/',views.invoice_download,name='invoice_download'),
    path('invoice_delete/<int:id>/',views.invoice_delete,name='invoice_delete'),
]