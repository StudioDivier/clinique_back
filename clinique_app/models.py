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

