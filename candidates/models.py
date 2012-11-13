import os
from django.db import models
from election.settings import MEDIA_ROOT

# Create your models here.
class Faculty(models.Model):
    name = models.CharField(max_length=150)
    def __unicode__(self):
        return u'%s' % (self.name)

class Committee(models.Model):
    name = models.CharField(max_length=150)
    def __unicode__(self):
        return u'%s' % (self.name)


class CabinetPosition(models.Model):
    name = models.CharField(max_length=150)
    def __unicode__(self):
        return u'%s' % (self.name)

class PresidentialCabinet(models.Model):
    name = models.CharField(max_length=150)
    agenda = models.TextField()
    SecretCode=models.CharField(max_length=32)
    def __unicode__(self):
        return u'%s' % (self.name)



class Batch(models.Model):
    numberBeforeDash = models.IntegerField(default=4)
    def __unicode__(self):
        return u'%s' % (self.numberBeforeDash)

class SJBCandidate(models.Model):
    name = models.CharField(max_length=150)
    studentID=models.CharField(max_length=12)
    faculty=models.ForeignKey(Faculty)
    batch=models.ForeignKey(Batch)
    image=models.ImageField("Avatar", upload_to=MEDIA_ROOT, blank=True, null=True)
    mobile = models.CharField(max_length=30)
    GUCemail=models.EmailField(max_length=75)
    GPA=models.DecimalField(max_digits=3,decimal_places=2)
    agenda = models.TextField()
    def __unicode__(self):
        return u'%s' % (self.name)
    def filename(self):
        return os.path.basename(self.image.name)

class SenateCandidate(models.Model):
    name = models.CharField(max_length=150)
    studentID=models.CharField(max_length=12)
    faculty=models.ForeignKey(Faculty)
    batch=models.ForeignKey(Batch)
    image=models.ImageField("Avatar", upload_to=MEDIA_ROOT, blank=True, null=True)
    mobile = models.CharField(max_length=30)
    GUCemail=models.EmailField(max_length=75)
    GPA=models.DecimalField(max_digits=3,decimal_places=2)
    agenda = models.TextField()
    def __unicode__(self):
        return u'%s' % (self.name)
    def filename(self):
        return os.path.basename(self.image.name)


class ScCandidate(models.Model):
    name = models.CharField(max_length=150)
    studentID=models.CharField(max_length=12)
    faculty=models.ForeignKey(Faculty)
    committee=models.ForeignKey(Committee)
    batch=models.ForeignKey(Batch)
    image=models.ImageField("Avatar", upload_to=MEDIA_ROOT, blank=True, null=True)
    mobile = models.CharField(max_length=30)
    GUCemail=models.EmailField(max_length=75)
    GPA=models.DecimalField(max_digits=3,decimal_places=2)
    agenda = models.TextField()
    def __unicode__(self):
        return u'%s' % (self.name)
    def filename(self):
        return os.path.basename(self.image.name)

class AcCandidate(models.Model):
    name = models.CharField(max_length=150)
    studentID=models.CharField(max_length=12)
    faculty=models.ForeignKey(Faculty)
    grade=models.IntegerField(default=1)
    batch=models.ForeignKey(Batch)
    image=models.ImageField("Avatar", upload_to=MEDIA_ROOT, blank=True, null=True)
    mobile = models.CharField(max_length=30)
    GUCemail=models.EmailField(max_length=75)
    GPA=models.DecimalField(max_digits=3,decimal_places=2)
    agenda = models.TextField()
    def __unicode__(self):
        return u'%s' % (self.name)
    def filename(self):
        return os.path.basename(self.image.name)

class PresidentialCabinetMember(models.Model):
    name = models.CharField(max_length=150)
    studentID=models.CharField(max_length=12)
    faculty=models.ForeignKey(Faculty)
    cabinet=models.ForeignKey(PresidentialCabinet)
    position=models.ForeignKey(CabinetPosition)
    batch=models.ForeignKey(Batch)
    image=models.ImageField("Avatar", upload_to=MEDIA_ROOT, blank=True, null=True)
    mobile = models.CharField(max_length=30)
    GUCemail=models.EmailField(max_length=75)
    GPA=models.DecimalField(max_digits=3,decimal_places=2)
    agenda = models.TextField()
    def __unicode__(self):
        return u'%s' % (self.name)
    def filename(self):
        return os.path.basename(self.image.name)


