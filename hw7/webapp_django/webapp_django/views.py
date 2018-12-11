from django.http import HttpResponse
from .models import *


def get_name(requests):
    persons = [
        '%s' % person.name
        for person in Person.objects.all()
    ]
    return HttpResponse('; '.join(persons))


def get_person_data(requests, name):
    person_data = ['%s, %s' % (person.age, person.profession) for person in Person.objects.all() if person.name == name]
    return HttpResponse(person_data)


def get_age(requests, name):
    person_age = ['%s' % person.age for person in Person.objects.all() if person.name == name]
    return HttpResponse(person_age)


def get_profession(requests, name):
    person_profession = ['%s' % person.profession for person in Person.objects.all() if person.name == name]
    return HttpResponse(person_profession)
