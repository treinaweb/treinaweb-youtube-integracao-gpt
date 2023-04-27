from django.db import models


class Job(models.Model):
    LEVEL_CHOICES = (
        ('jr', 'Júnior'),
        ('pl', 'Pleno'),
        ('sr', 'Sênior'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField()
    responsibilities = models.TextField()
    level = models.CharField(max_length=2, choices=LEVEL_CHOICES)
    skills = models.ManyToManyField("jobs.Skill", related_name="jobs")

    def __str__(self):
        return self.title



class Skill(models.Model):
    title = models.CharField(max_length=100, unique=True, blank=False, null=False)

    def __str__(self):
        return self.title