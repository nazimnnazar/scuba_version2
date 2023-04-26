from django.urls import path
from . import views
urlpatterns = [
    path('',views.membercount,name='membercount'),
    # Multiuser Form Path
    path('option1',views.option1,name='option1'),
    path('option2',views.option2,name='option2'),
    path('option3',views.option3,name='option3'),
    path('option4',views.option4,name='option4'),
    path('option5',views.option5,name='option5'),
    path('option6',views.option6,name='option6'),
    path('option7',views.option7,name='option7'),
    path('option8',views.option8,name='option8'),
    path('option9',views.option9,name='option9'),
    path('option10',views.option10,name='option10'),
    path('option11',views.option11,name='option11'),
    path('option12',views.option12,name='option12'),
    path('option13',views.option13,name='option13'),
    path('option14',views.option14,name='option14'),
    path('option15',views.option15,name='option15'),
    # End MUltiuser Path
]