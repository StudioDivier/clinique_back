from django.contrib import admin
from . import models


class InfoInline(admin.StackedInline):
    model = models.InfoDirections


class ItemsInline(admin.StackedInline):
    model = models.ItemsSubDirection


class EducationItemsInline(admin.StackedInline):
    model = models.EducationItems


class CoursesItemsInline(admin.StackedInline):
    model = models.CoursesItems


class EventsItemsInline(admin.StackedInline):
    model = models.EventsItems


class DirectionStaffItemsInline(admin.StackedInline):
    model = models.DirectionStaffItems


@admin.register(models.DirectionsStaff)
class DirectionsStaffAdmin(admin.ModelAdmin):
    list_display = ('staff', )
    inlines = [DirectionStaffItemsInline, ]


class SubDirectionStaffItemsInline(admin.StackedInline):
    model = models.SubDirectionStaffItems


@admin.register(models.SubDirectionsStaff)
class SubdirectionsAdmin(admin.ModelAdmin):
    list_display = ('staff', )
    inlines = [SubDirectionStaffItemsInline, ]


@admin.register(models.Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ('direction', )


@admin.register(models.Informations)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('staff', )
    inlines = [InfoInline, ]


@admin.register(models.Educations)
class EducationAdmin(admin.ModelAdmin):

    inlines = [ EducationItemsInline, ]


@admin.register(models.Courses)
class CoursesAdmin(admin.ModelAdmin):

    inlines = [ CoursesItemsInline, ]


@admin.register(models.Events)
class EventsAdmin(admin.ModelAdmin):

    inlines = [ EventsItemsInline, ]


@admin.register(models.Personals)
class PersonalAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'state', 'experience', 'photo', 'about_text',
                    'info', 'ed', 'cur', 'events', 'add_direction', 'add_subdirection')


class SessionInline(admin.StackedInline):
    model = models.SessionPrices


@admin.register(models.ServiceDetail)
class ServiceDetailAdmin(admin.ModelAdmin):
    list_display = ('name','description','time_operation','sex','reabilitation','time_result','amnesia',)
    inlines = [ SessionInline ]


@admin.register(models.ServicesList)
class ServiceListAdmin(admin.ModelAdmin):
    list_display = ('service', 'img',)
