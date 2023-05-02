from django.contrib import messages
from django.shortcuts import render, redirect , get_list_or_404
from . models import Team, TeamMember
from django.http import HttpResponse
# form page count pages 
def membercount(request):
    if request.method == 'POST':
        applicant_count = request.POST.get('applicant-count')
        if applicant_count == 'option1':
            messages.success(request,'You Are Selected 1')
            return redirect('option1')
        elif applicant_count == 'option2':
            messages.success(request,'You Are Selected 2')
            return redirect('option2')
        elif applicant_count == 'option3':
            messages.success(request,'You Are Selected 3')
            return redirect('option3')
        elif applicant_count == 'option4':
            messages.success(request,'You Are Selected 4')
            return redirect('option4')
        elif applicant_count == 'option5':
            messages.success(request,'You Are Selected 5')
            return redirect('option5')
        elif applicant_count == 'option6':
            messages.success(request,'You Are Selected 6')
            return redirect('option6')
        elif applicant_count == 'option7':
            messages.success(request,'You Are Selected 7')
            return redirect('option7')
        elif applicant_count == 'option8':
            messages.success(request,'You Are Selected 8')
            return redirect('option8')
        elif applicant_count == 'option9':
            messages.success(request,'You Are Selected 9')
            return redirect('option9')
        elif applicant_count == 'option10':
            messages.success(request,'You Are Selected 10')            
            return redirect('option10')
        elif applicant_count == 'option11':
            messages.success(request,'You Are Selected 11')            
            return redirect('option11')
        elif applicant_count == 'option12':
            messages.success(request,'You Are Selected 12')
            return redirect('option12')
        elif applicant_count == 'option13':
            messages.success(request,'You Are Selected 13')            
            return redirect('option13')
        elif applicant_count == 'option14':
            messages.success(request,'You Are Selected 14')            
            return redirect('option14')
        elif applicant_count == 'option15':
            messages.success(request,'You Are Selected 15')            
            return redirect('option15')
    return render(request,'index.html')
# ENd form

# Multi page function
# def option1(request):
#     if request.method == 'POST':
#         if 'submit' in request.POST:
#             package_str = ", ".join(request.POST.getlist('package'))
#             team = Team.objects.create(
#                 island = request.POST['island'],
#                 leader_name = request.POST['leader_name'],
#                 leader_father_name = request.POST['leader_father_name'],
#                 leader_contact_number=request.POST['leader_contact_number'],
#                 leader_date_of_birth=request.POST['leader_date_of_birth'],
#                 leader_email=request.POST['leader_email'],
#                 leader_address=request.POST['leader_address'],
#                 leader_emergency_contact_person= request.POST['leader_emergency_contact_person'],
#                 leader_emergency_contact_number=request.POST['leader_emergency_contact_number'],
#                 leader_photo=request.FILES['leader_photo'],
#                 leader_id_adhaar = request.FILES['leader_id_adhaar'],
#                 leader_id_PCC = request.FILES['leader_id_PCC'],
#                 package = request.POST['package'],
#                 checkin=request.POST['checkin'],        
#                 checkout=request.POST['checkout'],
#                 number_of_rooms=request.POST['number_of_rooms'],
#                 ac_or_nonac=request.POST['ac_or_nonac'],
#                 veg_or_nonveg=request.POST['veg_or_nonveg'],    
#                 package=package_str        
#                 )
#             messages.success(request,'Your Data Successfully Saved')
#             return redirect('/')
#     else:
#         package_choices = Team.PACKAGE
#         return render(request, 'option1.html',{'package_choices': package_choices})
def option1(request):
    if request.method == 'POST':
        if 'submit' in request.POST:
            package_str = ", ".join(request.POST.getlist('package'))
            team = Team.objects.create(
                island = request.POST['island'],
                leader_name = request.POST['leader_name'],
                leader_father_name = request.POST['leader_father_name'],
                leader_contact_number=request.POST['leader_contact_number'],
                leader_date_of_birth=request.POST['leader_date_of_birth'],
                leader_email=request.POST['leader_email'],
                leader_address=request.POST['leader_address'],
                leader_emergency_contact_person= request.POST['leader_emergency_contact_person'],
                leader_emergency_contact_number=request.POST['leader_emergency_contact_number'],
                leader_photo=request.FILES['leader_photo'],
                leader_id_adhaar = request.FILES['leader_id_adhaar'],
                leader_id_PCC = request.FILES['leader_id_PCC'],
                checkin=request.POST['checkin'],        
                checkout=request.POST['checkout'],
                number_of_rooms=request.POST['number_of_rooms'],
                ac_or_nonac=request.POST['ac_or_nonac'],
                veg_or_nonveg=request.POST['veg_or_nonveg'],    
                package=package_str        
            )
            messages.success(request,'Registered Successfully')
            return redirect('/')
    else:
        package_choices = Team.PACKAGE
        return render(request, 'option1.html',{'package_choices': package_choices})

# --------------------------------First Member Page----------------------------
def option2(request):
    if request.method == 'POST':
        if 'submit' in request.POST:
            package_str = ", ".join(request.POST.getlist('package'))
            team = Team.objects.create(
                island = request.POST['island'],
                leader_name = request.POST['leader_name'],
                leader_father_name = request.POST['leader_father_name'],
                leader_contact_number=request.POST['leader_contact_number'],
                leader_date_of_birth=request.POST['leader_date_of_birth'],
                leader_email=request.POST['leader_email'],
                leader_address=request.POST['leader_address'],
                leader_emergency_contact_person= request.POST['leader_emergency_contact_person'],
                leader_emergency_contact_number=request.POST['leader_emergency_contact_number'],
                leader_photo=request.FILES['leader_photo'],
                leader_id_adhaar = request.FILES['leader_id_adhaar'],
                leader_id_PCC = request.FILES['leader_id_PCC'],
                checkin=request.POST['checkin'],        
                checkout=request.POST['checkout'],
                number_of_rooms=request.POST['number_of_rooms'],
                ac_or_nonac=request.POST['ac_or_nonac'],
                veg_or_nonveg=request.POST['veg_or_nonveg'],    
                package=package_str        
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member_name'],
                father_name=request.POST['member_father_name'],
                date_of_birth=request.POST['member_date_of_birth'],
                email=request.POST['member_email'],
                contact_number=request.POST['member_contact_number'],
                address=request.POST['member_address'],
                emergency_contact_person=request.POST['member_emergency_contact_person'],
                emergency_contact_number=request.POST['member_emergency_contact_number'],
                photo=request.FILES['member_photo'],
                id_proof=request.FILES['member_id_proof'],
                id_proof_again=request.FILES['member_id_proof_again']
            )
            messages.success(request,'Registered Successfully')
            return redirect('/')
    else:
        package_choices = Team.PACKAGE
        return render(request, 'option2.html',{'package_choices': package_choices})
# --------------------------------End Page Second------------------------------

# --------------------------------Second Member--------------------------------
def option3(request):
    if request.method == 'POST':
        if 'submit' in request.POST:
            package_str = ", ".join(request.POST.getlist('package'))
            team = Team.objects.create(
                island = request.POST['island'],
                leader_name = request.POST['leader_name'],
                leader_father_name = request.POST['leader_father_name'],
                leader_contact_number=request.POST['leader_contact_number'],
                leader_date_of_birth=request.POST['leader_date_of_birth'],
                leader_email=request.POST['leader_email'],
                leader_address=request.POST['leader_address'],
                leader_emergency_contact_person= request.POST['leader_emergency_contact_person'],
                leader_emergency_contact_number=request.POST['leader_emergency_contact_number'],
                leader_photo=request.FILES['leader_photo'],
                leader_id_adhaar = request.FILES['leader_id_adhaar'],
                leader_id_PCC = request.FILES['leader_id_PCC'],
                checkin=request.POST['checkin'],        
                checkout=request.POST['checkout'],
                number_of_rooms=request.POST['number_of_rooms'],
                ac_or_nonac=request.POST['ac_or_nonac'],
                veg_or_nonveg=request.POST['veg_or_nonveg'],    
                package=package_str        
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member_name'],
                father_name=request.POST['member_father_name'],
                date_of_birth=request.POST['member_date_of_birth'],
                email=request.POST['member_email'],
                contact_number=request.POST['member_contact_number'],
                address=request.POST['member_address'],
                emergency_contact_person=request.POST['member_emergency_contact_person'],
                emergency_contact_number=request.POST['member_emergency_contact_number'],
                photo=request.FILES['member_photo'],
                id_proof=request.FILES['member_id_proof'],
                id_proof_again=request.FILES['member_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member2_name'],
                father_name=request.POST['member2_father_name'],
                date_of_birth=request.POST['member2_date_of_birth'],
                email=request.POST['member2_email'],
                contact_number=request.POST['member2_contact_number'],
                address=request.POST['member2_address'],
                emergency_contact_person=request.POST['member2_emergency_contact_person'],
                emergency_contact_number=request.POST['member2_emergency_contact_number'],
                photo=request.FILES['member2_photo'],
                id_proof=request.FILES['member2_id_proof'],
                id_proof_again=request.FILES['member2_id_proof_again']
            )
            messages.success(request,'Registered Successfully')
            return redirect('/')
    else:
        package_choices = Team.PACKAGE
        return render(request, 'option3.html',{'package_choices': package_choices})
# --------------------------------End Second Member----------------------------

