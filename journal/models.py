from django.db import models

# Create your models here.
class Org(models.Model):
    org_name = models.CharField(max_length=200)
    def __str__(self):
        return self.org_name

class Actor(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return '{0} {1}'.format(self.surname, self.name)

class InRecord(models.Model):
    rec_num = models.CharField(max_length=50)
    rec_date = models.DateField(auto_now_add=True)
    rec_org = models.ForeignKey(Org, on_delete=models.CASCADE)
    out_num = models.CharField(max_length=50)
    out_date = models.DateField()
    rec_desc = models.CharField(max_length=200)
    rec_actor = models.ForeignKey(Actor, on_delete=models.CASCADE, limit_choices_to={'is_active': True}, null=True, blank=True, default=None)
    control_date = models.DateField(null=True, blank=True, default=None)
    rec_deal = models.PositiveIntegerField(null=True, blank=True, default=None)
    action_date = models.DateField(null=True, blank=True, default=None)
    
class OutRecord(models.Model):
    rec_num = models.CharField(max_length=50)
    rec_date = models.DateField(auto_now_add=True)
    rec_org = models.ForeignKey(Org, on_delete=models.CASCADE)
    rec_desc = models.CharField(max_length=200)
    rec_actor = models.ForeignKey(Actor, on_delete=models.CASCADE, limit_choices_to={'is_active': True})
    num_serv = models.PositiveIntegerField(null=True, blank=True, default=None)
    in_ref = models.ForeignKey(InRecord, on_delete=models.CASCADE, null=True, blank=True, default=None)
    num_mainpages = models.PositiveIntegerField()
    num_optpages = models.PositiveIntegerField()
