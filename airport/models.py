from django.db import models
from django.utils import timezone

class Airport(models.Model):
  name = models.CharField(max_length=60, unique=True, verbose_name='نام')
  city = models.CharField(max_length=60,verbose_name='شهر')
  country = models.CharField(max_length=60, verbose_name='کشور')
  class Meta:
    verbose_name = 'فرودگاه'
    verbose_name_plural = 'فرودگاه ها'
  def __str__(self):
    return self.name 


class Flight(models.Model):
  STATUS_CHOICES = (('C' , "کنسل"),('D' , 'تاخیر'),('I','حادثه'),('O','Ok'))
  orgin = models.ForeignKey(Airport, related_name='orgin',on_delete = models.CASCADE , verbose_name="مبدا")
  destination = models.ForeignKey(Airport, related_name='dest', on_delete=models.CASCADE,verbose_name='مقصد')
  flight_time = models.DateTimeField(default=timezone.now, verbose_name='ساعت و تاریخ پرواز')
  land_time = models.DateTimeField(default=timezone.now  ,verbose_name='  ساعت و تاریخ فرود')
  status = models.CharField(max_length=1, choices=STATUS_CHOICES , verbose_name='وضعیت')
  capcity = models.IntegerField(verbose_name='ظرفیت')

  class Meta:
    verbose_name = 'پرواز'
    verbose_name_plural = 'پرواز ها'
  def __str__(self):
     return f"{self.orgin.name}  به {self.destination.name}"

class  Staff(models.Model):
  ROLE_CHOICES= (('C' , 'کاپیتان'),('M' , 'مهماندار') , ('K','کمک خلبان'),)
  GENDER_CHOICES = (('M','male') , ('F' , 'Female') ,('U' , 'Undefined'))
  name = models.CharField(max_length=60, verbose_name='نام')
  age = models.IntegerField(verbose_name='سن')
  role = models.CharField(
  max_length=1, choices=ROLE_CHOICES, verbose_name='نقش')
  mobile = models.CharField(max_length=11, verbose_name='تلفن همراه')
  gender = models.CharField(
  max_length=1, choices=GENDER_CHOICES, verbose_name='جنسیت')
  flight = models.ForeignKey(Flight, on_delete=models.CASCADE)

  class Meta:
    verbose_name = 'خدمه'
    verbose_name_plural = 'خدمه ها'
  def __str__(self):
    return self.name


class Employee(models.Model):
  GENDER_CHOICES = (('M', 'male'), ('F', 'Female'), ('U', 'Undefined'))
  name = models.CharField(max_length=60, unique=True, verbose_name='نام')
  manager = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
  age = models.IntegerField(verbose_name='سن')
  job = models.CharField(max_length=100)
  mobile = models.CharField(max_length=11, verbose_name='تلفن همراه')
  gender = models.CharField(
  max_length=1, choices=GENDER_CHOICES, verbose_name='جنسیت')
  pay = models.IntegerField()
  airport = models.ForeignKey(Airport, on_delete=models.CASCADE)
  def __str__(self):
    return self.name
  class Meta:
    verbose_name = 'کارمندان'
    verbose_name_plural = 'کارمندان ها'

class Passenger(models.Model):
  GENDER_CHOICES = (('M', 'male'), ('F', 'Female'), ('U', 'Undefined'))
  name = models.CharField(max_length = 60, unique = True, verbose_name = 'نام')
  age = models.IntegerField(verbose_name = 'سن')
  mobile = models.CharField(max_length = 11, verbose_name = 'تلفن همراه')
  gender = models.CharField(
  max_length = 1, choices = GENDER_CHOICES, verbose_name = 'جنسیت')
  email = models.EmailField()
  flight = models.OneToOneField(Flight, on_delete=models.CASCADE)
  def __str__(self):
    return self.name
  class Meta:
    verbose_name = 'مسافر'
    verbose_name_plural = 'مسافرها'

class Tickets(models.Model):
  TYPE_CHOICES = (('F', 'First class'), ('R', 'regular'), ('B', 'Bisiness'))
  passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)
  flight = models.OneToOneField(Flight,on_delete=models.CASCADE)
  time = models.DateTimeField(default = timezone.now)
  kind = models.CharField(max_length = 1, choices = TYPE_CHOICES, verbose_name = 'جنسیت')
  price = models.PositiveIntegerField()

  class Meta:
    verbose_name = 'بلیط'
    verbose_name_plural = 'بلیط ها'

  def __str__(self):
    return f"{self.passenger.name } /{self.flight}"

  