# --------------------------------thered Member--------------------------------
def option4(request):
    if request.method == 'POST':
        if 'submit' in request.POST:
            package_str = ", ".join(request.POST.getlist('package'))
            team = Team.objects.create(
                island = request.POST['island'],
                leader_name = request.POST['leader_name'],
                leader_father_name = request.POST['leader_father_name'],
                leader_contact_number=request.POST['leader_contact_number'],
                leader_date_of_birth=request.POST['leader_date_of_birth'],
                leader_email=request.POST['leader_email'],
                leader_address=request.POST['leader_address'],
                leader_emergency_contact_person= request.POST['leader_emergency_contact_person'],
                leader_emergency_contact_number=request.POST['leader_emergency_contact_number'],
                leader_photo=request.FILES['leader_photo'],
                leader_id_adhaar = request.FILES['leader_id_adhaar'],
                leader_id_PCC = request.FILES['leader_id_PCC'],
                checkin=request.POST['checkin'],        
                checkout=request.POST['checkout'],
                number_of_rooms=request.POST['number_of_rooms'],
                ac_or_nonac=request.POST['ac_or_nonac'],
                veg_or_nonveg=request.POST['veg_or_nonveg'],    
                package=package_str        
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member_name'],
                father_name=request.POST['member_father_name'],
                date_of_birth=request.POST['member_date_of_birth'],
                email=request.POST['member_email'],
                contact_number=request.POST['member_contact_number'],
                address=request.POST['member_address'],
                emergency_contact_person=request.POST['member_emergency_contact_person'],
                emergency_contact_number=request.POST['member_emergency_contact_number'],
                photo=request.FILES['member_photo'],
                id_proof=request.FILES['member_id_proof'],
                id_proof_again=request.FILES['member_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member2_name'],
                father_name=request.POST['member2_father_name'],
                date_of_birth=request.POST['member2_date_of_birth'],
                email=request.POST['member2_email'],
                contact_number=request.POST['member2_contact_number'],
                address=request.POST['member2_address'],
                emergency_contact_person=request.POST['member2_emergency_contact_person'],
                emergency_contact_number=request.POST['member2_emergency_contact_number'],
                photo=request.FILES['member2_photo'],
                id_proof=request.FILES['member2_id_proof'],
                id_proof_again=request.FILES['member2_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member3_name'],
                father_name=request.POST['member3_father_name'],
                date_of_birth=request.POST['member3_date_of_birth'],
                email=request.POST['member3_email'],
                contact_number=request.POST['member3_contact_number'],
                address=request.POST['member2_address'],
                emergency_contact_person=request.POST['member3_emergency_contact_person'],
                emergency_contact_number=request.POST['member3_emergency_contact_number'],
                photo=request.FILES['member3_photo'],
                id_proof=request.FILES['member3_id_proof'],
                id_proof_again=request.FILES['member3_id_proof_again']
            )
            messages.success(request,'Registered Successfully')
            return redirect('/')
    else:
        package_choices = Team.PACKAGE
        return render(request, 'option4.html',{'package_choices': package_choices})
# --------------------------------End Second Member----------------------------

def option5(request):
    if request.method == 'POST':
        if 'submit' in request.POST:
            package_str = ", ".join(request.POST.getlist('package'))
            team = Team.objects.create(
                island = request.POST['island'],
                leader_name = request.POST['leader_name'],
                leader_father_name = request.POST['leader_father_name'],
                leader_contact_number=request.POST['leader_contact_number'],
                leader_date_of_birth=request.POST['leader_date_of_birth'],
                leader_email=request.POST['leader_email'],
                leader_address=request.POST['leader_address'],
                leader_emergency_contact_person= request.POST['leader_emergency_contact_person'],
                leader_emergency_contact_number=request.POST['leader_emergency_contact_number'],
                leader_photo=request.FILES['leader_photo'],
                leader_id_adhaar = request.FILES['leader_id_adhaar'],
                leader_id_PCC = request.FILES['leader_id_PCC'],
                checkin=request.POST['checkin'],        
                checkout=request.POST['checkout'],
                number_of_rooms=request.POST['number_of_rooms'],
                ac_or_nonac=request.POST['ac_or_nonac'],
                veg_or_nonveg=request.POST['veg_or_nonveg'],    
                package=package_str        
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member_name'],
                father_name=request.POST['member_father_name'],
                date_of_birth=request.POST['member_date_of_birth'],
                email=request.POST['member_email'],
                contact_number=request.POST['member_contact_number'],
                address=request.POST['member_address'],
                emergency_contact_person=request.POST['member_emergency_contact_person'],
                emergency_contact_number=request.POST['member_emergency_contact_number'],
                photo=request.FILES['member_photo'],
                id_proof=request.FILES['member_id_proof'],
                id_proof_again=request.FILES['member_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member2_name'],
                father_name=request.POST['member2_father_name'],
                date_of_birth=request.POST['member2_date_of_birth'],
                email=request.POST['member2_email'],
                contact_number=request.POST['member2_contact_number'],
                address=request.POST['member2_address'],
                emergency_contact_person=request.POST['member2_emergency_contact_person'],
                emergency_contact_number=request.POST['member2_emergency_contact_number'],
                photo=request.FILES['member2_photo'],
                id_proof=request.FILES['member2_id_proof'],
                id_proof_again=request.FILES['member2_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member3_name'],
                father_name=request.POST['member3_father_name'],
                date_of_birth=request.POST['member3_date_of_birth'],
                email=request.POST['member3_email'],
                contact_number=request.POST['member3_contact_number'],
                address=request.POST['member2_address'],
                emergency_contact_person=request.POST['member3_emergency_contact_person'],
                emergency_contact_number=request.POST['member3_emergency_contact_number'],
                photo=request.FILES['member3_photo'],
                id_proof=request.FILES['member3_id_proof'],
                id_proof_again=request.FILES['member3_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member4_name'],
                father_name=request.POST['member4_father_name'],
                date_of_birth=request.POST['member4_date_of_birth'],
                email=request.POST['member4_email'],
                contact_number=request.POST['member4_contact_number'],
                address=request.POST['member4_address'],
                emergency_contact_person=request.POST['member4_emergency_contact_person'],
                emergency_contact_number=request.POST['member4_emergency_contact_number'],
                photo=request.FILES['member4_photo'],
                id_proof=request.FILES['member4_id_proof'],
                id_proof_again=request.FILES['member4_id_proof_again']
            )
            messages.success(request,'Registered Successfully')
            return redirect('/')
    else:
        package_choices = Team.PACKAGE
        return render(request, 'option5.html',{'package_choices': package_choices})

def option6(request):
    if request.method == 'POST':
        if 'submit' in request.POST:
            package_str = ", ".join(request.POST.getlist('package'))
            team = Team.objects.create(
                island = request.POST['island'],
                leader_name = request.POST['leader_name'],
                leader_father_name = request.POST['leader_father_name'],
                leader_contact_number=request.POST['leader_contact_number'],
                leader_date_of_birth=request.POST['leader_date_of_birth'],
                leader_email=request.POST['leader_email'],
                leader_address=request.POST['leader_address'],
                leader_emergency_contact_person= request.POST['leader_emergency_contact_person'],
                leader_emergency_contact_number=request.POST['leader_emergency_contact_number'],
                leader_photo=request.FILES['leader_photo'],
                leader_id_adhaar = request.FILES['leader_id_adhaar'],
                leader_id_PCC = request.FILES['leader_id_PCC'],
                checkin=request.POST['checkin'],        
                checkout=request.POST['checkout'],
                number_of_rooms=request.POST['number_of_rooms'],
                ac_or_nonac=request.POST['ac_or_nonac'],
                veg_or_nonveg=request.POST['veg_or_nonveg'],    
                package=package_str        
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member_name'],
                father_name=request.POST['member_father_name'],
                date_of_birth=request.POST['member_date_of_birth'],
                email=request.POST['member_email'],
                contact_number=request.POST['member_contact_number'],
                address=request.POST['member_address'],
                emergency_contact_person=request.POST['member_emergency_contact_person'],
                emergency_contact_number=request.POST['member_emergency_contact_number'],
                photo=request.FILES['member_photo'],
                id_proof=request.FILES['member_id_proof'],
                id_proof_again=request.FILES['member_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member2_name'],
                father_name=request.POST['member2_father_name'],
                date_of_birth=request.POST['member2_date_of_birth'],
                email=request.POST['member2_email'],
                contact_number=request.POST['member2_contact_number'],
                address=request.POST['member2_address'],
                emergency_contact_person=request.POST['member2_emergency_contact_person'],
                emergency_contact_number=request.POST['member2_emergency_contact_number'],
                photo=request.FILES['member2_photo'],
                id_proof=request.FILES['member2_id_proof'],
                id_proof_again=request.FILES['member2_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member3_name'],
                father_name=request.POST['member3_father_name'],
                date_of_birth=request.POST['member3_date_of_birth'],
                email=request.POST['member3_email'],
                contact_number=request.POST['member3_contact_number'],
                address=request.POST['member2_address'],
                emergency_contact_person=request.POST['member3_emergency_contact_person'],
                emergency_contact_number=request.POST['member3_emergency_contact_number'],
                photo=request.FILES['member3_photo'],
                id_proof=request.FILES['member3_id_proof'],
                id_proof_again=request.FILES['member3_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member4_name'],
                father_name=request.POST['member4_father_name'],
                date_of_birth=request.POST['member4_date_of_birth'],
                email=request.POST['member4_email'],
                contact_number=request.POST['member4_contact_number'],
                address=request.POST['member4_address'],
                emergency_contact_person=request.POST['member4_emergency_contact_person'],
                emergency_contact_number=request.POST['member4_emergency_contact_number'],
                photo=request.FILES['member4_photo'],
                id_proof=request.FILES['member4_id_proof'],
                id_proof_again=request.FILES['member4_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member5_name'],
                father_name=request.POST['member5_father_name'],
                date_of_birth=request.POST['member5_date_of_birth'],
                email=request.POST['member5_email'],
                contact_number=request.POST['member5_contact_number'],
                address=request.POST['member5_address'],
                emergency_contact_person=request.POST['member5_emergency_contact_person'],
                emergency_contact_number=request.POST['member5_emergency_contact_number'],
                photo=request.FILES['member5_photo'],
                id_proof=request.FILES['member5_id_proof'],
                id_proof_again=request.FILES['member5_id_proof_again']
            )
            messages.success(request,'Registered Successfully')
            return redirect('/')
    else:
        package_choices = Team.PACKAGE
        return render(request, 'option6.html',{'package_choices': package_choices})
 
