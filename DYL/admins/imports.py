import datetime
import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.utils.crypto import get_random_string

from admins.forms import UnitForm, ClusterForm, ZoneForm, CentreForm
from admins.models import Account
from msg.views import SmsSent
from users.forms import PatientForm, ApproveForm, RelationForm, MarkForm, MedicalForm, MedicineApproveForm, MarkMedForm
from users.models import patient, approved, centre, medicine


