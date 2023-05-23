from django.db import models

# Create your models here.
class TeacherDeptInfo(models.Model):
    dept_name = models.CharField(max_length=50)

    def __str__(self):
        return self.dept_name

class TeacherSubInfo(models.Model):
    sub_name = models.CharField(max_length=50)

    def __str__(self):
        return self.sub_name

class TeacherInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    gender_choice = (
        ("male", "Male"),
        ("Female", "Female"),
    )
    gender = models.CharField(choices=gender_choice, max_length=10)
    teacher_img = models.ImageField(upload_to='photos/%Y/%m/%d/')
    passing_year = models.CharField(max_length=100)
    joining_date = models.DateField()
    dept_type = models.ForeignKey(TeacherDeptInfo, on_delete=models.CASCADE)
    sub_type = models.ForeignKey(TeacherSubInfo, on_delete=models.CASCADE)
    salary = models.IntegerField()

    def __str__(self):
        return self.name

class Personnel(models.Model):
    name = models.CharField(max_length=100)
    fichier_cv = models.FileField(upload_to='cv')
    image = models.ImageField(upload_to='personnel', null=True, blank=True)
    lien_linkedin = models.URLField(null=True, blank=True)
def __str__(self):
        return self.user +","+self.fichier_cv +","+str(self.image)+","+self.lien_linkedin


class PaymentHistory(models.Model):
    personnel = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    payment_date = models.DateField()
    payment_amount = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Payment of {self.payment_amount} for {self.personnel} on {self.payment_date}"