def option7(request):
    if request.method == 'POST':
        if 'submit' in request.POST:
            package_str = ", ".join(request.POST.getlist('package'))
            team = Team.objects.create(
                island = request.POST['island'],
                leader_name = request.POST['leader_name'],
                leader_father_name = request.POST['leader_father_name'],
                leader_contact_number=request.POST['leader_contact_number'],
                leader_date_of_birth=request.POST['leader_date_of_birth'],
                leader_email=request.POST['leader_email'],
                leader_address=request.POST['leader_address'],
                leader_emergency_contact_person= request.POST['leader_emergency_contact_person'],
                leader_emergency_contact_number=request.POST['leader_emergency_contact_number'],
                leader_photo=request.FILES['leader_photo'],
                leader_id_adhaar = request.FILES['leader_id_adhaar'],
                leader_id_PCC = request.FILES['leader_id_PCC'],
                checkin=request.POST['checkin'],        
                checkout=request.POST['checkout'],
                number_of_rooms=request.POST['number_of_rooms'],
                ac_or_nonac=request.POST['ac_or_nonac'],
                veg_or_nonveg=request.POST['veg_or_nonveg'],    
                package=package_str        
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member_name'],
                father_name=request.POST['member_father_name'],
                date_of_birth=request.POST['member_date_of_birth'],
                email=request.POST['member_email'],
                contact_number=request.POST['member_contact_number'],
                address=request.POST['member_address'],
                emergency_contact_person=request.POST['member_emergency_contact_person'],
                emergency_contact_number=request.POST['member_emergency_contact_number'],
                photo=request.FILES['member_photo'],
                id_proof=request.FILES['member_id_proof'],
                id_proof_again=request.FILES['member_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member2_name'],
                father_name=request.POST['member2_father_name'],
                date_of_birth=request.POST['member2_date_of_birth'],
                email=request.POST['member2_email'],
                contact_number=request.POST['member2_contact_number'],
                address=request.POST['member2_address'],
                emergency_contact_person=request.POST['member2_emergency_contact_person'],
                emergency_contact_number=request.POST['member2_emergency_contact_number'],
                photo=request.FILES['member2_photo'],
                id_proof=request.FILES['member2_id_proof'],
                id_proof_again=request.FILES['member2_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member3_name'],
                father_name=request.POST['member3_father_name'],
                date_of_birth=request.POST['member3_date_of_birth'],
                email=request.POST['member3_email'],
                contact_number=request.POST['member3_contact_number'],
                address=request.POST['member2_address'],
                emergency_contact_person=request.POST['member3_emergency_contact_person'],
                emergency_contact_number=request.POST['member3_emergency_contact_number'],
                photo=request.FILES['member3_photo'],
                id_proof=request.FILES['member3_id_proof'],
                id_proof_again=request.FILES['member3_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member4_name'],
                father_name=request.POST['member4_father_name'],
                date_of_birth=request.POST['member4_date_of_birth'],
                email=request.POST['member4_email'],
                contact_number=request.POST['member4_contact_number'],
                address=request.POST['member4_address'],
                emergency_contact_person=request.POST['member4_emergency_contact_person'],
                emergency_contact_number=request.POST['member4_emergency_contact_number'],
                photo=request.FILES['member4_photo'],
                id_proof=request.FILES['member4_id_proof'],
                id_proof_again=request.FILES['member4_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member5_name'],
                father_name=request.POST['member5_father_name'],
                date_of_birth=request.POST['member5_date_of_birth'],
                email=request.POST['member5_email'],
                contact_number=request.POST['member5_contact_number'],
                address=request.POST['member5_address'],
                emergency_contact_person=request.POST['member5_emergency_contact_person'],
                emergency_contact_number=request.POST['member5_emergency_contact_number'],
                photo=request.FILES['member5_photo'],
                id_proof=request.FILES['member5_id_proof'],
                id_proof_again=request.FILES['member5_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member6_name'],
                father_name=request.POST['member6_father_name'],
                date_of_birth=request.POST['member6_date_of_birth'],
                email=request.POST['member6_email'],
                contact_number=request.POST['member5_contact_number'],
                address=request.POST['member6_address'],
                emergency_contact_person=request.POST['member6_emergency_contact_person'],
                emergency_contact_number=request.POST['member6_emergency_contact_number'],
                photo=request.FILES['member6_photo'],
                id_proof=request.FILES['member6_id_proof'],
                id_proof_again=request.FILES['member6_id_proof_again']
            )
            messages.success(request,'Registered Successfully')
            return redirect('/')
    else:
        package_choices = Team.PACKAGE
        return render(request, 'option7.html',{'package_choices': package_choices})

def option8(request):
    if request.method == 'POST':
        if 'submit' in request.POST:
            package_str = ", ".join(request.POST.getlist('package'))
            team = Team.objects.create(
                island = request.POST['island'],
                leader_name = request.POST['leader_name'],
                leader_father_name = request.POST['leader_father_name'],
                leader_contact_number=request.POST['leader_contact_number'],
                leader_date_of_birth=request.POST['leader_date_of_birth'],
                leader_email=request.POST['leader_email'],
                leader_address=request.POST['leader_address'],
                leader_emergency_contact_person= request.POST['leader_emergency_contact_person'],
                leader_emergency_contact_number=request.POST['leader_emergency_contact_number'],
                leader_photo=request.FILES['leader_photo'],
                leader_id_adhaar = request.FILES['leader_id_adhaar'],
                leader_id_PCC = request.FILES['leader_id_PCC'],
                checkin=request.POST['checkin'],        
                checkout=request.POST['checkout'],
                number_of_rooms=request.POST['number_of_rooms'],
                ac_or_nonac=request.POST['ac_or_nonac'],
                veg_or_nonveg=request.POST['veg_or_nonveg'],    
                package=package_str        
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member_name'],
                father_name=request.POST['member_father_name'],
                date_of_birth=request.POST['member_date_of_birth'],
                email=request.POST['member_email'],
                contact_number=request.POST['member_contact_number'],
                address=request.POST['member_address'],
                emergency_contact_person=request.POST['member_emergency_contact_person'],
                emergency_contact_number=request.POST['member_emergency_contact_number'],
                photo=request.FILES['member_photo'],
                id_proof=request.FILES['member_id_proof'],
                id_proof_again=request.FILES['member_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member2_name'],
                father_name=request.POST['member2_father_name'],
                date_of_birth=request.POST['member2_date_of_birth'],
                email=request.POST['member2_email'],
                contact_number=request.POST['member2_contact_number'],
                address=request.POST['member2_address'],
                emergency_contact_person=request.POST['member2_emergency_contact_person'],
                emergency_contact_number=request.POST['member2_emergency_contact_number'],
                photo=request.FILES['member2_photo'],
                id_proof=request.FILES['member2_id_proof'],
                id_proof_again=request.FILES['member2_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member3_name'],
                father_name=request.POST['member3_father_name'],
                date_of_birth=request.POST['member3_date_of_birth'],
                email=request.POST['member3_email'],
                contact_number=request.POST['member3_contact_number'],
                address=request.POST['member2_address'],
                emergency_contact_person=request.POST['member3_emergency_contact_person'],
                emergency_contact_number=request.POST['member3_emergency_contact_number'],
                photo=request.FILES['member3_photo'],
                id_proof=request.FILES['member3_id_proof'],
                id_proof_again=request.FILES['member3_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member4_name'],
                father_name=request.POST['member4_father_name'],
                date_of_birth=request.POST['member4_date_of_birth'],
                email=request.POST['member4_email'],
                contact_number=request.POST['member4_contact_number'],
                address=request.POST['member4_address'],
                emergency_contact_person=request.POST['member4_emergency_contact_person'],
                emergency_contact_number=request.POST['member4_emergency_contact_number'],
                photo=request.FILES['member4_photo'],
                id_proof=request.FILES['member4_id_proof'],
                id_proof_again=request.FILES['member4_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member5_name'],
                father_name=request.POST['member5_father_name'],
                date_of_birth=request.POST['member5_date_of_birth'],
                email=request.POST['member5_email'],
                contact_number=request.POST['member5_contact_number'],
                address=request.POST['member5_address'],
                emergency_contact_person=request.POST['member5_emergency_contact_person'],
                emergency_contact_number=request.POST['member5_emergency_contact_number'],
                photo=request.FILES['member5_photo'],
                id_proof=request.FILES['member5_id_proof'],
                id_proof_again=request.FILES['member5_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member6_name'],
                father_name=request.POST['member6_father_name'],
                date_of_birth=request.POST['member6_date_of_birth'],
                email=request.POST['member6_email'],
                contact_number=request.POST['member5_contact_number'],
                address=request.POST['member6_address'],
                emergency_contact_person=request.POST['member6_emergency_contact_person'],
                emergency_contact_number=request.POST['member6_emergency_contact_number'],
                photo=request.FILES['member6_photo'],
                id_proof=request.FILES['member6_id_proof'],
                id_proof_again=request.FILES['member6_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member7_name'],
                father_name=request.POST['member7_father_name'],
                date_of_birth=request.POST['member7_date_of_birth'],
                email=request.POST['member7_email'],
                contact_number=request.POST['member7_contact_number'],
                address=request.POST['member7_address'],
                emergency_contact_person=request.POST['member7_emergency_contact_person'],
                emergency_contact_number=request.POST['member7_emergency_contact_number'],
                photo=request.FILES['member7_photo'],
                id_proof=request.FILES['member7_id_proof'],
                id_proof_again=request.FILES['member7_id_proof_again']
            )
            messages.success(request,'Registered Successfully')
            return redirect('/')
    else:
        package_choices = Team.PACKAGE
        return render(request, 'option8.html',{'package_choices': package_choices})
