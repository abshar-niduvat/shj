from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=10)
    address = models.TextField(max_length=2000)
    phone = models.CharField(max_length=100)
    nofdyl = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)
    cluster = models.CharField(max_length=100)
    zone = models.CharField(max_length=100)
    applytime = models.DateTimeField()
    formes =models.FileField(upload_to='form/')
    unit_relate = models.CharField(max_length=200, null=True,blank=True)
    unit_approve = models.CharField(max_length=10, default="PENDING")
    unit_time = models.CharField(max_length=100)
    cluster_approve = models.CharField(max_length=10, default="PENDING")
    cluster_time = models.CharField(max_length=100)
    zonal_approve = models.CharField(max_length=10, default="PENDING")
    zonal_time = models.CharField(max_length=100)
    dist_approve = models.CharField(max_length=10, default="PENDING")
    dist_time = models.CharField(max_length=100)
    dist_feedback = models.CharField(max_length=1000, null=True,blank=True)
    dylnumber = models.CharField(max_length=100,unique=True)
    centre = models.CharField(max_length=100)

    def __str__(self):
        return self.dylnumber

class medicine(models.Model):
    unit = models.CharField(max_length=150)
    cluster = models.CharField(max_length=150)
    zone = models.CharField(max_length=150)
    dateofreq = models.DateTimeField(null=True, blank=True)
    p1 = models.CharField(max_length=150)
    a1 = models.CharField(max_length=150)
    h1 =models.CharField(max_length=150)
    p2 = models.CharField(max_length=150, null=True,blank=True)
    a2 =models.CharField(max_length=150, null=True,blank=True)
    h2 =models.CharField(max_length=150, null=True,blank=True)
    p3 = models.CharField(max_length=150, null=True,blank=True)
    a3 =models.CharField(max_length=150, null=True,blank=True)
    h3=models.CharField(max_length=150, null=True,blank=True)
    p4 = models.CharField(max_length=150, null=True, blank=True)
    a4 = models.CharField(max_length=150, null=True, blank=True)
    h4 = models.CharField(max_length=150, null=True, blank=True)
    dist_approve = models.CharField(max_length=150)
    dateofapp = models.DateTimeField(null=True, blank=True)
    dist_approve_by = models.CharField(max_length=150)
    mdcnumber = models.CharField(max_length=150,unique=True)
    otp1 = models.CharField(max_length=150)
    otp2 = models.CharField(max_length=150)
    otp3 = models.CharField(max_length=150)
    otp4 = models.CharField(max_length=150)
    lastdat = models.DateField(null=True, blank=True)
    medrem = models.CharField(max_length=50)
    medshop = models.CharField(max_length=150)

    def __str__(self):
        return self.mdcnumber

class approved(models.Model):
    dylnumber = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=10)
    address = models.TextField(max_length=2000)
    phone = models.CharField(max_length=100)
    startdate = models.DateField()
    upto = models.DateField()
    dylcount = models.CharField(max_length=10)
    dylrem  =   models.CharField(max_length=10)
    otp = models.CharField(max_length=10)
    centre = models.CharField(max_length=100)

    def __str__(self):
        return self.dylnumber
class centre(models.Model):
    dylnumber = models.CharField(max_length=100)
    otp = models.CharField(max_length=100)
    dyldone = models.DateTimeField()
    centre = models.CharField(max_length=100)
    billno = models.CharField(max_length=100, null=True, blank=True)
    amount = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.dylnumber