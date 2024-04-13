from django import forms

from admins.models import Account


class UnitForm(forms.ModelForm):
    class Meta:
        model=Account
        fields = ['username','name','cluster','zone','phone','password']

class ClusterForm(forms.ModelForm):
    class Meta:
        model=Account
        fields = ['username','name','zone','phone','password']

class ZoneForm(forms.ModelForm):
    class Meta:
        model=Account
        fields = ['username','name','phone','password']

class CentreForm(forms.ModelForm):
    class Meta:
        model=Account
        fields = ['username','name','phone','password']