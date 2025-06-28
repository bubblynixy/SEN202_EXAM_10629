from rest_framework import serializers
from employees.models import StaffBase, Manager, Intern

class StaffBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffBase
        fields = ['id', 'first_name', 'last_name', 'email', 'address', 'phone_number']

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['manager_id', 'manager_name', 'manager_email', 'manager_department', 'has_company_card']

class InternSerializer(serializers.ModelSerializer):
    mentor = ManagerSerializer(read_only=True)

    class Meta:
        model = Intern
        fields = ['intern_id', 'intern_name', 'intern_email', 'intern_department', 'internship_end', 'mentor']