def option9(request):
    if request.method == 'POST':
        if 'submit' in request.POST:
            package_str = ", ".join(request.POST.getlist('package'))
            team = Team.objects.create(
                island = request.POST['island'],
                leader_name = request.POST['leader_name'],
                leader_father_name = request.POST['leader_father_name'],
                leader_contact_number=request.POST['leader_contact_number'],
                leader_date_of_birth=request.POST['leader_date_of_birth'],
                leader_email=request.POST['leader_email'],
                leader_address=request.POST['leader_address'],
                leader_emergency_contact_person= request.POST['leader_emergency_contact_person'],
                leader_emergency_contact_number=request.POST['leader_emergency_contact_number'],
                leader_photo=request.FILES['leader_photo'],
                leader_id_adhaar = request.FILES['leader_id_adhaar'],
                leader_id_PCC = request.FILES['leader_id_PCC'],
                checkin=request.POST['checkin'],        
                checkout=request.POST['checkout'],
                number_of_rooms=request.POST['number_of_rooms'],
                ac_or_nonac=request.POST['ac_or_nonac'],
                veg_or_nonveg=request.POST['veg_or_nonveg'],    
                package=package_str        
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member_name'],
                father_name=request.POST['member_father_name'],
                date_of_birth=request.POST['member_date_of_birth'],
                email=request.POST['member_email'],
                contact_number=request.POST['member_contact_number'],
                address=request.POST['member_address'],
                emergency_contact_person=request.POST['member_emergency_contact_person'],
                emergency_contact_number=request.POST['member_emergency_contact_number'],
                photo=request.FILES['member_photo'],
                id_proof=request.FILES['member_id_proof'],
                id_proof_again=request.FILES['member_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member2_name'],
                father_name=request.POST['member2_father_name'],
                date_of_birth=request.POST['member2_date_of_birth'],
                email=request.POST['member2_email'],
                contact_number=request.POST['member2_contact_number'],
                address=request.POST['member2_address'],
                emergency_contact_person=request.POST['member2_emergency_contact_person'],
                emergency_contact_number=request.POST['member2_emergency_contact_number'],
                photo=request.FILES['member2_photo'],
                id_proof=request.FILES['member2_id_proof'],
                id_proof_again=request.FILES['member2_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member3_name'],
                father_name=request.POST['member3_father_name'],
                date_of_birth=request.POST['member3_date_of_birth'],
                email=request.POST['member3_email'],
                contact_number=request.POST['member3_contact_number'],
                address=request.POST['member2_address'],
                emergency_contact_person=request.POST['member3_emergency_contact_person'],
                emergency_contact_number=request.POST['member3_emergency_contact_number'],
                photo=request.FILES['member3_photo'],
                id_proof=request.FILES['member3_id_proof'],
                id_proof_again=request.FILES['member3_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member4_name'],
                father_name=request.POST['member4_father_name'],
                date_of_birth=request.POST['member4_date_of_birth'],
                email=request.POST['member4_email'],
                contact_number=request.POST['member4_contact_number'],
                address=request.POST['member4_address'],
                emergency_contact_person=request.POST['member4_emergency_contact_person'],
                emergency_contact_number=request.POST['member4_emergency_contact_number'],
                photo=request.FILES['member4_photo'],
                id_proof=request.FILES['member4_id_proof'],
                id_proof_again=request.FILES['member4_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member5_name'],
                father_name=request.POST['member5_father_name'],
                date_of_birth=request.POST['member5_date_of_birth'],
                email=request.POST['member5_email'],
                contact_number=request.POST['member5_contact_number'],
                address=request.POST['member5_address'],
                emergency_contact_person=request.POST['member5_emergency_contact_person'],
                emergency_contact_number=request.POST['member5_emergency_contact_number'],
                photo=request.FILES['member5_photo'],
                id_proof=request.FILES['member5_id_proof'],
                id_proof_again=request.FILES['member5_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member6_name'],
                father_name=request.POST['member6_father_name'],
                date_of_birth=request.POST['member6_date_of_birth'],
                email=request.POST['member6_email'],
                contact_number=request.POST['member5_contact_number'],
                address=request.POST['member6_address'],
                emergency_contact_person=request.POST['member6_emergency_contact_person'],
                emergency_contact_number=request.POST['member6_emergency_contact_number'],
                photo=request.FILES['member6_photo'],
                id_proof=request.FILES['member6_id_proof'],
                id_proof_again=request.FILES['member6_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member7_name'],
                father_name=request.POST['member7_father_name'],
                date_of_birth=request.POST['member7_date_of_birth'],
                email=request.POST['member7_email'],
                contact_number=request.POST['member7_contact_number'],
                address=request.POST['member7_address'],
                emergency_contact_person=request.POST['member7_emergency_contact_person'],
                emergency_contact_number=request.POST['member7_emergency_contact_number'],
                photo=request.FILES['member7_photo'],
                id_proof=request.FILES['member7_id_proof'],
                id_proof_again=request.FILES['member7_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member8_name'],
                father_name=request.POST['member8_father_name'],
                date_of_birth=request.POST['member8_date_of_birth'],
                email=request.POST['member8_email'],
                contact_number=request.POST['member8_contact_number'],
                address=request.POST['member8_address'],
                emergency_contact_person=request.POST['member8_emergency_contact_person'],
                emergency_contact_number=request.POST['member8_emergency_contact_number'],
                photo=request.FILES['member8_photo'],
                id_proof=request.FILES['member8_id_proof'],
                id_proof_again=request.FILES['member8_id_proof_again']
            )
            messages.success(request,'Registered Successfully')
            return redirect('/')
    else:
        package_choices = Team.PACKAGE
        return render(request, 'option9.html',{'package_choices': package_choices})

def option10(request):
    if request.method == 'POST':
        if 'submit' in request.POST:
            package_str = ", ".join(request.POST.getlist('package'))
            team = Team.objects.create(
                island = request.POST['island'],
                leader_name = request.POST['leader_name'],
                leader_father_name = request.POST['leader_father_name'],
                leader_contact_number=request.POST['leader_contact_number'],
                leader_date_of_birth=request.POST['leader_date_of_birth'],
                leader_email=request.POST['leader_email'],
                leader_address=request.POST['leader_address'],
                leader_emergency_contact_person= request.POST['leader_emergency_contact_person'],
                leader_emergency_contact_number=request.POST['leader_emergency_contact_number'],
                leader_photo=request.FILES['leader_photo'],
                leader_id_adhaar = request.FILES['leader_id_adhaar'],
                leader_id_PCC = request.FILES['leader_id_PCC'],
                checkin=request.POST['checkin'],        
                checkout=request.POST['checkout'],
                number_of_rooms=request.POST['number_of_rooms'],
                ac_or_nonac=request.POST['ac_or_nonac'],
                veg_or_nonveg=request.POST['veg_or_nonveg'],    
                package=package_str        
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member_name'],
                father_name=request.POST['member_father_name'],
                date_of_birth=request.POST['member_date_of_birth'],
                email=request.POST['member_email'],
                contact_number=request.POST['member_contact_number'],
                address=request.POST['member_address'],
                emergency_contact_person=request.POST['member_emergency_contact_person'],
                emergency_contact_number=request.POST['member_emergency_contact_number'],
                photo=request.FILES['member_photo'],
                id_proof=request.FILES['member_id_proof'],
                id_proof_again=request.FILES['member_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member2_name'],
                father_name=request.POST['member2_father_name'],
                date_of_birth=request.POST['member2_date_of_birth'],
                email=request.POST['member2_email'],
                contact_number=request.POST['member2_contact_number'],
                address=request.POST['member2_address'],
                emergency_contact_person=request.POST['member2_emergency_contact_person'],
                emergency_contact_number=request.POST['member2_emergency_contact_number'],
                photo=request.FILES['member2_photo'],
                id_proof=request.FILES['member2_id_proof'],
                id_proof_again=request.FILES['member2_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member3_name'],
                father_name=request.POST['member3_father_name'],
                date_of_birth=request.POST['member3_date_of_birth'],
                email=request.POST['member3_email'],
                contact_number=request.POST['member3_contact_number'],
                address=request.POST['member2_address'],
                emergency_contact_person=request.POST['member3_emergency_contact_person'],
                emergency_contact_number=request.POST['member3_emergency_contact_number'],
                photo=request.FILES['member3_photo'],
                id_proof=request.FILES['member3_id_proof'],
                id_proof_again=request.FILES['member3_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member4_name'],
                father_name=request.POST['member4_father_name'],
                date_of_birth=request.POST['member4_date_of_birth'],
                email=request.POST['member4_email'],
                contact_number=request.POST['member4_contact_number'],
                address=request.POST['member4_address'],
                emergency_contact_person=request.POST['member4_emergency_contact_person'],
                emergency_contact_number=request.POST['member4_emergency_contact_number'],
                photo=request.FILES['member4_photo'],
                id_proof=request.FILES['member4_id_proof'],
                id_proof_again=request.FILES['member4_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member5_name'],
                father_name=request.POST['member5_father_name'],
                date_of_birth=request.POST['member5_date_of_birth'],
                email=request.POST['member5_email'],
                contact_number=request.POST['member5_contact_number'],
                address=request.POST['member5_address'],
                emergency_contact_person=request.POST['member5_emergency_contact_person'],
                emergency_contact_number=request.POST['member5_emergency_contact_number'],
                photo=request.FILES['member5_photo'],
                id_proof=request.FILES['member5_id_proof'],
                id_proof_again=request.FILES['member5_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member6_name'],
                father_name=request.POST['member6_father_name'],
                date_of_birth=request.POST['member6_date_of_birth'],
                email=request.POST['member6_email'],
                contact_number=request.POST['member5_contact_number'],
                address=request.POST['member6_address'],
                emergency_contact_person=request.POST['member6_emergency_contact_person'],
                emergency_contact_number=request.POST['member6_emergency_contact_number'],
                photo=request.FILES['member6_photo'],
                id_proof=request.FILES['member6_id_proof'],
                id_proof_again=request.FILES['member6_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member7_name'],
                father_name=request.POST['member7_father_name'],
                date_of_birth=request.POST['member7_date_of_birth'],
                email=request.POST['member7_email'],
                contact_number=request.POST['member7_contact_number'],
                address=request.POST['member7_address'],
                emergency_contact_person=request.POST['member7_emergency_contact_person'],
                emergency_contact_number=request.POST['member7_emergency_contact_number'],
                photo=request.FILES['member7_photo'],
                id_proof=request.FILES['member7_id_proof'],
                id_proof_again=request.FILES['member7_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member8_name'],
                father_name=request.POST['member8_father_name'],
                date_of_birth=request.POST['member8_date_of_birth'],
                email=request.POST['member8_email'],
                contact_number=request.POST['member8_contact_number'],
                address=request.POST['member8_address'],
                emergency_contact_person=request.POST['member8_emergency_contact_person'],
                emergency_contact_number=request.POST['member8_emergency_contact_number'],
                photo=request.FILES['member8_photo'],
                id_proof=request.FILES['member8_id_proof'],
                id_proof_again=request.FILES['member8_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member9_name'],
                father_name=request.POST['member9_father_name'],
                date_of_birth=request.POST['member9_date_of_birth'],
                email=request.POST['member9_email'],
                contact_number=request.POST['member9_contact_number'],
                address=request.POST['member9_address'],
                emergency_contact_person=request.POST['member9_emergency_contact_person'],
                emergency_contact_number=request.POST['member9_emergency_contact_number'],
                photo=request.FILES['member9_photo'],
                id_proof=request.FILES['member9_id_proof'],
                id_proof_again=request.FILES['member9_id_proof_again']
            )
            messages.success(request,'Registered Successfully')
            return redirect('/')
    else:
        package_choices = Team.PACKAGE
        return render(request, 'option10.html',{'package_choices': package_choices})

