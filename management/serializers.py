from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Student_database,ICS,subjects,Engineering,Medical,ICom,Arts,Seience,UserAuth

class Student_databaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_database
        fields = '__all__'
class UserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAuth
        fields = '__all__'
class subjectsSerializer(serializers.ModelSerializer):

    class Meta:
        model = subjects
        fields = '__all__'

class icsSerializer(serializers.ModelSerializer):
    child=Student_databaseSerializer()
    auth=UserAuthSerializer()
    subjects_set = subjectsSerializer(many=True, read_only=True)

    class Meta:
        model = ICS
        fields = '__all__'

class EngineeringSerializer(serializers.ModelSerializer):
    child=Student_databaseSerializer()
    class Meta:
        model = Engineering
        fields = '__all__'
class MedicalSerializer(serializers.ModelSerializer):
    child=Student_databaseSerializer()
    class Meta:
        model = Medical
        fields = '__all__'
class IComSerializer(serializers.ModelSerializer):
    child=Student_databaseSerializer()
    class Meta:
        model = ICom
        fields = '__all__'
class ArtsSerializer(serializers.ModelSerializer):
    child=Student_databaseSerializer()
    class Meta:
        model = Arts
        fields = '__all__'
class SeienceSerializer(serializers.ModelSerializer):
    child=Student_databaseSerializer()
    class Meta:
        model = Seience
        fields = '__all__'
