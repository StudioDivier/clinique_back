from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse


class Informations(models.Model):
    staff = models.CharField(name='staff', max_length=128)
    text = models.CharField(name='text', max_length=256)

    def __str__(self):
        return self.staff


class InfoDirections(models.Model):
    info_id = models.ForeignKey(Informations, on_delete=models.CASCADE)
    direction_row = models.CharField(name='direction_row', max_length=256)


class Educations(models.Model):
    staff = models.CharField(name='staff', max_length=128)

    def __str__(self):
        return self.staff


class EducationItems(models.Model):
    ed_id = models.ForeignKey(Educations, on_delete=models.CASCADE)
    item = models.CharField(name='item', max_length=256)


class Courses(models.Model):
    staff = models.CharField(name='staff', max_length=128)

    def __str__(self):
        return self.staff


class CoursesItems(models.Model):
    courses_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    item = models.CharField(name='item', max_length=256)


class Events(models.Model):
    staff = models.CharField(name='staff', max_length=128)

    def __str__(self):
        return self.staff


class EventsItems(models.Model):
    events_id = models.ForeignKey(Events, on_delete=models.CASCADE)
    item = models.CharField(name='item', max_length=256)


class Subdirections(models.Model):
    name_direction = models.CharField(name='name_direction', max_length=128)
    name_subdirection = models.CharField(name='name_subdirection', max_length=128)

    def __str__(self):
        return self.name_subdirection


class ItemsSubDirection(models.Model):
    subdirection_id = models.ForeignKey(Subdirections, on_delete=models.CASCADE)
    item = models.CharField(name='item', max_length=128)

    # def __str__(self):
    #     return self.subdirection_id


class Direction(models.Model):
    direction = models.CharField(name='direction', max_length=128)

    def __str__(self):
        return self.direction


class DirectionsStaff(models.Model):
    staff = models.CharField(name='staff', max_length=256)

    def __str__(self):
        return self.staff

class DirectionStaffItems(models.Model):
    dir = models.ForeignKey(DirectionsStaff, on_delete=models.CASCADE)
    direction = models.CharField(name='direction', max_length=128)

    def __str__(self):
        return self.direction


class SubDirectionsStaff(models.Model):
    staff = models.CharField(name='staff', max_length=256)

    def __str__(self):
        return self.staff


class SubDirectionStaffItems(models.Model):
    subdir = models.ForeignKey(SubDirectionsStaff, on_delete=models.CASCADE)
    subdirection = models.CharField(name='subdirection', max_length=128)

    def __str__(self):
        return self.subdirection


class Personals(models.Model):
    full_name = models.CharField(name='full_name', max_length=128)
    state = models.CharField(name='state', max_length=128)
    experience = models.CharField(name='experience', max_length=64)
    photo = models.ImageField(name='photo')
    about_text = RichTextField()

    info = models.ForeignKey(Informations, on_delete=models.CASCADE)
    ed = models.ForeignKey(Educations, on_delete=models.CASCADE)
    cur = models.ForeignKey(Courses, on_delete=models.CASCADE)
    events = models.ForeignKey(Events, on_delete=models.CASCADE)
    add_direction = models.ForeignKey(DirectionsStaff, on_delete=models.CASCADE)
    add_subdirection = models.ForeignKey(SubDirectionsStaff, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('index:detail_staff', args=[self.id])


class Appointment(models.Model):
    name = models.CharField(name='name', max_length=128)
    phone = models.BigIntegerField(name='phone')
    email = models.EmailField(name='email')
    date = models.CharField(name='date', max_length=128)
    service = models.CharField(name='service', max_length=128)


class GetPrice(models.Model):
    name = models.CharField(name='name', max_length=128)
    phone = models.BigIntegerField(name='phone')
    email = models.EmailField(name='email')


class ServicesList(models.Model):
    service = models.CharField(name='service', max_length=128)
    img = models.ImageField(name='img')

class ServiceDetail(models.Model):
    service = models.ForeignKey(ServicesList, on_delete=models.CASCADE)
    name = models.CharField(name='name', max_length=128)

    description = models.CharField(name='description', max_length=1024)
    time_operation = models.CharField(name='time_operation', max_length=128)
    sex = models.CharField(name='sex', max_length=64)
    reabilitation = models.CharField(name='reabilitation', max_length=128)
    time_result = models.CharField(name='time_result', max_length=128)
    amnesia = models.CharField(name='amnesia', max_length=128)


    def get_absolute_url(self):
        return reverse('index:detail_services', args=[self.id])


class SessionPrices(models.Model):
    part_name = models.CharField(name='part_name', max_length=128)
    session_price1 = models.DecimalField(name='session_price1', max_digits=9, decimal_places=2)
    session_price2 = models.DecimalField(name='session_price2', max_digits=9, decimal_places=2)
    service = models.ForeignKey(ServiceDetail, on_delete=models.CASCADE)



