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
from . models import *
# from .forms import TeamForm

def demo(request):
    hotels = HotelManage.objects.all()
    return render(request, 'applicantprofile.html', {'hotels':hotels})

# ==========Main Page==========
@login_required(login_url='login')
def dashboard(request):
    island_choices = Team.ISLAND
    selected_island = request.POST.get('island')
    if selected_island:
        leader = Team.objects.filter(island=selected_island)
    else:
        leader = Team.objects.all()
    context = {
        'leader':leader,
        'island_choices':island_choices,
        'selected_island':selected_island,
    }
    return render(request, 'admin.html',context)
# ========== END FUNCTION  ==========

# ========== ROOM AND PERMIT FUNCTION==========
# @login_required(login_url='login')
# def team_edit(request, team_id):
    # team = get_object_or_404(Team, pk=team_id)


    # if request.method == 'POST':
        
    #     room_id = request.POST['room_name']
    #     room = HotelManage.objects.get(pk=room_id)
    #     team.room_name = room
    #     team.save()
    #     messages.success(request, "Room  Updated")

    # return render(request, 'applicantprofile.html', {'team': team,'hotels':hotels})
    # pass
# ========== END FUNCTION  ==========


# ========== TEAM DETAIL ==========
@login_required(login_url='login')
def leader_member(request,team_id):
    team = get_object_or_404(Team, id=team_id)
    team_members = TeamMember.objects.filter(team=team)

    hotels = HotelManage.objects.all()
    if request.method == 'POST':

        team.admin_checkin = request.POST['admin_checkin']
        team.admin_checkout = request.POST['admin_checkout']
        team.admin_number_of_rooms = request.POST['admin_number_of_rooms']

        room_id = request.POST['room_name']
        room = HotelManage.objects.get(pk=room_id)
        team.room_name = room
        team.save()
    context = {
        'team': team,
        'team_members': team_members,
        'hotels':hotels,
        'team': team
    }
    return render(request, 'applicantprofile.html',context)
# ========== END FUNCTION  ==========

# ========== NEW DASHBOARD + DELETE USER ==========

# ========== END FUNCTION  ==========

# ====================================== MAIN BUTTONS IN DETAIL PAGE ===========================================
# ==========OLD Status Function==========
@login_required(login_url='login')
def adminstatus(request,pk):
    # team = get_object_or_404(Team, pk=pk)
    # if request.method == 'POST':
    #     status = request.POST.get('status')
    #     if status != team.status:
    #         if Team.objects.filter(status=status):
    #             team.status = status
    #             team.save()
    #         messages.success(request, 'You have updated the status ')
    # context = {'team': team}
    # return render(request, 'applicantprofile.html',context)
    pass
# ========== END FUNCTION  ==========
# ==========New   Function==========
@login_required(login_url='login')
def statusur(request,status_id):
    team = get_object_or_404(Team, pk=status_id)
    if request.method == 'POST':
        team.status = request.POST['status']
        team.save()
        messages.success(request, "status  Updated")
    return render(request, 'applicantprofile.html',{'team':team})
# ========== END FUNCTION  ==========

# ====================================== END FUNCTION ===========================================

# ========== DOWNLOAD LEADER PDF==========
@login_required(login_url='login')
def download_file(request, team_id, field_name):
    team = get_object_or_404(Team, id=team_id)
    file_field = getattr(team, field_name)
    if file_field:
        response = FileResponse(file_field)
        response['Content-Disposition'] = f'attachment; filename="{file_field.name}"'
        return response
    else:
        messages.warning(request, f"No file found for {field_name}.")
    return redirect('/')
# ========== END FUNCTION  ==========

# ========== TEAM MEMBER DETAILS  ==========
@login_required(login_url='login')
def download_member_file(request, team_id, member_id, field_name):
    team_member = get_object_or_404(TeamMember, id=member_id, team__id=team_id)
    file_field = getattr(team_member, field_name)
    if file_field:
        response = FileResponse(file_field)
        response['Content-Disposition'] = f'attachment; filename="{file_field.name}"'
        return response
    else:
        messages.warning(request, f"No file found for {field_name}.")
    return redirect('/')
# ========== END FUNCTION  ==========

# ========== SEARCH + AJAX ==========
@csrf_exempt
def search_leaders(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query')
        leaders = Leader.objects.filter(name__icontains=search_query)
        leaders_list = []
        for leader in leaders:
            leaders_list.append({
                'id': leader.id,
                'name': leader.name,
                'contact': leader.contact,
                'package': leader.package,
                'status': leader.status,
                'details_url': f"/leader/{leader.id}"
            })
        return JsonResponse({'leaders': leaders_list})
    else:
        return render(request, 'admin.html')
# ========== END FUNCTION  ==========
# =================PERMIT =============================
def permitkavarathi(request,permit_id):
    team = get_object_or_404(Team,pk=permit_id)
    if request.method == 'POST':
        team.permit = request.POST['permit']
        team.save()
        messages.success(request, "Permit Updated")
    return render(request, 'applicantprofile.html',{'team':team})
# =====================ENDPERMIT==================
# ====================================== ACCOUNT ===========================================
# ========== LOGIN  ==========
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request,"You are Login")
            return redirect('dashboard')
        else:
            error_message = "!!Username Or Password Incorrect"
            return redirect('login')
    else:
        return render(request,'login.html')
