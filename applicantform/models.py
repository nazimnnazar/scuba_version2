from django.db import models

class HotelManage(models.Model):
    hotelname = models.CharField(max_length=100)
    def __str__(self):
        return '{}'.format(self.hotelname)
    
class Team(models.Model):
    ROOM_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    AC_CHOICES = (
        ('AC', 'AC'),
        ('Non-AC', 'Non-AC'),
    )
    FOOD_CHOICES = (
        ('Veg', 'Veg'),
        ('Non-veg', 'Non-veg'),
    )
    
    PACKAGE=(
        ('Bubble Maker', 'Bubble Maker '),
        ('Seal Team', 'Seal Team'),
        ('Open Water Diver', 'Open Water Diver'),
        ('Adventure Diver','Adventure Diver'),
        ('Advanced Open Water Diver','Advanced Open Water Diver'),
        ('EFR Primary & Secondary Care','EFR Primary & Secondary Care'),
        ('Rescue Diver','Rescue Diver'),
        ('Divemaster','Divemaster'),
        ('Deep Diver','Deep Diver'),
        ('Digital Underwater Photography','Digital Underwater Photography'),
        ('Enriched Air Diver','Enriched Air Diver'),
        ('Night Diver','Night Diver'),
        ('Adaptive Support Diver','Adaptive Support Diver'),
        ('Adaptive Techniques','Adaptive Techniques'),
        ('DSMB Diver','DSMB Diver'),
        ('Emergency Oxygen Provider','Emergency Oxygen Provider'),
        ('Underwater Navigator','Underwater Navigator'),
        ('Wreck Diver','Wreck Diver'),
        ('Peak Performance Buoyancy','Peak Performance Buoyancy'),
        ('Fun Dive Package','Fun Dive Package'),
        ('Fun Dive + Course Package','Fun Dive + Course Package'),
        ('Open Water Dive Course Package','Open Water Dive Course Package'),
        ('Advanced Open Water Diver Course Package','Advanced Open Water Diver Course Package'),
        ('Open & Advanced Open Water Diver Course','Open & Advanced Open Water Diver Course'),
        ('Open Water To Divemaster','Open Water To Divemaster'),
        ('Explore Lakshadweep','Explore Lakshadweep'),
    )
    STATUS = (
        ('Processing','Processing'),
        ('open','open'),
        ('Confirm','Confirm'),
        ('Closed','Closed'),
        ('Completed','Completed'),
    )
    PERMIT =(
        ('Applied','Applied'),
        ('Need to apply','Need to apply'),
        ('Document waiting','Document waiting'),
        ('Permit ready','Permit ready'),
        ('Expired','Expired'),
        ('Without permit','Without permit'),
    )

    ADMIN_ROOM_CHOICES =(
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    ISLAND = (
        ('Kavaratti','Kavaratti'),
        ('Agatti','Agatti'),
        ('Kadmat','Kadmat'),
        ('Minicoy','Minicoy'),
        ('Kalpeni','Kalpeni'),
    )
    island = models.CharField(max_length=240,choices=ISLAND)
    leader_name = models.CharField(max_length=250)
    leader_father_name = models.CharField(max_length=255)
    leader_date_of_birth = models.DateField()
    leader_email = models.EmailField()
    leader_address = models.CharField(max_length=455)
    leader_contact_number = models.CharField(max_length=255)
    leader_emergency_contact_person = models.CharField(max_length=255)
    leader_emergency_contact_number = models.CharField(max_length=25)
    leader_photo = models.FileField(upload_to='photos/',max_length=250,null=True,default=None)
    leader_id_adhaar = models.FileField(upload_to='id_adhaar/',max_length=250,null=True,default=None)
    leader_id_PCC = models.FileField(upload_to='id_pcc/',max_length=250,null=True,default=None)
    checkin = models.DateField(blank=True,null=True)
    checkout = models.DateField(blank=True,null=True)
    number_of_rooms = models.CharField(max_length=10, choices=ROOM_CHOICES)
    ac_or_nonac = models.CharField(max_length=10, choices=AC_CHOICES)
    veg_or_nonveg = models.CharField(max_length=10, choices=FOOD_CHOICES)
    package = models.CharField(max_length=240,choices=PACKAGE)
    status = models.CharField(max_length=100,choices=STATUS, default='Processing')
    permit = models.CharField(max_length=100,choices=PERMIT)
    admin_checkin = models.DateField(blank=True,null=True)
    admin_checkout = models.DateField(blank=True,null=True)
    room_name = models.ForeignKey(HotelManage, on_delete=models.CASCADE,null=True)
    admin_number_of_rooms = models.CharField(max_length=10, choices=ADMIN_ROOM_CHOICES)
    packagerate = models.DecimalField(max_digits=1000000, decimal_places=2,null=True,default=None)
    advanced = models.DecimalField(max_digits=1000000, decimal_places=2,null=True,default=None)
    balance = models.DecimalField(max_digits=1000000, decimal_places=2,null=True,default=None)
    todo = models.CharField(max_length=500)
    def __str__(self):
        return f'Team {self.id} - Leader: {self.leader_name}'
    
class TeamMember(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_members')
    name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField()
    address = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    emergency_contact_person = models.CharField(max_length=255)
    emergency_contact_number = models.CharField(max_length=20)
    photo = models.FileField(upload_to='photos/')
    id_proof = models.FileField(upload_to='id_proofs/')
    id_proof_again = models.FileField(upload_to='id_proofs/')    
    def __str__(self):
        return '{}'.format(self.name)
    
