from django.db import models

class Data(models.Model):
    polling_booth_number    =   models.CharField(max_length=50, blank=True, null=True)
    polling_booth_name      =   models.CharField(max_length=50, blank=True, null=True)
    parent_constituency     =   models.CharField(max_length=50, blank=True, null=True)
    winner2014              =   models.CharField(max_length=50, blank=True, null=True)
    runner_up               =   models.CharField(max_length=50, blank=True, null=True)
    margin1_percent         =   models.CharField(max_length=50, blank=True, null=True)
    margin1                 =   models.CharField(max_length=50, blank=True, null=True)
    total_voters            =   models.CharField(max_length=50, blank=True, null=True)
    bjp1_votes              =   models.CharField(max_length=50, blank=True, null=True)
    bjp1_vote_percent       =   models.CharField(max_length=50, blank=True, null=True)
    inc1_votes              =   models.CharField(max_length=50, blank=True, null=True)
    inc1_votes_percent      =   models.CharField(max_length=50, blank=True, null=True)
    winner2019              =   models.CharField(max_length=50, blank=True, null=True)
    margin2_percent         =   models.CharField(max_length=50, blank=True, null=True)
    margin2                 =   models.CharField(max_length=50, blank=True, null=True)
    total2_voters           =   models.CharField(max_length=50, blank=True, null=True)
    bjp2_votes              =   models.CharField(max_length=50, blank=True, null=True)
    bjp2_votes_percent      =   models.CharField(max_length=50, blank=True, null=True)
    inc2_votes              =   models.CharField(max_length=50, blank=True, null=True)
    inc2_vote_percent       =   models.CharField(max_length=50, blank=True, null=True)

    def __str__(self) -> str:
        return (f"{self.polling_booth_name}")
    
    objects = models.Manager()