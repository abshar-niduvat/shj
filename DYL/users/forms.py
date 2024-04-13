from django import forms

from users.models import patient, approved, centre, medicine


class PatientForm(forms.ModelForm):
    class Meta:
        model = patient
        exclude=['applytime','unit_relate','unit_approve','unit_time','cluster','zone','cluster_approve','cluster_time','zonal_approve','zonal_time','dist_approve','dylnumber','dist_time','dist_feedback','centre']

class ApproveForm(forms.ModelForm):
    class Meta:
        model = approved
        exclude =['otp','dylrem','dylnumber','name','age','address','phone']

class RelationForm(forms.ModelForm):
    class Meta:
        model= patient
        fields=['unit_relate']

class MarkForm(forms.ModelForm):
    class Meta:
        model = centre
        fields =['dylnumber','otp']

class MarkMedForm(forms.ModelForm):
    class Meta:
        model = centre
        fields =['dylnumber','otp','amount','billno']

class ViewForm(forms.ModelForm):
    class Meta:
        model = patient
        fields = ['name','phone']

class MedicalForm(forms.ModelForm):
    class Meta:
        model = medicine
        fields = ['p1','p2','p3','p4','a1','a2','a3','a4','h1','h2','h3','h4']
class MedicineApproveForm(forms.ModelForm):
    class Meta:
        model = medicine
        fields = ['medshop','lastdat','medrem']