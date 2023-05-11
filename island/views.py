from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from applicantform. models import*
from django.contrib import messages
from django.http import FileResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

@login_required(login_url='loginagatti')
def agatti(request):
    agatti_ialnad = Team.objects.all()
    return render(request,'adminagatti.html',{'agatti_ialnad':agatti_ialnad})
@login_required(login_url='loginkatmat')
def kadmat(request):
    kadmat_island = Team.objects.all()
    return render(request,'adminkadmat.html',{'kadmat_island':kadmat_island})
@login_required(login_url='loginminicoy')
def minicoy(request):
    minicoy_island = Team.objects.all()
    return render(request,'adminminicoy.html',{'minicoy_island':minicoy_island})
@login_required(login_url='loginkalpeni')
def kalpeni(request):
    kalpeni_island = Team.objects.all()
    return render(request,'adminkalpeni.html',{'kalpeni_island':kalpeni_island})


# ***************** AGATTI DASHBOARD LOOP *****************
@login_required(login_url='loginagatti')
def leader_details(request,team_id):
    team = get_object_or_404(Team, id=team_id)
    team_members = TeamMember.objects.filter(team=team)
    context = {
        'team': team,
        'team_members': team_members,
    }
    return render(request,'applicantprofileisland.html',context)
@login_required(login_url='loginagatti')
def download_agatti(request, team_id, field_name):
    team = get_object_or_404(Team, id=team_id)
    file_field = getattr(team, field_name)
    if file_field:
        response = FileResponse(file_field)
        response['Content-Disposition'] = f'attachment; filename="{file_field.name}"'
        return response
    else:
        messages.warning(request, f"No file found for {field_name}.")
    return redirect('/')
@login_required(login_url='loginagatti')
def download_member_file_agatti(request, team_id, member_id, field_name):
    team_member = get_object_or_404(TeamMember, id=member_id, team__id=team_id)
    file_field = getattr(team_member, field_name)
    if file_field:
        response = FileResponse(file_field)
        response['Content-Disposition'] = f'attachment; filename="{file_field.name}"'
        return response
    else:
        messages.warning(request, f"No file found for {field_name}.")
    return redirect('/')
@login_required(login_url='loginagatti')
def statusagatti(request,status_id):
    team = get_object_or_404(Team, pk=status_id)
    if request.method == 'POST':
        team.status = request.POST['status']
        team.save()
        messages.success(request, "status  Updated")
    return render(request, 'applicantprofileisland.html',{'team':team})