# ========== END FUNCTION  ==========

# ========== REGISTER  ==========
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                error_message="username taken"
            elif User.objects.filter(password=confirm_password).exists():
                error_message="Passwored taken"
            else:
                user = User.objects.create_user(username=username, password=confirm_password)
                user.save()
                return redirect('dashboard') 
        else:
            error_message = "Opps!!! Passwords Do Not Match.."
    else:
        error_message = ""
    return render(request,'register.html',{'error_message':error_message})
# ========== END FUNCTION  ==========

# ========== LOGOUT  ==========
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')
# ========== END FUNCTION  ==========
# ====================================== END ACCOUNT ===========================================

def input_balance(request,balance_id):
    team = get_object_or_404(Team,pk=balance_id)
    if request.method == 'POST':
        team.packagerate = request.POST['packagerate']
        team.advanced = request.POST['advanced']
        team.balance = request.POST['balance']
        
        team.save()
    return render(request, 'applicantprofile.html',{'team': team})

def todo(request,todo_id):
    team = get_object_or_404(Team,pk=todo_id)
    if request.method == 'POST':
        team.todo  = request.POST['todo']
        team.save()
    return render(request, 'applicantprofile.html',{'team': team})
    
# --------------------------INVOICE---------------------------
def invoice(request):
    return render(request,'invoice.html')
# ------------------------------END----------------------------

def pdf_invoice(request):
    checkin_str = ''
    checkout_str = ''
    today_str = ''

    if request.method == 'POST':
        name = request.POST['name']
        contact = request.POST['contact']
        numberofguest = request.POST['numberofguest']
        rooms = request.POST['rooms']
        checkin_str = request.POST['checkin']
        checkout_str = request.POST['checkout']
        today_str = request.POST['today']
        prepayment = request.POST['prepayment']
        total = request.POST['total']

    checkin = datetime.strptime(checkin_str, '%Y-%m-%d').strftime('%d-%m-%Y')
    checkout = datetime.strptime(checkout_str, '%Y-%m-%d').strftime('%d-%m-%Y')
    today = datetime.strptime(today_str, '%Y-%m-%d').strftime('%d-%m-%Y')

    context = {
        'name':name,
        'contact':contact,
        'numberofguest':numberofguest,
        'rooms':rooms,
        'checkin':checkin,
        'checkout':checkout,
        'prepayment':prepayment,
        'today':today,
        'prepayment':prepayment,
        'total':total,
    }
    return render(request,'pdf_invoice.html',context) if request.method == 'POST' else render(request,'invoice.html')

# ================ROOM CREATE================
def room_c(request):
    if request.method == 'POST':
        hotelname = request.POST['hotelname']
        hotelname = HotelManage.objects.create(hotelname = hotelname)
        hotelname.save()
        return redirect('room_c')
    else:
        return render(request,'room/room_c.html')

def room_rdu(request):
    room_details = HotelManage.objects.all()
    return render(request,'room/room_rdu.html',{'room_details':room_details})

def room_delete(request,id):
    room_delete = get_object_or_404(HotelManage, id=id)
    if request.method == 'POST':
        room_delete.delete()
        return redirect('room_rdu')       
    return redirect('room_rdu')

def room_update(request,id):
    room_update = get_object_or_404(HotelManage,id=id)
    if request.method == 'POST':
        hotelname = request.POST['hotelname']
        room_update.hotelname = hotelname
        room_update.save()
        return redirect('room_rdu')
    return render(request,'room/update_room_name.html',{'room_update':room_update})

# ==============INVOICE============
@login_required(login_url='login')
def leader_all_data(request):
    allinvoicedata = Invoice.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        package = request.POST.get('package')
        package_rate = request.POST.get('package_rate')
        arrival_date = request.POST.get('arrival_date')
        departure_date = request.POST.get('departure_date')
        today_date = request.POST.get('today_date')
        prepayment = request.POST.get('prepayment')
        total = request.POST.get('total')

        reservation = Invoice(
            name=name,
            phone=phone,
            email=email,
            package=package,
            arrival_date=arrival_date,
            departure_date=departure_date,
            today_date=today_date,
            package_rate=package_rate,
            prepayment=prepayment,
            total=total
        )
        reservation.save()
        return redirect('leader_all_data')

    return render(request,'leader_all_data.html',{'allinvoicedata':allinvoicedata})

def invoice_download(request,pk):
    invoice_download = Invoice.objects.get(id=pk)
    return render(request,'invoice/pdf.html',{'invoice_download':invoice_download})

def invoice_delete(request,id):
    invoice_delete = get_object_or_404(Invoice,id=id)
    if request.method == 'POST':
        invoice_delete.delete()
        return redirect('leader_all_data')
    return redirect('leader_all_data')