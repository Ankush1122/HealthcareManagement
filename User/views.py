from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .models import User
from .models import Patient, Doctor, Nurse, Pharmacist, Pathologist, Admin, InsuranceCompany, LawEnforcementAgency, Hospital
from django.shortcuts import HttpResponse
import json

def home(request):
    if(request.session.get('username') is not None):
        temp = "Home Page - Logged in as ", request.session.get("username")
        return HttpResponse(temp)
    return HttpResponse("Home Page - Login to Continue")

def login_signup(request):
    if(request.session.get('username') is not None):
        return redirect('home')
    
    if request.method == 'POST':
        form_id = request.POST.get('form_id')
        print(form_id)
        if form_id == "loginForm":
            username = request.POST['username']
            password = request.POST['password']
            user = User.objects.filter(username=username, password=password)
            # authenticate
            if user.count() >= 1:
                if not user[0].verified:
                    context = {
                        'warning': "User not verified."
                    }
                    return render(request, 'User/login.html', context)
                
                request.session['username'] = username
                return redirect('home')
            else:
                context = {
                    'warning': "Invalid username or password."
                }
                return render(request, 'User/login.html', context)

        elif form_id == "signupForm":
            first_name = request.POST['firstName']
            last_name = request.POST['lastName']
            username = request.POST['signupUsername']
            email = request.POST['email']
            role = request.POST['role']
            password = request.POST['signupPassword']
            confirm_password = request.POST['confirmPassword']

            if password != confirm_password:
                print("Error")
                context = {
                    'warning': "Passwords do not match."
                }
                return render(request, 'User/login.html', context)

            if User.objects.filter(username=username).exists():
                context = {
                    'warning': "Username is already taken."
                }
                return render(request, 'User/login.html', context)
            
            if User.objects.filter(email=email).exists():
                context = {
                    'warning': "Email is already taken."
                }
                return render(request, 'User/login.html', context)

            user = User.objects.create(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
            user.role = role
            user.verified = False
            user.save()

            # Create user-specific models based on the role
            if role == 'Patient':
                patient = Patient.objects.create(user=user)
                request.session["patient_id"] = patient.patient_id
                return redirect('complete_profile_patient')
            elif role == 'Doctor':
                doctor = Doctor.objects.create(user=user)
                request.session["doctor_id"] = doctor.doctor_id
                return redirect('complete_profile_doctor')
            elif role == 'Nurse':
                nurse = Nurse.objects.create(user=user)
                request.session["nurse_id"] = nurse.nurse_id
                return redirect('complete_profile_nurse')
            elif role == 'Pharmacist':
                pharmacist = Pharmacist.objects.create(user=user)
                request.session["pharmacist_id"] = pharmacist.pharmacist_id
                return redirect('complete_profile_pharmacist')
            elif role == 'Pathologist':
                pathologist = Pathologist.objects.create(user=user)
                request.session["pathologist_id"] = pathologist.pathologist_id
                return redirect('complete_profile_pathologist')
            elif role == 'Admin':
                admin = Admin.objects.create(user=user)
                request.session["admin_id"] = admin.admin_id
                return redirect('complete_profile_admin')
            elif role == 'InsuranceAgent':
                insuranceCompany = InsuranceCompany.objects.create(user=user)
                request.session["insurance_agent_id"] = insuranceCompany.insurance_company_id
                return redirect('complete_profile_insurance')
            elif role == 'LawEnforcementAgent':
                lawEnforcement = LawEnforcementAgency.objects.create(user=user)
                request.session["lawEnforcement_agent_id"] = lawEnforcement.agency_id
                return redirect('complete_profile_law_enforcement')
            elif role == 'Hospital':
                hospital = Hospital.objects.create(user=user)
                hospital.name = user.first_name + user.last_name
                hospital.save()
                request.session["hospital_id"] = hospital.hospital_id
                return redirect('complete_profile_hospital')

            context = {
                'success': "Signup successful. You can now log in."
            }
            return render(request, 'User/login.html', context)

    return render(request, 'User/login.html')

def complete_profile_admin(request):
    if(request.session.get("admin_id") is None):
        return HttpResponse("Invalid Request")
    
    if(request.method == "POST"):
        admin = Admin.objects.get(admin_id=request.session["admin_id"])
        admin.admin_details = request.POST['adminDetails']
        admin.save()
        del request.session["admin_id"]
        return redirect('home')
    
    return render(request, 'User/admin_first_login.html')
 
def complete_profile_doctor(request):
    if(request.session.get("doctor_id") is None):
        return HttpResponse("Invalid Request")
    
    if(request.method == "POST"):
        doctor = Doctor.objects.get(doctor_id=request.session["doctor_id"])
        specialization = request.POST['specialization']
        licenseNumber = request.POST['licenseNumber']
        hospitalID = request.POST['hospitalId']
        doctor.specialization = specialization
        doctor.license_number = licenseNumber
        doctor.specialization = specialization
        doctor.hospital = Hospital.objects.get(hospital_id=hospitalID)
        doctor.save()
        del request.session["doctor_id"]
        return redirect('home')
    
    hospitals = Hospital.objects.all().values('hospital_id', 'name')
    hospital_list = list(hospitals)    
    return render(request, 'User/doctor_first_login.html', {'hospitals_json': json.dumps(hospital_list)})

def complete_profile_hospital(request):
    if(request.session.get("hospital_id") is None):
        return HttpResponse("Invalid Request")
    
    if(request.method == "POST"):
        hospital = Hospital.objects.get(hospital_id=request.session["hospital_id"])
        hospital.address = request.POST['address']
        hospital.contact_number = request.POST['contactNumber']
        hospital.save()
        del request.session["hospital_id"]
        return redirect('home')

    return render(request, 'User/hospital_first_login.html')

def complete_profile_insurance(request):
    if(request.session.get("insurance_agent_id") is None):
        return HttpResponse("Invalid Request")
    
    if(request.method == "POST"):
        insurance_agent = InsuranceCompany.objects.get(insurance_company_id=request.session["insurance_agent_id"])
        insurance_agent.name = request.POST['agencyName']
        insurance_agent.address = request.POST['address']
        insurance_agent.contact_number = request.POST['contactNumber']
        insurance_agent.save()
        del request.session["insurance_agent_id"]
        return redirect('home')
    
    return render(request, 'User/insurance_first_login.html')

def complete_profile_law_enforcement(request):
    if(request.session.get("lawEnforcement_agent_id") is None):
        return HttpResponse("Invalid Request")
    
    if(request.method == "POST"):
        law_enforcement_agency = LawEnforcementAgency.objects.get(agency_id=request.session["lawEnforcement_agent_id"])
        law_enforcement_agency.name = request.POST['agencyName']
        law_enforcement_agency.address = request.POST['address']
        law_enforcement_agency.contact_number = request.POST['contactNumber']
        law_enforcement_agency.save()
        del request.session["lawEnforcement_agent_id"]
        return redirect('home')
    
    return render(request, 'User/law_enforcement_first_login.html')

def complete_profile_nurse(request):
    if(request.session.get("nurse_id") is None):
        return HttpResponse("Invalid Request")
    
    hospitals = Hospital.objects.all().values('hospital_id', 'name')
    hospital_list = list(hospitals)
    
    if(request.method == "POST"):
        nurse = Nurse.objects.get(nurse_id=request.session["nurse_id"])
        doctorId = request.POST['doctorId']
        hospitalID = request.POST['hospitalId']
        if((not doctorId.isnumeric()) or  Doctor.objects.filter(doctor_id=doctorId).count() == 0):
            context = {
                'warning': "Invalid Doctor ID, try again.",
                'hospitals_json': json.dumps(hospital_list)
            }
            return render(request, 'User/nurse_first_login.html', context)

        nurse.supervising_doctor = Doctor.objects.get(doctor_id = doctorId)
        nurse.hospital = Hospital.objects.get(hospital_id=hospitalID)
        nurse.save()
        del request.session["nurse_id"]
        return redirect('home')
    

    return render(request, 'User/nurse_first_login.html', {'hospitals_json': json.dumps(hospital_list)})

def complete_profile_pathologist(request):
    if(request.session.get("pathologist_id") is None):
        return HttpResponse("Invalid Request")
    
    hospitals = Hospital.objects.all().values('hospital_id', 'name')
    hospital_list = list(hospitals)
    
    if(request.method == "POST"):
        pathologist = Pathologist.objects.get(pathologist_id=request.session["pathologist_id"])
        hospitalID = request.POST['hospitalId']
        pathologist.hospital = Hospital.objects.get(hospital_id=hospitalID)
        pathologist.save()
        del request.session["pathologist_id"]
        return redirect('home')
    

    return render(request, 'User/pathologist_first_login.html', {'hospitals_json': json.dumps(hospital_list)})

def complete_profile_patient(request):
    if(request.session.get("patient_id") is None):
        return HttpResponse("Invalid Request")
    
    if(request.method == "POST"):
        patient = Patient.objects.get(patient_id=request.session["patient_id"])
        patient.date_of_birth = request.POST['dob']
        patient.gender = request.POST['gender']
        patient.address = request.POST['address']
        patient.contact_number = request.POST['contactNumber']
        patient.insurance_policy_number = request.POST['insurancePolicyNumber']

        patient.save()
        del request.session["patient_id"]
        return redirect('home')
    
    return render(request, 'User/patient_first_login.html')

def complete_profile_pharmacist(request):
    if(request.session.get("pharmacist_id") is None):
        return HttpResponse("Invalid Request")
    
    if(request.method == "POST"):
        pharmacist = Pharmacist.objects.get(pharmacist_id=request.session["pharmacist_id"])
        hospitalID = request.POST['hospitalId']
        pharmacist.hospital = Hospital.objects.get(hospital_id=hospitalID)
        pharmacist.save()
        del request.session["pharmacist_id"]
        return redirect('home')
    
    hospitals = Hospital.objects.all().values('hospital_id', 'name')
    hospital_list = list(hospitals)
    return render(request, 'User/pharmacist_first_login.html', {'hospitals_json': json.dumps(hospital_list)})
 
def logout(request):
    del request.session["username"]
    return redirect('home')
