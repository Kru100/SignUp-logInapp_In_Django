# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Login(models.Model):
    user_id = models.CharField(primary_key=True, max_length=-1)
    password = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'login'


class Personal(models.Model):
    user_id = models.CharField(primary_key=True, max_length=-1)
    user_name = models.CharField(max_length=-1)
    age = models.IntegerField(blank=True, null=True)
    star_sign = models.CharField(max_length=-1, blank=True, null=True)
    fav_mus = models.CharField(max_length=-1, blank=True, null=True)
    drama_type = models.CharField(max_length=-1, blank=True, null=True)
    number_27_07_15 = models.BooleanField(db_column='27/07/15', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'personal'