@login_required(login_url='loginagatti')
def room_edit(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    if request.method == 'POST':
        team.admin_checkin = request.POST['admin_checkin']
        team.admin_checkout = request.POST['admin_checkout']
        team.room_name = request.POST['room_name']
        team.admin_number_of_rooms = request.POST['admin_number_of_rooms']
        team.save()
        messages.success(request, "Room  Updated")
    return render(request, 'applicantprofileisland.html', {'team': team})
@login_required(login_url='loginagatti')
def permitagatti(request,permit_id):
    team = get_object_or_404(Team,pk=permit_id)
    if request.method == 'POST':
        team.permit = request.POST['permit']
        team.save()
        messages.success(request, "Permit Updated")
    return render(request, 'applicantprofileisland.html',{'team':team})
def loginagatti(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request,"You are Login")
            return redirect('agatti')
        else:
            error_message = "!!Username Or Password Incorrect"
            return redirect('loginagatti')
    else:
        return render(request,'login.html')
def logoutagatti(request):
    auth.logout(request)
    return redirect('loginagatti')
def input_balance_agatti(request,balance_id):
    team = get_object_or_404(Team,pk=balance_id)
    if request.method == 'POST':
        team.balance = request.POST['balance']
        team.advanced = request.POST['advanced']
        team.save()
    return render(request, 'applicantprofileisland.html', {'team': team})
def todo_agatti(request,todo_id):
    team = get_object_or_404(Team,pk=todo_id)
    if request.method == 'POST':
        team.todo  = request.POST['todo']
        team.save()
    return render(request, 'applicantprofileisland.html', {'team': team})    

def invoice_agatti(request):
    return render(request,'invoice_agatti.html')
# ***************** END FUNCTION *****************
# ******************************** AGATTI DASHBOARD LOOP **************************************
@login_required(login_url='loginkatmat')
def leader_details_kadmat(request,team_id):
    team =  get_object_or_404(Team,id =team_id)
    team_members = TeamMember.objects.filter(team=team)
    context = {'team':team,'team_members':team_members} 
    return render(request, 'applicantprofilekadmat.html',context)
@login_required(login_url='loginkatmat')
def download_kadmat(request,team_id,field_name):
    team = get_object_or_404(Team, id=team_id)
    file_field = getattr(team, field_name)
    if file_field:
        response = FileResponse(file_field)
        response['Content-Disposition'] = f'attachment; filename="{file_field.name}"'
        return response
    else:
        messages.warning(request, f"No file found for {field_name}.")
    return redirect('/')
@login_required(login_url='loginkatmat')
def download_member_file_kadmat(request, team_id, member_id, field_name):
    team_member = get_object_or_404(TeamMember, id=member_id, team__id=team_id)
    file_field = getattr(team_member, field_name)
    if file_field:
        response = FileResponse(file_field)
        response['Content-Disposition'] = f'attachment; filename="{file_field.name}"'
        return response
    else:
        messages.warning(request, f"No file found for {field_name}.")
    return redirect('/')
@login_required(login_url='loginkatmat')
def statuskadmat(request,status_id):
    team = get_object_or_404(Team,pk=status_id)
    if request.method == 'POST':
        team.status = request.POST['status']
        team.save()
        messages.success(request, "status  Updated")
    return render(request, 'applicantprofilekadmat.html',{'team':team})
@login_required(login_url='loginkatmat')
def kadmat_room_edit(request,team_id):
    team = get_object_or_404(Team, pk=team_id)
    if request.method == 'POST':
        team.admin_checkin = request.POST['admin_checkin']
        team.admin_checkout = request.POST['admin_checkout']
        team.room_name = request.POST['room_name']
        team.admin_number_of_rooms = request.POST['admin_number_of_rooms']
        team.save()
        messages.success(request, "Room  Updated")
    return render(request, 'applicantprofilekadmat.html',{'team':team})
@login_required(login_url='loginkatmat')
def permitkadmat(request,permit_id):
    team = get_object_or_404(Team,pk=permit_id)
    if request.method == 'POST':
        team.permit = request.POST['permit']
        team.save()
        messages.success(request, "Permit Updated")
    return render(request, 'applicantprofilekadmat.html',{'team':team})
def loginkatmat(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request,"You are Login")
            return redirect('kadmat')
        else:
            error_message = "!!Username Or Password Incorrect"
            return redirect('loginkatmat')
    else:
        return render(request,'login.html')
def logoutkadmat(request):
    auth.logout(request)
    return redirect('loginkatmat')

def input_balance_kadmat(request,balance_id):
    team = get_object_or_404(Team,pk=balance_id)
    if request.method == 'POST':
        team.balance = request.POST['balance']
        team.advanced = request.POST['advanced']
        team.save()
    return render(request, 'applicantprofilekadmat.html',{'team': team})

def todo_kadmat(request,todo_id):
    team = get_object_or_404(Team,pk=todo_id)
    if request.method == 'POST':
        team.todo  = request.POST['todo']
        team.save()
    return render(request, 'applicantprofilekadmat.html',{'team': team})
def invoice_kadmat(request):
    return render(request,'invoice_kadmat.html')
# ***************** END LOGIN  *****************
# ++++++++++++++++++++++++++++++++++MINICOY++++++++++++++++++++++++++++++++++++
@login_required(login_url='loginminicoy')
def leader_details_mincoy(request,team_id):
    team = get_object_or_404(Team,id=team_id)
    team_members = TeamMember.objects.filter(team = team)
    context = {
        'team':team,
        'team_members':team_members
    }
    return render(request,'applicantprofile_minicoy.html',context)
@login_required(login_url='loginminicoy')
def download_minicoy(request,team_id,field_name):
    team = get_object_or_404(Team, id=team_id)
    file_field = getattr(team, field_name)
    if file_field:
        response = FileResponse(file_field)
        response['Content-Disposition'] = f'attachment; filename="{file_field.name}"'
        return response
    else:
        messages.warning(request, f"No file found for {field_name}.")
    return redirect('/')
@login_required(login_url='loginminicoy')
def download_member_file_minicoy(request, team_id, member_id, field_name):
    team_member = get_object_or_404(TeamMember, id=member_id, team__id=team_id)
    file_field = getattr(team_member, field_name)
    if file_field:
        response = FileResponse(file_field)
        response['Content-Disposition'] = f'attachment; filename="{file_field.name}"'
        return response
    else:
        messages.warning(request, f"No file found for {field_name}.")
    return redirect('/')
@login_required(login_url='loginminicoy')
def statusminicoy(request,status_id):
    team = get_object_or_404(Team, pk=status_id)
    if request.method == 'POST':
        team.status = request.POST['status']
        team.save()
        messages.success(request, "status  Updated")
    return render(request, 'applicantprofile_minicoy.html',{'team':team})
@login_required(login_url='loginminicoy')
def minicoy_room_edit(request,team_id):
    team = get_object_or_404(Team, pk=team_id)
    if request.method == 'POST':
        team.admin_checkin = request.POST['admin_checkin']
        team.admin_checkout = request.POST['admin_checkout']
        team.room_name = request.POST['room_name']
        team.admin_number_of_rooms = request.POST['admin_number_of_rooms']
        team.save()
        messages.success(request, "Room  Updated")
    return render(request, 'applicantprofile_minicoy.html',{'team':team})
@login_required(login_url='loginminicoy')
def permitminicoy(request,permit_id):
    team = get_object_or_404(Team,pk=permit_id)
    if request.method == 'POST':
        team.permit = request.POST['permit']
        team.save()
        messages.success(request, "Permit Updated")
    return render(request, 'applicantprofile_minicoy.html',{'team':team})
def loginminicoy(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request,"You are Login")
            return redirect('minicoy')
        else:
            error_message = "!!Username Or Password Incorrect"
            return redirect('loginminicoy')
    else:
        return render(request,'login.html')
def logoutminicoy(request):
    auth.logout(request)
    return redirect('loginminicoy')

def input_balance_minicoy(request,balance_id):
    team = get_object_or_404(Team,pk=balance_id)
    if request.method == 'POST':
        team.balance = request.POST['balance']
        team.advanced = request.POST['advanced']
        team.save()
    return render(request, 'applicantprofile_minicoy.html',{'team': team})

def todo_minicoy(request,todo_id):
    team = get_object_or_404(Team,pk=todo_id)
    if request.method == 'POST':
        team.todo  = request.POST['todo']
        team.save()
    return render(request, 'applicantprofile_minicoy.html',{'team': team})
def invoice_minicoy(request):
    return render(request,'invoice_minicoy.html')
# ***************** END FUNCTION *****************
# ++++++++++++++++++++++++++++++++++KALPENI++++++++++++++++++++++++++++++++++++
@login_required(login_url='loginkalpeni')
def leader_details_kalpeni(request,team_id):
    team = get_object_or_404(Team,id=team_id)
    team_members = TeamMember.objects.filter(team = team)
    context = {
        'team':team,
        'team_members':team_members
    }
    return render(request,'applicantprofile_kalpeni.html',context)
@login_required(login_url='loginkalpeni')
def download_kalpeni(request,team_id,field_name):
    team = get_object_or_404(Team, id=team_id)
    file_field = getattr(team, field_name)
    if file_field:
        response = FileResponse(file_field)
        response['Content-Disposition'] = f'attachment; filename="{file_field.name}"'
        return response
    else:
        messages.warning(request, f"No file found for {field_name}.")
    return redirect('/')
@login_required(login_url='loginkalpeni')
def download_member_file_kalpeni(request, team_id, member_id, field_name):
    team_member = get_object_or_404(TeamMember, id=member_id, team__id=team_id)
    file_field = getattr(team_member, field_name)
    if file_field:
        response = FileResponse(file_field)
        response['Content-Disposition'] = f'attachment; filename="{file_field.name}"'
        return response
    else:
        messages.warning(request, f"No file found for {field_name}.")
    return redirect('/')
@login_required(login_url='loginkalpeni')
def statuskalpeni(request,status_id):
    team = get_object_or_404(Team, pk=status_id)
    if request.method == 'POST':
        team.status = request.POST['status']
        team.save()
        messages.success(request, "status  Updated")
    return render(request,'applicantprofile_kalpeni.html',{'team':team})
@login_required(login_url='loginkalpeni')
def kalpeni_room_edit(request,team_id):
    team = get_object_or_404(Team, pk=team_id)
    if request.method == 'POST':
        team.admin_checkin = request.POST['admin_checkin']
        team.admin_checkout = request.POST['admin_checkout']
        team.room_name = request.POST['room_name']
        team.admin_number_of_rooms = request.POST['admin_number_of_rooms']
        team.save()
        messages.success(request, "Room  Updated")
    return render(request, 'applicantprofile_kalpeni.html', {'team': team})
@login_required(login_url='loginkalpeni')
def permitkalpeni(request,permit_id):
    team = get_object_or_404(Team,pk=permit_id)
    if request.method == 'POST':
        team.permit = request.POST['permit']
        team.save()
        messages.success(request, "Permit Updated")
    return render(request, 'applicantprofile_kalpeni.html',{'team':team})
@login_required(login_url='loginkalpeni')
def loginkalpeni(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request,"You are Login")
            return redirect('kalpeni')
        else:
            error_message = "!!Username Or Password Incorrect"
            return redirect('loginkalpeni')
    else:
        return render(request,'login.html')
@login_required(login_url='loginkalpeni')
def logoutkalpeni(request):
    auth.logout(request)
    return redirect('loginkalpeni')

def input_balance_kalpeni(request,balance_id):
    team = get_object_or_404(Team,pk=balance_id)
    if request.method == 'POST':
        team.balance = request.POST['balance']
        team.advanced = request.POST['advanced']
        team.save()
    return render(request,'applicantprofile_kalpeni.html',{'team':team})

def todo_kalpeni(request,todo_id):
    team = get_object_or_404(Team,pk=todo_id)
    if request.method == 'POST':
        team.todo  = request.POST['todo']
        team.save()
    return render(request,'applicantprofile_kalpeni.html',{'team':team})
def invoice_kalpeni(request):
    return render(request,'invoice_kalpeni.html')
# ++++++++++++++++++++++++++++++++++++++END++++++++++++++++++++++++++++++++++++++

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ APPLICANT DETAILS $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# $$$$$$$$$$$$$$$$$$$ End Details $$$$$$$$$$$$$$$$$$$