def option11(request):
    if request.method == 'POST':
        if 'submit' in request.POST:
            package_str = ", ".join(request.POST.getlist('package'))
            team = Team.objects.create(
                island = request.POST['island'],
                leader_name = request.POST['leader_name'],
                leader_father_name = request.POST['leader_father_name'],
                leader_contact_number=request.POST['leader_contact_number'],
                leader_date_of_birth=request.POST['leader_date_of_birth'],
                leader_email=request.POST['leader_email'],
                leader_address=request.POST['leader_address'],
                leader_emergency_contact_person= request.POST['leader_emergency_contact_person'],
                leader_emergency_contact_number=request.POST['leader_emergency_contact_number'],
                leader_photo=request.FILES['leader_photo'],
                leader_id_adhaar = request.FILES['leader_id_adhaar'],
                leader_id_PCC = request.FILES['leader_id_PCC'],
                checkin=request.POST['checkin'],        
                checkout=request.POST['checkout'],
                number_of_rooms=request.POST['number_of_rooms'],
                ac_or_nonac=request.POST['ac_or_nonac'],
                veg_or_nonveg=request.POST['veg_or_nonveg'],    
                package=package_str        
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member_name'],
                father_name=request.POST['member_father_name'],
                date_of_birth=request.POST['member_date_of_birth'],
                email=request.POST['member_email'],
                contact_number=request.POST['member_contact_number'],
                address=request.POST['member_address'],
                emergency_contact_person=request.POST['member_emergency_contact_person'],
                emergency_contact_number=request.POST['member_emergency_contact_number'],
                photo=request.FILES['member_photo'],
                id_proof=request.FILES['member_id_proof'],
                id_proof_again=request.FILES['member_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member2_name'],
                father_name=request.POST['member2_father_name'],
                date_of_birth=request.POST['member2_date_of_birth'],
                email=request.POST['member2_email'],
                contact_number=request.POST['member2_contact_number'],
                address=request.POST['member2_address'],
                emergency_contact_person=request.POST['member2_emergency_contact_person'],
                emergency_contact_number=request.POST['member2_emergency_contact_number'],
                photo=request.FILES['member2_photo'],
                id_proof=request.FILES['member2_id_proof'],
                id_proof_again=request.FILES['member2_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member3_name'],
                father_name=request.POST['member3_father_name'],
                date_of_birth=request.POST['member3_date_of_birth'],
                email=request.POST['member3_email'],
                contact_number=request.POST['member3_contact_number'],
                address=request.POST['member2_address'],
                emergency_contact_person=request.POST['member3_emergency_contact_person'],
                emergency_contact_number=request.POST['member3_emergency_contact_number'],
                photo=request.FILES['member3_photo'],
                id_proof=request.FILES['member3_id_proof'],
                id_proof_again=request.FILES['member3_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member4_name'],
                father_name=request.POST['member4_father_name'],
                date_of_birth=request.POST['member4_date_of_birth'],
                email=request.POST['member4_email'],
                contact_number=request.POST['member4_contact_number'],
                address=request.POST['member4_address'],
                emergency_contact_person=request.POST['member4_emergency_contact_person'],
                emergency_contact_number=request.POST['member4_emergency_contact_number'],
                photo=request.FILES['member4_photo'],
                id_proof=request.FILES['member4_id_proof'],
                id_proof_again=request.FILES['member4_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member5_name'],
                father_name=request.POST['member5_father_name'],
                date_of_birth=request.POST['member5_date_of_birth'],
                email=request.POST['member5_email'],
                contact_number=request.POST['member5_contact_number'],
                address=request.POST['member5_address'],
                emergency_contact_person=request.POST['member5_emergency_contact_person'],
                emergency_contact_number=request.POST['member5_emergency_contact_number'],
                photo=request.FILES['member5_photo'],
                id_proof=request.FILES['member5_id_proof'],
                id_proof_again=request.FILES['member5_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member6_name'],
                father_name=request.POST['member6_father_name'],
                date_of_birth=request.POST['member6_date_of_birth'],
                email=request.POST['member6_email'],
                contact_number=request.POST['member5_contact_number'],
                address=request.POST['member6_address'],
                emergency_contact_person=request.POST['member6_emergency_contact_person'],
                emergency_contact_number=request.POST['member6_emergency_contact_number'],
                photo=request.FILES['member6_photo'],
                id_proof=request.FILES['member6_id_proof'],
                id_proof_again=request.FILES['member6_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member7_name'],
                father_name=request.POST['member7_father_name'],
                date_of_birth=request.POST['member7_date_of_birth'],
                email=request.POST['member7_email'],
                contact_number=request.POST['member7_contact_number'],
                address=request.POST['member7_address'],
                emergency_contact_person=request.POST['member7_emergency_contact_person'],
                emergency_contact_number=request.POST['member7_emergency_contact_number'],
                photo=request.FILES['member7_photo'],
                id_proof=request.FILES['member7_id_proof'],
                id_proof_again=request.FILES['member7_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member8_name'],
                father_name=request.POST['member8_father_name'],
                date_of_birth=request.POST['member8_date_of_birth'],
                email=request.POST['member8_email'],
                contact_number=request.POST['member8_contact_number'],
                address=request.POST['member8_address'],
                emergency_contact_person=request.POST['member8_emergency_contact_person'],
                emergency_contact_number=request.POST['member8_emergency_contact_number'],
                photo=request.FILES['member8_photo'],
                id_proof=request.FILES['member8_id_proof'],
                id_proof_again=request.FILES['member8_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member9_name'],
                father_name=request.POST['member9_father_name'],
                date_of_birth=request.POST['member9_date_of_birth'],
                email=request.POST['member9_email'],
                contact_number=request.POST['member9_contact_number'],
                address=request.POST['member9_address'],
                emergency_contact_person=request.POST['member9_emergency_contact_person'],
                emergency_contact_number=request.POST['member9_emergency_contact_number'],
                photo=request.FILES['member9_photo'],
                id_proof=request.FILES['member9_id_proof'],
                id_proof_again=request.FILES['member9_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member10_name'],
                father_name=request.POST['member10_father_name'],
                date_of_birth=request.POST['member10_date_of_birth'],
                email=request.POST['member10_email'],
                contact_number=request.POST['member10_contact_number'],
                address=request.POST['member10_address'],
                emergency_contact_person=request.POST['member10_emergency_contact_person'],
                emergency_contact_number=request.POST['member10_emergency_contact_number'],
                photo=request.FILES['member10_photo'],
                id_proof=request.FILES['member10_id_proof'],
                id_proof_again=request.FILES['member10_id_proof_again']
            )
            messages.success(request,'Registered Successfully')
            return redirect('/')
    else:
        package_choices = Team.PACKAGE
        return render(request, 'option11.html',{'package_choices': package_choices})

