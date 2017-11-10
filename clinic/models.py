from django.db import models

class Brand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=32,null=True)
    brand_address = models.CharField(max_length=300,null=True)
    brand_phone_number = models.CharField(max_length=11,null=True)
    brand_manager_id  = models.IntegerField(null=True)

class User(models.Model):
    brand_id = models.IntegerField(null=True)
    user_id = models.AutoField(primary_key=True)
    user_login_id = models.CharField(max_length=8,null=True)
    user_password = models.CharField(max_length=32,null=True)
    user_role = models.CharField(max_length=100,null=True)
    user_name = models.CharField(max_length=300,null=True)
    user_dob = models.CharField(max_length=10,null=True)
    user_phone_number = models.CharField(max_length=11,null=True)
    user_address = models.TextField(null=True)
    user_specialize = models.CharField(max_length=200,null=True)
    user_delete_flag = models.CharField(max_length=1,null=True)

class Customer(models.Model):
    brand_id = models.IntegerField(null=True)
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=32,null=True)
    customer_sex = models.CharField(max_length=32,null=True)
    customer_dob = models.CharField(max_length=10,null=True)
    customer_job = models.CharField(max_length=500,null=True)
    customer_company = models.CharField(max_length=500,null=True)
    customer_phone_number = models.CharField(max_length=11,null=True)
    customer_email = models.CharField(max_length=200,null=True)
    customer_address = models.TextField(null=True)
    customer_source = models.CharField(max_length=500,null=True)
    customer_fingerprint = models.TextField(max_length=500,null=True)

#   medical_biography = models.TextField(max_length=500,null=True)#sẽ bỏ cái này
#   def __str__(self):
#    return self.customer_name
# class MedicalHistory(models.Model):
#   # medicalhis_id = models.CharField(max_length=8,null=True)
#   brand_id = models.CharField(max_length=8,null=True)
#   customer_id = models.CharField(max_length=8,null=True)
#   medicalhis_type = models.CharField(max_length=2,null=True)
#   medicalhis_name = models.CharField(max_length=500,null=True)
#   medicalhis_status = models.CharField(max_length=500,null=True)
#   medicalhis_detail = models.CharField(max_length=500,null=True)
#   create_date = models.CharField(max_length=10,null=True)
#   create_by = models.CharField(max_length=10,null=True)
#   update_date = models.CharField(max_length=10,null=True)
#   update_by = models.CharField(max_length=10,null=True)
#   delete_flag = models.CharField(max_length=1,null=True)

# class Relationship(models.Model):
#   customer_id1 = models.CharField(max_length=8,null=True)
#   customer_id2 = models.CharField(max_length=8,null=True)
#   relationship = models.CharField(max_length=32,null=True)
# class CalendarDentist(models.Model):
#   brand_id =  models.CharField(max_length=8,null=True)
#   user_id = models.CharField(max_length=8,null=True)
#   time = models.DateTimeField(null=True)

class Appointment(models.Model):
    brand_id = models.IntegerField(null=True)
    user_id =  models.IntegerField(null=True)
    customer_id =  models.IntegerField(null=True)
    treatment_id = models.IntegerField(null=True)
    appointment_id = models.AutoField(primary_key=True)
    appointment_date = models.CharField(max_length=10,null=True)
    appointment_time = models.CharField(max_length=5,null=True)
    # appointment_name = models.CharField(max_length=500,null=True)
    appointment_content = models.CharField(max_length=500,null=True)
    appointment_assign_id = models.IntegerField(null=True)
    appointment_estimated_time = models.CharField(max_length=8,null=True)
    appointment_estimated_difficulty = models.CharField(max_length=2,null=True)
    appointment_status = models.CharField(max_length=10,null=True)
    appointment_note = models.TextField(null=True)
    appointment_create_date = models.CharField(max_length=10,null=True)
    appointment_create_by = models.CharField(max_length=8,null=True)
    appointment_update_date = models.CharField(max_length=10,null=True)
    appointment_update_by = models.CharField(max_length=8,null=True)
    appointment_delete_flag = models.CharField(max_length=1,null=True)
#   def __str__(self):
#    return self.userID
class Treatment(models.Model):
    brand_id = models.IntegerField(null=True)
    user_id = models.IntegerField(null=True)
    customer_id = models.IntegerField(null=True)
    treatment_id = models.AutoField(primary_key=True)
    treatment_name = models.CharField(max_length=200,null=True)
    treatment_content = models.CharField(max_length=500,null=True)
    treatment_total_payment =  models.IntegerField(null=True,default=0)
    treatment_payment_status = models.IntegerField(null=True,default=0)
    treatment_status = models.CharField(max_length=10,null=True)
    treatment_create_date = models.CharField(max_length=10,null=True)
    treatment_create_by = models.CharField(max_length=8,null=True)
    treatment_update_date = models.CharField(max_length=10,null=True)
    treatment_update_by = models.CharField(max_length=8,null=True)
    treatment_delete_flag = models.CharField(max_length=1,null=True)

class TreatmentDetail(models.Model):
    brand_id = models.IntegerField(null=True)
    treatment_id = models.IntegerField(null=True)
    treatmentdetail_id = models.AutoField(primary_key=True)
    treatmentdetail_no = models.CharField(max_length=10,null=True)
    treatmentdetail_date = models.CharField(max_length=10,null=True)
    treatmentdetail_content = models.CharField(max_length=500,null=True)
    treatmentdetail_price  = models.IntegerField(null=True)
    treatmentdetail_status = models.CharField(max_length=10,null=True)
    treatmentdetail_create_date = models.CharField(max_length=10,null=True)
    treatmentdetail_create_by = models.CharField(max_length=8,null=True)
    treatmentdetail_update_date = models.CharField(max_length=10,null=True)
    treatmentdetail_update_by = models.CharField(max_length=8,null=True)
    treatmentdetail_delete_flag = models.CharField(max_length=1,null=True)

# class Invoice(models.Model):
#   brand_id = models.CharField(max_length=8,null=True)
#   user_id = models.CharField(max_length=8,null=True)
#   customer_id = models.CharField(max_length=8,null=True)
#   treatment_id = models.CharField(max_length=8,null=True)
#   invoice_id = models.CharField(max_length=8,null=True)
#   pay = models.IntegerField(null=True)

# class Inventory(models.Model):
#   brand_id = models.CharField(max_length=8,null=True)
#   item_id = models.CharField(max_length=8,null=True)
#   item_name = models.IntegerField(null=True)
#   unit = models.CharField(max_length=32,null=True)
#   quantity = models.IntegerField(null=True)

# class Labo(models.Model):
#   brand_id = models.CharField(max_length=8,null=True)
#   labo_name = models.CharField(max_length=100,null=True)
#   address =  models.TextField(max_length=500,null=True)
#   phone_number =  models.CharField(max_length=11,null=True)

# class TreatmentDetailLabo   (models.Model):
#   labo_id = models.CharField(max_length=8,null=True)
#   treatment_id = models.CharField(max_length=8,null=True)
#   send_day = models.DateTimeField(null=True)
#   received_day = models.DateTimeField(null=True)
#   price = models.IntegerField(null=True)


