from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    department = serializers.ReadOnlyField(source='departament.department')

    class Meta:
        model = Employee
        fields = ('name', 'email', 'department')
