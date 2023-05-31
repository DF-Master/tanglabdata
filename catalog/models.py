from django.db import models
from django.urls import reverse  #Used to generate URLs by reversing the URL patterns

# ManyToManyField


class Tags(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="Enter a Tag in English (e.g. Toxic, Avoid Light)")

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('tags-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


# ForeignKey


class ChineseName(models.Model):
    name = models.CharField(max_length=200,
                            help_text="Enter a Chinese Name (e.g. 丙酮, 乙腈)")

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('chinese_name-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class EnglishName(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="Enter a English Name (e.g. Acetone, Acetonitrile)")

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('english_name-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(
        max_length=200,
        help_text=
        "Enter a Location (e.g. B205-4°C-Refrigerator, B205-Table1-Lowbox)")

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('location-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Source(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="Enter a Purchase Source (e.g. Aladdin, 源叶生物)")

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('source-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Principal(models.Model):
    first_name = models.CharField(max_length=100,
                                  help_text="Enter a First Name (e.g. Chun)")
    last_name = models.CharField(max_length=100,
                                 help_text="Enter a Last Name (e.g. Tang)")

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('principal-detail', args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)


# Reagent
class Reagent(models.Model):
    # Name
    name = models.CharField(
        max_length=200,
        help_text="Enter a Name in detail (e.g. Acetonitrile-5L-Masspure)")
    # Foreign Key used because Reagent can only have one key, but keys can have multiple reagents
    chinese_name = models.ForeignKey('ChineseName',
                                     on_delete=models.SET_NULL,
                                     null=True)
    english_name = models.ForeignKey('EnglishName',
                                     on_delete=models.SET_NULL,
                                     null=True)
    source = models.ForeignKey('Source', on_delete=models.SET_NULL, null=True)
    # ManyToManyField used because tags can contain many reagents. Reagents can cover many tags.
    # Tags class has already been defined so we can also specify the object above.
    tags = models.ManyToManyField(Tags,
                                  help_text="Select a tags for this book")

    specification = models.CharField(
        max_length=200,
        help_text="Enter a specification (e.g. 1L, 30mg)",
        null=True,
        blank=True)
    cas = models.CharField(
        max_length=200,
        help_text=
        'Enter a <a href="https://en.wikipedia.org/wiki/CAS_Registry_Number">CAS</a> (e.g. 921-60-8)',
        null=True,
        blank=True,
        verbose_name='CAS')
    # Other Information
    purchase_note = models.CharField(
        max_length=200,
        help_text="Enter a purchase note (e.g. hyperlink, item No.)",
        null=True,
        blank=True)
    note = models.CharField(max_length=1000,
                            help_text="Enter a brief note",
                            null=True,
                            blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('reagent-detail', args=[str(self.id)])

    def display_tags(self):
        return ', '.join([tags.name for tags in self.tags.all()[:3]])

    display_tags.short_description = 'Tags'


import uuid  # Required for unique reagent instances
import datetime
import random


class ReagentInstance(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text=
        "Unique ID for this particular reagent across whole database, be careful to change!!"
    )
    reagent = models.ForeignKey('Reagent',
                                on_delete=models.SET_NULL,
                                null=True)
    register_date = models.DateField(null=True,
                                     blank=True,
                                     default=datetime.date.today)
    name = models.CharField(max_length=200,
                            null=True,
                            blank=True,
                            default=id.default,
                            help_text="Change to your favorate name")
    principal = models.ForeignKey('Principal',
                                  on_delete=models.SET_NULL,
                                  null=True,
                                  blank=True)
    location = models.ForeignKey('Location',
                                 on_delete=models.SET_NULL,
                                 null=True)

    STATUS = (
        ('n', 'Never Used'),
        ('o', 'Occupied'),
        ('a', 'Available'),
        ('r', 'Run out'),
    )

    status = models.CharField(max_length=1,
                              choices=STATUS,
                              blank=True,
                              default='o',
                              help_text='Reagent Status')
    note = models.CharField(max_length=1000,
                            help_text="Enter a brief note",
                            null=True,
                            blank=True)

    class Meta:
        ordering = ["-register_date", "name"]

    def __str__(self):
        return '%s (%s)' % (self.id, self.reagent.name)

    def get_absolute_url(self):
        return reverse('reagentinstance-detail', args=[str(self.id)])
