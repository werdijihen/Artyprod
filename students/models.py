from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
class Projet(models.Model):
    libelle = models.CharField(max_length=255)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    acheve = models.BooleanField(default=False)
    image = models.ImageField(upload_to='projet', null=True, blank=True)
 
def __str__(self):
        return self.libelle +","+self.description +","+str(self.date_debut)+","+self.type +","+str(self.date_fin)+","+self.acheve



class Personnel(models.Model):
    name = models.CharField(max_length=100)
    fichier_cv = models.FileField(upload_to='cv')
    image = models.ImageField(upload_to='personnel', null=True, blank=True)
    lien_linkedin = models.URLField(null=True, blank=True)
def __str__(self):
        return self.user +","+self.fichier_cv +","+str(self.image)+","+self.lien_linkedin
class Equipe(models.Model):
    nom = models.CharField(max_length=255)
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    members = models.ManyToManyField(User)
    image = models.ImageField(upload_to='equipe', null=True, blank=True)
    def __str__(self):
        return self.nom +","+str(self.projet)


class ProjectView(models.Model):
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    viewed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
     return f"{self.project.title} - {self.viewed_by.username}"


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    projects = models.ManyToManyField(Projet, through='ProjectRequest')
    email = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.user.username



class ProjectRequest(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    project = models.ForeignKey(Projet, on_delete=models.CASCADE)
    status_choices = (
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    )
    status = models.CharField(max_length=10, choices=status_choices, default='PENDING')

    def __str__(self):
        return f"Project Request by {self.client.user.username}: {self.project.title}"














































# Create your models here.
class StudentClassInfo(models.Model):
    class_name = models.CharField(max_length=20)
    class_short_form = models.CharField(max_length=10)

    def __str__(self):
        return self.class_name


class StudentSectionInfo(models.Model):
    section_name = models.CharField(max_length=20)

    def __str__(self):
        return self.section_name


class StudentShiftInfo(models.Model):
    shift_name = models.CharField(max_length=100)

    def __str__(self):
        return self.shift_name


class StudentInfo(models.Model):
    academic_year = models.CharField(max_length=100)
    admission_date = models.DateField()
    admission_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender_choice = (
        ("male", "Male"),
        ("Female", "Female"),
    )
    gender = models.CharField(choices=gender_choice, max_length=10)
    class_type = models.ForeignKey(StudentClassInfo, on_delete=models.CASCADE)
    section_type = models.ForeignKey(StudentSectionInfo, on_delete=models.CASCADE)
    shift_type = models.ForeignKey(StudentShiftInfo, on_delete=models.CASCADE)
    student_img = models.ImageField(upload_to='photos/%Y/%m/%d/')
    fathers_name = models.CharField(max_length=100)
    fathers_img = models.ImageField(upload_to='photos/%Y/%m/%d/')
    fathers_nid = models.IntegerField(unique=True)
    fathers_number = models.IntegerField(unique=True)
    mothers_name = models.CharField(max_length=100)
    mothers_img = models.ImageField(upload_to='photos/%Y/%m/%d/')
    mothers_nid = models.IntegerField(unique=True)
    mothers_number = models.IntegerField()

    class Meta:
        unique_together = ["admission_id", "class_type"]

    def __str__(self):
        return self.name


class AttendanceManager(models.Manager):
    def create_attendance(self, student_class, student_id):
        student_obj = StudentInfo.objects.get(
            class_type__class_short_form=student_class,
            admission_id=student_id
        )
        attendance_obj = Attendance.objects.create(student=student_obj, status=1)
        return attendance_obj


class Attendance(models.Model):
    student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.IntegerField(default=0)

    objects = AttendanceManager()

    class Meta:
        unique_together = ['student', 'date']

    def __str__(self):
        return self.student.admission_id

        # # for integer field
        # return str(self.student.mothers_nid)




      