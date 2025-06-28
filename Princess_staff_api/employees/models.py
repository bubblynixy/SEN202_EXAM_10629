from django.db import models

class StaffBase(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

    class Manager(models.Model):
        manager_id = models.AutoField(primary_key=True)
        manager_name = models.CharField(max_length=100)
        manager_email = models.EmailField(unique=True)
        manager_department = models.CharField(max_length=100)
        has_company_card = models.BooleanField(default=True)
    
        def _str_(self):
            return f"{self.manager_id},  {self.manager_name}, {self.manager_email}, {self.manager_department}"

    class Intern(models.Model):
        intern_id = models.AutoField(primary_key=True)
        intern_name = models.CharField(max_length=100)
        intern_email = models.EmailField(unique=True)
        internship_end = models.CharField(max_length=50)
        intern_department = models.CharField(max_length=100)
        mentor = models.ForeignKey(Manager, on_delete=models.CASCADE)
        
        def _str_(self):
            return f"{self.intern_id},  {self.intern_name}, {self.intern_email}, {self.intern_department}"
        
        

