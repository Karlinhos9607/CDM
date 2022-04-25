from django.db import models

# Create your models here.

class Matiere(models.Model):
    name = models.CharField(max_length=100)
    coef = models.IntegerField(null=False)

    def __str__(self):
        return self.name

class Etudiant(models.Model):
    name = models.CharField(max_length=200)
    matieres = models.ManyToManyField(Matiere, through='Note')

    def __str__(self):
        return self.name


class Note(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    note = models.FloatField()

    def __float__(self):
        return self.note

    class Meta:
        unique_together = ('matiere', 'etudiant')