def option12(request):
    if request.method == 'POST':
        if 'submit' in request.POST:
            package_str = ", ".join(request.POST.getlist('package'))
            team = Team.objects.create(
                island = request.POST['island'],
                leader_name = request.POST['leader_name'],
                leader_father_name = request.POST['leader_father_name'],
                leader_contact_number=request.POST['leader_contact_number'],
                leader_date_of_birth=request.POST['leader_date_of_birth'],
                leader_email=request.POST['leader_email'],
                leader_address=request.POST['leader_address'],
                leader_emergency_contact_person= request.POST['leader_emergency_contact_person'],
                leader_emergency_contact_number=request.POST['leader_emergency_contact_number'],
                leader_photo=request.FILES['leader_photo'],
                leader_id_adhaar = request.FILES['leader_id_adhaar'],
                leader_id_PCC = request.FILES['leader_id_PCC'],
                checkin=request.POST['checkin'],        
                checkout=request.POST['checkout'],
                number_of_rooms=request.POST['number_of_rooms'],
                ac_or_nonac=request.POST['ac_or_nonac'],
                veg_or_nonveg=request.POST['veg_or_nonveg'],    
                package=package_str        
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member_name'],
                father_name=request.POST['member_father_name'],
                date_of_birth=request.POST['member_date_of_birth'],
                email=request.POST['member_email'],
                contact_number=request.POST['member_contact_number'],
                address=request.POST['member_address'],
                emergency_contact_person=request.POST['member_emergency_contact_person'],
                emergency_contact_number=request.POST['member_emergency_contact_number'],
                photo=request.FILES['member_photo'],
                id_proof=request.FILES['member_id_proof'],
                id_proof_again=request.FILES['member_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member2_name'],
                father_name=request.POST['member2_father_name'],
                date_of_birth=request.POST['member2_date_of_birth'],
                email=request.POST['member2_email'],
                contact_number=request.POST['member2_contact_number'],
                address=request.POST['member2_address'],
                emergency_contact_person=request.POST['member2_emergency_contact_person'],
                emergency_contact_number=request.POST['member2_emergency_contact_number'],
                photo=request.FILES['member2_photo'],
                id_proof=request.FILES['member2_id_proof'],
                id_proof_again=request.FILES['member2_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member3_name'],
                father_name=request.POST['member3_father_name'],
                date_of_birth=request.POST['member3_date_of_birth'],
                email=request.POST['member3_email'],
                contact_number=request.POST['member3_contact_number'],
                address=request.POST['member2_address'],
                emergency_contact_person=request.POST['member3_emergency_contact_person'],
                emergency_contact_number=request.POST['member3_emergency_contact_number'],
                photo=request.FILES['member3_photo'],
                id_proof=request.FILES['member3_id_proof'],
                id_proof_again=request.FILES['member3_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member4_name'],
                father_name=request.POST['member4_father_name'],
                date_of_birth=request.POST['member4_date_of_birth'],
                email=request.POST['member4_email'],
                contact_number=request.POST['member4_contact_number'],
                address=request.POST['member4_address'],
                emergency_contact_person=request.POST['member4_emergency_contact_person'],
                emergency_contact_number=request.POST['member4_emergency_contact_number'],
                photo=request.FILES['member4_photo'],
                id_proof=request.FILES['member4_id_proof'],
                id_proof_again=request.FILES['member4_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member5_name'],
                father_name=request.POST['member5_father_name'],
                date_of_birth=request.POST['member5_date_of_birth'],
                email=request.POST['member5_email'],
                contact_number=request.POST['member5_contact_number'],
                address=request.POST['member5_address'],
                emergency_contact_person=request.POST['member5_emergency_contact_person'],
                emergency_contact_number=request.POST['member5_emergency_contact_number'],
                photo=request.FILES['member5_photo'],
                id_proof=request.FILES['member5_id_proof'],
                id_proof_again=request.FILES['member5_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member6_name'],
                father_name=request.POST['member6_father_name'],
                date_of_birth=request.POST['member6_date_of_birth'],
                email=request.POST['member6_email'],
                contact_number=request.POST['member5_contact_number'],
                address=request.POST['member6_address'],
                emergency_contact_person=request.POST['member6_emergency_contact_person'],
                emergency_contact_number=request.POST['member6_emergency_contact_number'],
                photo=request.FILES['member6_photo'],
                id_proof=request.FILES['member6_id_proof'],
                id_proof_again=request.FILES['member6_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member7_name'],
                father_name=request.POST['member7_father_name'],
                date_of_birth=request.POST['member7_date_of_birth'],
                email=request.POST['member7_email'],
                contact_number=request.POST['member7_contact_number'],
                address=request.POST['member7_address'],
                emergency_contact_person=request.POST['member7_emergency_contact_person'],
                emergency_contact_number=request.POST['member7_emergency_contact_number'],
                photo=request.FILES['member7_photo'],
                id_proof=request.FILES['member7_id_proof'],
                id_proof_again=request.FILES['member7_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member8_name'],
                father_name=request.POST['member8_father_name'],
                date_of_birth=request.POST['member8_date_of_birth'],
                email=request.POST['member8_email'],
                contact_number=request.POST['member8_contact_number'],
                address=request.POST['member8_address'],
                emergency_contact_person=request.POST['member8_emergency_contact_person'],
                emergency_contact_number=request.POST['member8_emergency_contact_number'],
                photo=request.FILES['member8_photo'],
                id_proof=request.FILES['member8_id_proof'],
                id_proof_again=request.FILES['member8_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member9_name'],
                father_name=request.POST['member9_father_name'],
                date_of_birth=request.POST['member9_date_of_birth'],
                email=request.POST['member9_email'],
                contact_number=request.POST['member9_contact_number'],
                address=request.POST['member9_address'],
                emergency_contact_person=request.POST['member9_emergency_contact_person'],
                emergency_contact_number=request.POST['member9_emergency_contact_number'],
                photo=request.FILES['member9_photo'],
                id_proof=request.FILES['member9_id_proof'],
                id_proof_again=request.FILES['member9_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member10_name'],
                father_name=request.POST['member10_father_name'],
                date_of_birth=request.POST['member10_date_of_birth'],
                email=request.POST['member10_email'],
                contact_number=request.POST['member10_contact_number'],
                address=request.POST['member10_address'],
                emergency_contact_person=request.POST['member10_emergency_contact_person'],
                emergency_contact_number=request.POST['member10_emergency_contact_number'],
                photo=request.FILES['member10_photo'],
                id_proof=request.FILES['member10_id_proof'],
                id_proof_again=request.FILES['member10_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member11_name'],
                father_name=request.POST['member11_father_name'],
                date_of_birth=request.POST['member11_date_of_birth'],
                email=request.POST['member11_email'],
                contact_number=request.POST['member11_contact_number'],
                address=request.POST['member11_address'],
                emergency_contact_person=request.POST['member11_emergency_contact_person'],
                emergency_contact_number=request.POST['member11_emergency_contact_number'],
                photo=request.FILES['member11_photo'],
                id_proof=request.FILES['member11_id_proof'],
                id_proof_again=request.FILES['member11_id_proof_again']
            )
            messages.success(request,'Registered Successfully')
            return redirect('/')
    else:
        package_choices = Team.PACKAGE
        return render(request, 'option12.html',{'package_choices': package_choices})

def option13(request):
    if request.method == 'POST':
        if 'submit' in request.POST:
            package_str = ", ".join(request.POST.getlist('package'))
            team = Team.objects.create(
                island = request.POST['island'],
                leader_name = request.POST['leader_name'],
                leader_father_name = request.POST['leader_father_name'],
                leader_contact_number=request.POST['leader_contact_number'],
                leader_date_of_birth=request.POST['leader_date_of_birth'],
                leader_email=request.POST['leader_email'],
                leader_address=request.POST['leader_address'],
                leader_emergency_contact_person= request.POST['leader_emergency_contact_person'],
                leader_emergency_contact_number=request.POST['leader_emergency_contact_number'],
                leader_photo=request.FILES['leader_photo'],
                leader_id_adhaar = request.FILES['leader_id_adhaar'],
                leader_id_PCC = request.FILES['leader_id_PCC'],
                checkin=request.POST['checkin'],        
                checkout=request.POST['checkout'],
                number_of_rooms=request.POST['number_of_rooms'],
                ac_or_nonac=request.POST['ac_or_nonac'],
                veg_or_nonveg=request.POST['veg_or_nonveg'],    
                package=package_str        
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member_name'],
                father_name=request.POST['member_father_name'],
                date_of_birth=request.POST['member_date_of_birth'],
                email=request.POST['member_email'],
                contact_number=request.POST['member_contact_number'],
                address=request.POST['member_address'],
                emergency_contact_person=request.POST['member_emergency_contact_person'],
                emergency_contact_number=request.POST['member_emergency_contact_number'],
                photo=request.FILES['member_photo'],
                id_proof=request.FILES['member_id_proof'],
                id_proof_again=request.FILES['member_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member2_name'],
                father_name=request.POST['member2_father_name'],
                date_of_birth=request.POST['member2_date_of_birth'],
                email=request.POST['member2_email'],
                contact_number=request.POST['member2_contact_number'],
                address=request.POST['member2_address'],
                emergency_contact_person=request.POST['member2_emergency_contact_person'],
                emergency_contact_number=request.POST['member2_emergency_contact_number'],
                photo=request.FILES['member2_photo'],
                id_proof=request.FILES['member2_id_proof'],
                id_proof_again=request.FILES['member2_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member3_name'],
                father_name=request.POST['member3_father_name'],
                date_of_birth=request.POST['member3_date_of_birth'],
                email=request.POST['member3_email'],
                contact_number=request.POST['member3_contact_number'],
                address=request.POST['member2_address'],
                emergency_contact_person=request.POST['member3_emergency_contact_person'],
                emergency_contact_number=request.POST['member3_emergency_contact_number'],
                photo=request.FILES['member3_photo'],
                id_proof=request.FILES['member3_id_proof'],
                id_proof_again=request.FILES['member3_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member4_name'],
                father_name=request.POST['member4_father_name'],
                date_of_birth=request.POST['member4_date_of_birth'],
                email=request.POST['member4_email'],
                contact_number=request.POST['member4_contact_number'],
                address=request.POST['member4_address'],
                emergency_contact_person=request.POST['member4_emergency_contact_person'],
                emergency_contact_number=request.POST['member4_emergency_contact_number'],
                photo=request.FILES['member4_photo'],
                id_proof=request.FILES['member4_id_proof'],
                id_proof_again=request.FILES['member4_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member5_name'],
                father_name=request.POST['member5_father_name'],
                date_of_birth=request.POST['member5_date_of_birth'],
                email=request.POST['member5_email'],
                contact_number=request.POST['member5_contact_number'],
                address=request.POST['member5_address'],
                emergency_contact_person=request.POST['member5_emergency_contact_person'],
                emergency_contact_number=request.POST['member5_emergency_contact_number'],
                photo=request.FILES['member5_photo'],
                id_proof=request.FILES['member5_id_proof'],
                id_proof_again=request.FILES['member5_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member6_name'],
                father_name=request.POST['member6_father_name'],
                date_of_birth=request.POST['member6_date_of_birth'],
                email=request.POST['member6_email'],
                contact_number=request.POST['member5_contact_number'],
                address=request.POST['member6_address'],
                emergency_contact_person=request.POST['member6_emergency_contact_person'],
                emergency_contact_number=request.POST['member6_emergency_contact_number'],
                photo=request.FILES['member6_photo'],
                id_proof=request.FILES['member6_id_proof'],
                id_proof_again=request.FILES['member6_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member7_name'],
                father_name=request.POST['member7_father_name'],
                date_of_birth=request.POST['member7_date_of_birth'],
                email=request.POST['member7_email'],
                contact_number=request.POST['member7_contact_number'],
                address=request.POST['member7_address'],
                emergency_contact_person=request.POST['member7_emergency_contact_person'],
                emergency_contact_number=request.POST['member7_emergency_contact_number'],
                photo=request.FILES['member7_photo'],
                id_proof=request.FILES['member7_id_proof'],
                id_proof_again=request.FILES['member7_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member8_name'],
                father_name=request.POST['member8_father_name'],
                date_of_birth=request.POST['member8_date_of_birth'],
                email=request.POST['member8_email'],
                contact_number=request.POST['member8_contact_number'],
                address=request.POST['member8_address'],
                emergency_contact_person=request.POST['member8_emergency_contact_person'],
                emergency_contact_number=request.POST['member8_emergency_contact_number'],
                photo=request.FILES['member8_photo'],
                id_proof=request.FILES['member8_id_proof'],
                id_proof_again=request.FILES['member8_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member9_name'],
                father_name=request.POST['member9_father_name'],
                date_of_birth=request.POST['member9_date_of_birth'],
                email=request.POST['member9_email'],
                contact_number=request.POST['member9_contact_number'],
                address=request.POST['member9_address'],
                emergency_contact_person=request.POST['member9_emergency_contact_person'],
                emergency_contact_number=request.POST['member9_emergency_contact_number'],
                photo=request.FILES['member9_photo'],
                id_proof=request.FILES['member9_id_proof'],
                id_proof_again=request.FILES['member9_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member10_name'],
                father_name=request.POST['member10_father_name'],
                date_of_birth=request.POST['member10_date_of_birth'],
                email=request.POST['member10_email'],
                contact_number=request.POST['member10_contact_number'],
                address=request.POST['member10_address'],
                emergency_contact_person=request.POST['member10_emergency_contact_person'],
                emergency_contact_number=request.POST['member10_emergency_contact_number'],
                photo=request.FILES['member10_photo'],
                id_proof=request.FILES['member10_id_proof'],
                id_proof_again=request.FILES['member10_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member11_name'],
                father_name=request.POST['member11_father_name'],
                date_of_birth=request.POST['member11_date_of_birth'],
                email=request.POST['member11_email'],
                contact_number=request.POST['member11_contact_number'],
                address=request.POST['member11_address'],
                emergency_contact_person=request.POST['member11_emergency_contact_person'],
                emergency_contact_number=request.POST['member11_emergency_contact_number'],
                photo=request.FILES['member11_photo'],
                id_proof=request.FILES['member11_id_proof'],
                id_proof_again=request.FILES['member11_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member12_name'],
                father_name=request.POST['member12_father_name'],
                date_of_birth=request.POST['member12_date_of_birth'],
                email=request.POST['member12_email'],
                contact_number=request.POST['member12_contact_number'],
                address=request.POST['member12_address'],
                emergency_contact_person=request.POST['member12_emergency_contact_person'],
                emergency_contact_number=request.POST['member12_emergency_contact_number'],
                photo=request.FILES['member12_photo'],
                id_proof=request.FILES['member12_id_proof'],
                id_proof_again=request.FILES['member12_id_proof_again']
            )
            messages.success(request,'Registered Successfully')
            return redirect('/')
    else:
        package_choices = Team.PACKAGE
        return render(request, 'option13.html',{'package_choices': package_choices})

