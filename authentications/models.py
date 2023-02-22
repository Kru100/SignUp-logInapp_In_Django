from django.db import models

class Personal(models.Model):
    user_id = models.CharField(primary_key=True, max_length=20)
    user_name = models.CharField(max_length=50)
    age = models.IntegerField(blank=True, null=True)
    password = models.CharField(db_column='Password', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'personal'
