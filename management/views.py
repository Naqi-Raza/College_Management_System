from .serializers import subjectsSerializer
from django.shortcuts import render,get_object_or_404
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
# Create your views here.
def Home(request):
    return render(request, 'Home.html')
def Department(request):
    return render(request, 'Department.html')

def login(request):
    return render(request, 'Login.html')

def navbar(request):
    return render(request, 'navbar.html')
def Admission_form(request):
    return render(request, 'Admission_form.html')
def Submit_admission_form(request):
    if request.method == 'POST':
        fst_name=request.POST.get('first_name')
        lst_name=request.POST.get('last_name')
        father_name=request.POST.get('father_name')
        student_cnic=request.POST.get('student_cnic')
        father_cnic=request.POST.get('father_cnic')
        address=request.POST.get('address')
        previous_qualification=request.POST.get('previous_degree')
        total_marks=request.POST.get('total_marks')
        obtained_marks=request.POST.get('obtained_marks')
        percentage=request.POST.get('percentage')
        previous_institute=request.POST.get('institution_name')
        selected_program=request.POST.get('selected_program')
        print(father_name)
        print(selected_program)
        student=Student_database.objects.create(First_name=fst_name, Last_name=lst_name, Father_name=father_name, Student_cnic=student_cnic, Father_cnic=father_cnic, Address=address, Previous_Qualification=previous_qualification, Total_marks=total_marks, Obtained_marks=obtained_marks, Percentage=percentage, previous_institute=previous_institute, selected_program=selected_program)
        if selected_program == "FSc Pre-Engineering":
          Engineering.objects.create(child=student)
        elif selected_program == "FSc Pre-Medical":
          Medical.objects.create(child=student)
        elif selected_program == "ICS":
          ICS.objects.create(child=student)
        elif selected_program == "ICom":
          ICom.objects.create(child=student)
        elif selected_program == "FA (Arts)":
          Arts.objects.create(child=student)
        elif selected_program == "General Science":
          Seience.objects.create(child=student)
        return render(request, 'Home.html')
    
    
def show_department(request):
    return render(request, 'show_department.html')

def show_fsc_eng(request):
    eng_students=Engineering.objects.all()
    result={
      "std_data":eng_students
    }
    print(result)
    return render(request, 'Fsc_Eng.html',result)

def show_ics(request):
    ics_students=ICS.objects.all()
    result={
      "std_data":ics_students
    }
    print(result)
    return render(request, 'Fsc_Eng.html',result)
def show_fsc_med(request):
    med_students=Medical.objects.all()
    result={
      "std_data":med_students
    }
    return render(request, 'Fsc_Eng.html',result)
def show_i_com(request):
    icom_students=ICom.objects.all()
    result={
      "std_data":icom_students
    }
    return render(request, 'Fsc_Eng.html',result)
def show_Arts(request):
    arts_students=Arts.objects.all()
    result={
      "std_data":arts_students
    }
    return render(request, 'Fsc_Eng.html',result)

def show_science(request):
    science_students=Seience.objects.all()
    result={
      "std_data":science_students
    }
    return render(request, 'Fsc_Eng.html',result)

def show_student_dashboard(request):
    return render(request, 'std_dashboard_home.html')

@api_view(['GET'])
def get_ics_students(request):
    ics_students=ICS.objects.all()
    serializer=icsSerializer(ics_students,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_ics_subjects(request, id):
    ics_students=ICS.objects.get(id=id)

    subjects_list = subjects.objects.filter(ics=ics_students).values('subject')

    return Response({
        "student": ics_students.auth.user_id,
        "subjects": list(subjects_list)
    })

def edit_student(request,program,id):
      if program == "ICS":
        data = ICS.objects.filter(id=id)
        serializer = icsSerializer(data,many=True)
        context = {
        'main_data': serializer.data   # this is your dictionary/list
        }
        print(context)
        return render(request, 'std_update.html',context)
      elif program == "FSc Pre-Engineering":
        data = Engineering.objects.filter(id=id)
        serializer = EngineeringSerializer(data,many=True)
        context = {
        'main_data': serializer.data   # this is your dictionary/list
        }
        print(context)
        return render(request, 'std_update.html',context)
      elif program == "FSc Pre-Medical":
        data = Medical.objects.filter(id=id)
        serializer = MedicalSerializer(data,many=True)
        context = {
        'main_data': serializer.data   # this is your dictionary/list
        }
        print(context)
        return render(request, 'std_update.html',context)
      elif program == "ICom":
        data = ICom.objects.filter(id=id)
        serializer = IComSerializer(data,many=True)
        context = {
        'main_data': serializer.data   # this is your dictionary/list
        }
        print(context)
        return render(request, 'std_update.html',context)
      elif program == "FA (Arts)":
        data = Arts.objects.filter(id=id)
        serializer = ArtsSerializer(data,many=True)
        context = {
        'main_data': serializer.data   # this is your dictionary/list
        }
        print(context)
        return render(request, 'std_update.html',context)
      elif program == "General Science":
        data = Seience.objects.filter(id=id)
        serializer = SeienceSerializer(data,many=True)
        context = {
        'main_data': serializer.data   # this is your dictionary/list
        }
        print(context)
        return render(request, 'std_update.html',context)
@api_view(['POST'])
def update_student(request, id):
    student = ICS.objects.get(id=id)

    # 1. Get New Roll No
    new_roll = request.data.get("roll_no")

    # UPDATE AUTH (MASTER)
    student.auth = UserAuth.objects.create(user_id=new_roll)
    student.save()
    # 2. Update Image
    print("FILES:", request.FILES)

    if "image" in request.FILES:
        student.image = request.FILES["image"]
        print("IMAGE RECEIVED")

    student.save()

    # 3. Update Subjects
    subjects.objects.filter(ics=student).delete()

    for sub in request.data.getlist("subjects"):
        subjects.objects.create(ics=student, subject=sub)

    return Response({"message": "Updated Successfully"})

def login_view(request):

    user_id = request.POST.get("user_id")
    password = request.POST.get("password")
    print(user_id)
    print(password)

    try:
        # 1. Auth check
        auth = UserAuth.objects.get(user_id=user_id, password=password)
        print(auth)
        print(ICS.objects.filter(auth=auth).exists())
        # 2. Check department tables

        if ICS.objects.filter(auth=auth).exists():
            data = ICS.objects.get(auth=auth)
            serializer = icsSerializer(data)
            main_data={'std_data':serializer.data}
            print(main_data)
            return render(request, "std_dashboard_home.html",main_data)                   
        
        
        elif Engineering.objects.filter(auth=auth).exists():
            data = Engineering.objects.get(auth=auth)
            eng_students=Engineering.objects.all()
            result={
            "std_data":eng_students
            }
            print(result)
            return render(request, 'Fsc_Eng.html',result)

        elif Medical.objects.filter(auth=auth).exists():
            data = Medical.objects.get(auth=auth)
            med_students=Medical.objects.all()
            result={
            "std_data":med_students
            }
            print(result)
            return render(request, 'Fsc_Eng.html',result)

        else:
            return render(request, 'login.html')

    except:
        return render(request, 'login.html')


def teaching_detail(request):
    return render(request, 'teaching_detail.html')


def teacher_profile(request):
    return render(request, 'teacher_profile.html')