def option14(request):
    if request.method == 'POST':
        if 'submit' in request.POST:
            package_str = ", ".join(request.POST.getlist('package'))
            team = Team.objects.create(
                island = request.POST['island'],
                leader_name = request.POST['leader_name'],
                leader_father_name = request.POST['leader_father_name'],
                leader_contact_number=request.POST['leader_contact_number'],
                leader_date_of_birth=request.POST['leader_date_of_birth'],
                leader_email=request.POST['leader_email'],
                leader_address=request.POST['leader_address'],
                leader_emergency_contact_person= request.POST['leader_emergency_contact_person'],
                leader_emergency_contact_number=request.POST['leader_emergency_contact_number'],
                leader_photo=request.FILES['leader_photo'],
                leader_id_adhaar = request.FILES['leader_id_adhaar'],
                leader_id_PCC = request.FILES['leader_id_PCC'],
                checkin=request.POST['checkin'],        
                checkout=request.POST['checkout'],
                number_of_rooms=request.POST['number_of_rooms'],
                ac_or_nonac=request.POST['ac_or_nonac'],
                veg_or_nonveg=request.POST['veg_or_nonveg'],    
                package=package_str        
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member_name'],
                father_name=request.POST['member_father_name'],
                date_of_birth=request.POST['member_date_of_birth'],
                email=request.POST['member_email'],
                contact_number=request.POST['member_contact_number'],
                address=request.POST['member_address'],
                emergency_contact_person=request.POST['member_emergency_contact_person'],
                emergency_contact_number=request.POST['member_emergency_contact_number'],
                photo=request.FILES['member_photo'],
                id_proof=request.FILES['member_id_proof'],
                id_proof_again=request.FILES['member_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member2_name'],
                father_name=request.POST['member2_father_name'],
                date_of_birth=request.POST['member2_date_of_birth'],
                email=request.POST['member2_email'],
                contact_number=request.POST['member2_contact_number'],
                address=request.POST['member2_address'],
                emergency_contact_person=request.POST['member2_emergency_contact_person'],
                emergency_contact_number=request.POST['member2_emergency_contact_number'],
                photo=request.FILES['member2_photo'],
                id_proof=request.FILES['member2_id_proof'],
                id_proof_again=request.FILES['member2_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member3_name'],
                father_name=request.POST['member3_father_name'],
                date_of_birth=request.POST['member3_date_of_birth'],
                email=request.POST['member3_email'],
                contact_number=request.POST['member3_contact_number'],
                address=request.POST['member2_address'],
                emergency_contact_person=request.POST['member3_emergency_contact_person'],
                emergency_contact_number=request.POST['member3_emergency_contact_number'],
                photo=request.FILES['member3_photo'],
                id_proof=request.FILES['member3_id_proof'],
                id_proof_again=request.FILES['member3_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member4_name'],
                father_name=request.POST['member4_father_name'],
                date_of_birth=request.POST['member4_date_of_birth'],
                email=request.POST['member4_email'],
                contact_number=request.POST['member4_contact_number'],
                address=request.POST['member4_address'],
                emergency_contact_person=request.POST['member4_emergency_contact_person'],
                emergency_contact_number=request.POST['member4_emergency_contact_number'],
                photo=request.FILES['member4_photo'],
                id_proof=request.FILES['member4_id_proof'],
                id_proof_again=request.FILES['member4_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member5_name'],
                father_name=request.POST['member5_father_name'],
                date_of_birth=request.POST['member5_date_of_birth'],
                email=request.POST['member5_email'],
                contact_number=request.POST['member5_contact_number'],
                address=request.POST['member5_address'],
                emergency_contact_person=request.POST['member5_emergency_contact_person'],
                emergency_contact_number=request.POST['member5_emergency_contact_number'],
                photo=request.FILES['member5_photo'],
                id_proof=request.FILES['member5_id_proof'],
                id_proof_again=request.FILES['member5_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member6_name'],
                father_name=request.POST['member6_father_name'],
                date_of_birth=request.POST['member6_date_of_birth'],
                email=request.POST['member6_email'],
                contact_number=request.POST['member5_contact_number'],
                address=request.POST['member6_address'],
                emergency_contact_person=request.POST['member6_emergency_contact_person'],
                emergency_contact_number=request.POST['member6_emergency_contact_number'],
                photo=request.FILES['member6_photo'],
                id_proof=request.FILES['member6_id_proof'],
                id_proof_again=request.FILES['member6_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member7_name'],
                father_name=request.POST['member7_father_name'],
                date_of_birth=request.POST['member7_date_of_birth'],
                email=request.POST['member7_email'],
                contact_number=request.POST['member7_contact_number'],
                address=request.POST['member7_address'],
                emergency_contact_person=request.POST['member7_emergency_contact_person'],
                emergency_contact_number=request.POST['member7_emergency_contact_number'],
                photo=request.FILES['member7_photo'],
                id_proof=request.FILES['member7_id_proof'],
                id_proof_again=request.FILES['member7_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member8_name'],
                father_name=request.POST['member8_father_name'],
                date_of_birth=request.POST['member8_date_of_birth'],
                email=request.POST['member8_email'],
                contact_number=request.POST['member8_contact_number'],
                address=request.POST['member8_address'],
                emergency_contact_person=request.POST['member8_emergency_contact_person'],
                emergency_contact_number=request.POST['member8_emergency_contact_number'],
                photo=request.FILES['member8_photo'],
                id_proof=request.FILES['member8_id_proof'],
                id_proof_again=request.FILES['member8_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member9_name'],
                father_name=request.POST['member9_father_name'],
                date_of_birth=request.POST['member9_date_of_birth'],
                email=request.POST['member9_email'],
                contact_number=request.POST['member9_contact_number'],
                address=request.POST['member9_address'],
                emergency_contact_person=request.POST['member9_emergency_contact_person'],
                emergency_contact_number=request.POST['member9_emergency_contact_number'],
                photo=request.FILES['member9_photo'],
                id_proof=request.FILES['member9_id_proof'],
                id_proof_again=request.FILES['member9_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member10_name'],
                father_name=request.POST['member10_father_name'],
                date_of_birth=request.POST['member10_date_of_birth'],
                email=request.POST['member10_email'],
                contact_number=request.POST['member10_contact_number'],
                address=request.POST['member10_address'],
                emergency_contact_person=request.POST['member10_emergency_contact_person'],
                emergency_contact_number=request.POST['member10_emergency_contact_number'],
                photo=request.FILES['member10_photo'],
                id_proof=request.FILES['member10_id_proof'],
                id_proof_again=request.FILES['member10_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member11_name'],
                father_name=request.POST['member11_father_name'],
                date_of_birth=request.POST['member11_date_of_birth'],
                email=request.POST['member11_email'],
                contact_number=request.POST['member11_contact_number'],
                address=request.POST['member11_address'],
                emergency_contact_person=request.POST['member11_emergency_contact_person'],
                emergency_contact_number=request.POST['member11_emergency_contact_number'],
                photo=request.FILES['member11_photo'],
                id_proof=request.FILES['member11_id_proof'],
                id_proof_again=request.FILES['member11_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member12_name'],
                father_name=request.POST['member12_father_name'],
                date_of_birth=request.POST['member12_date_of_birth'],
                email=request.POST['member12_email'],
                contact_number=request.POST['member12_contact_number'],
                address=request.POST['member12_address'],
                emergency_contact_person=request.POST['member12_emergency_contact_person'],
                emergency_contact_number=request.POST['member12_emergency_contact_number'],
                photo=request.FILES['member12_photo'],
                id_proof=request.FILES['member12_id_proof'],
                id_proof_again=request.FILES['member12_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member13_name'],
                father_name=request.POST['member13_father_name'],
                date_of_birth=request.POST['member13_date_of_birth'],
                email=request.POST['member13_email'],
                contact_number=request.POST['member13_contact_number'],
                address=request.POST['member13_address'],
                emergency_contact_person=request.POST['member13_emergency_contact_person'],
                emergency_contact_number=request.POST['member13_emergency_contact_number'],
                photo=request.FILES['member13_photo'],
                id_proof=request.FILES['member13_id_proof'],
                id_proof_again=request.FILES['member13_id_proof_again']
            )
            messages.success(request,'Registered Successfully')
            return redirect('/')
    else:
        package_choices = Team.PACKAGE
        return render(request, 'option14.html',{'package_choices': package_choices})

def option15(request):
    if request.method == 'POST':
        if 'submit' in request.POST:
            package_str = ", ".join(request.POST.getlist('package'))
            team = Team.objects.create(
                island = request.POST['island'],
                leader_name = request.POST['leader_name'],
                leader_father_name = request.POST['leader_father_name'],
                leader_contact_number=request.POST['leader_contact_number'],
                leader_date_of_birth=request.POST['leader_date_of_birth'],
                leader_email=request.POST['leader_email'],
                leader_address=request.POST['leader_address'],
                leader_emergency_contact_person= request.POST['leader_emergency_contact_person'],
                leader_emergency_contact_number=request.POST['leader_emergency_contact_number'],
                leader_photo=request.FILES['leader_photo'],
                leader_id_adhaar = request.FILES['leader_id_adhaar'],
                leader_id_PCC = request.FILES['leader_id_PCC'],
                checkin=request.POST['checkin'],        
                checkout=request.POST['checkout'],
                number_of_rooms=request.POST['number_of_rooms'],
                ac_or_nonac=request.POST['ac_or_nonac'],
                veg_or_nonveg=request.POST['veg_or_nonveg'],    
                package=package_str        
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member_name'],
                father_name=request.POST['member_father_name'],
                date_of_birth=request.POST['member_date_of_birth'],
                email=request.POST['member_email'],
                contact_number=request.POST['member_contact_number'],
                address=request.POST['member_address'],
                emergency_contact_person=request.POST['member_emergency_contact_person'],
                emergency_contact_number=request.POST['member_emergency_contact_number'],
                photo=request.FILES['member_photo'],
                id_proof=request.FILES['member_id_proof'],
                id_proof_again=request.FILES['member_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member2_name'],
                father_name=request.POST['member2_father_name'],
                date_of_birth=request.POST['member2_date_of_birth'],
                email=request.POST['member2_email'],
                contact_number=request.POST['member2_contact_number'],
                address=request.POST['member2_address'],
                emergency_contact_person=request.POST['member2_emergency_contact_person'],
                emergency_contact_number=request.POST['member2_emergency_contact_number'],
                photo=request.FILES['member2_photo'],
                id_proof=request.FILES['member2_id_proof'],
                id_proof_again=request.FILES['member2_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member3_name'],
                father_name=request.POST['member3_father_name'],
                date_of_birth=request.POST['member3_date_of_birth'],
                email=request.POST['member3_email'],
                contact_number=request.POST['member3_contact_number'],
                address=request.POST['member2_address'],
                emergency_contact_person=request.POST['member3_emergency_contact_person'],
                emergency_contact_number=request.POST['member3_emergency_contact_number'],
                photo=request.FILES['member3_photo'],
                id_proof=request.FILES['member3_id_proof'],
                id_proof_again=request.FILES['member3_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member4_name'],
                father_name=request.POST['member4_father_name'],
                date_of_birth=request.POST['member4_date_of_birth'],
                email=request.POST['member4_email'],
                contact_number=request.POST['member4_contact_number'],
                address=request.POST['member4_address'],
                emergency_contact_person=request.POST['member4_emergency_contact_person'],
                emergency_contact_number=request.POST['member4_emergency_contact_number'],
                photo=request.FILES['member4_photo'],
                id_proof=request.FILES['member4_id_proof'],
                id_proof_again=request.FILES['member4_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member5_name'],
                father_name=request.POST['member5_father_name'],
                date_of_birth=request.POST['member5_date_of_birth'],
                email=request.POST['member5_email'],
                contact_number=request.POST['member5_contact_number'],
                address=request.POST['member5_address'],
                emergency_contact_person=request.POST['member5_emergency_contact_person'],
                emergency_contact_number=request.POST['member5_emergency_contact_number'],
                photo=request.FILES['member5_photo'],
                id_proof=request.FILES['member5_id_proof'],
                id_proof_again=request.FILES['member5_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member6_name'],
                father_name=request.POST['member6_father_name'],
                date_of_birth=request.POST['member6_date_of_birth'],
                email=request.POST['member6_email'],
                contact_number=request.POST['member5_contact_number'],
                address=request.POST['member6_address'],
                emergency_contact_person=request.POST['member6_emergency_contact_person'],
                emergency_contact_number=request.POST['member6_emergency_contact_number'],
                photo=request.FILES['member6_photo'],
                id_proof=request.FILES['member6_id_proof'],
                id_proof_again=request.FILES['member6_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member7_name'],
                father_name=request.POST['member7_father_name'],
                date_of_birth=request.POST['member7_date_of_birth'],
                email=request.POST['member7_email'],
                contact_number=request.POST['member7_contact_number'],
                address=request.POST['member7_address'],
                emergency_contact_person=request.POST['member7_emergency_contact_person'],
                emergency_contact_number=request.POST['member7_emergency_contact_number'],
                photo=request.FILES['member7_photo'],
                id_proof=request.FILES['member7_id_proof'],
                id_proof_again=request.FILES['member7_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member8_name'],
                father_name=request.POST['member8_father_name'],
                date_of_birth=request.POST['member8_date_of_birth'],
                email=request.POST['member8_email'],
                contact_number=request.POST['member8_contact_number'],
                address=request.POST['member8_address'],
                emergency_contact_person=request.POST['member8_emergency_contact_person'],
                emergency_contact_number=request.POST['member8_emergency_contact_number'],
                photo=request.FILES['member8_photo'],
                id_proof=request.FILES['member8_id_proof'],
                id_proof_again=request.FILES['member8_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member9_name'],
                father_name=request.POST['member9_father_name'],
                date_of_birth=request.POST['member9_date_of_birth'],
                email=request.POST['member9_email'],
                contact_number=request.POST['member9_contact_number'],
                address=request.POST['member9_address'],
                emergency_contact_person=request.POST['member9_emergency_contact_person'],
                emergency_contact_number=request.POST['member9_emergency_contact_number'],
                photo=request.FILES['member9_photo'],
                id_proof=request.FILES['member9_id_proof'],
                id_proof_again=request.FILES['member9_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member10_name'],
                father_name=request.POST['member10_father_name'],
                date_of_birth=request.POST['member10_date_of_birth'],
                email=request.POST['member10_email'],
                contact_number=request.POST['member10_contact_number'],
                address=request.POST['member10_address'],
                emergency_contact_person=request.POST['member10_emergency_contact_person'],
                emergency_contact_number=request.POST['member10_emergency_contact_number'],
                photo=request.FILES['member10_photo'],
                id_proof=request.FILES['member10_id_proof'],
                id_proof_again=request.FILES['member10_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member11_name'],
                father_name=request.POST['member11_father_name'],
                date_of_birth=request.POST['member11_date_of_birth'],
                email=request.POST['member11_email'],
                contact_number=request.POST['member11_contact_number'],
                address=request.POST['member11_address'],
                emergency_contact_person=request.POST['member11_emergency_contact_person'],
                emergency_contact_number=request.POST['member11_emergency_contact_number'],
                photo=request.FILES['member11_photo'],
                id_proof=request.FILES['member11_id_proof'],
                id_proof_again=request.FILES['member11_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member12_name'],
                father_name=request.POST['member12_father_name'],
                date_of_birth=request.POST['member12_date_of_birth'],
                email=request.POST['member12_email'],
                contact_number=request.POST['member12_contact_number'],
                address=request.POST['member12_address'],
                emergency_contact_person=request.POST['member12_emergency_contact_person'],
                emergency_contact_number=request.POST['member12_emergency_contact_number'],
                photo=request.FILES['member12_photo'],
                id_proof=request.FILES['member12_id_proof'],
                id_proof_again=request.FILES['member12_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member13_name'],
                father_name=request.POST['member13_father_name'],
                date_of_birth=request.POST['member13_date_of_birth'],
                email=request.POST['member13_email'],
                contact_number=request.POST['member13_contact_number'],
                address=request.POST['member13_address'],
                emergency_contact_person=request.POST['member13_emergency_contact_person'],
                emergency_contact_number=request.POST['member13_emergency_contact_number'],
                photo=request.FILES['member13_photo'],
                id_proof=request.FILES['member13_id_proof'],
                id_proof_again=request.FILES['member13_id_proof_again']
            )
            TeamMember.objects.create(
                team=team,
                name=request.POST['member14_name'],
                father_name=request.POST['member14_father_name'],
                date_of_birth=request.POST['member14_date_of_birth'],
                email=request.POST['member14_email'],
                contact_number=request.POST['member14_contact_number'],
                address=request.POST['member14_address'],
                emergency_contact_person=request.POST['member14_emergency_contact_person'],
                emergency_contact_number=request.POST['member14_emergency_contact_number'],
                photo=request.FILES['member14_photo'],
                id_proof=request.FILES['member14_id_proof'],
                id_proof_again=request.FILES['member14_id_proof_again']
            )
            messages.success(request,'Registered Successfully')
            return redirect('/')
    else:
        package_choices = Team.PACKAGE
        return render(request, 'option15.html',{'package_choices': package_choices})
# End Multiuser