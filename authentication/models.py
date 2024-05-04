from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    CREATOR = 'CREATOR'
    SUBSCRIBER ='SUBSCRIBER'
    Role_Choices =(
        (CREATOR ,'Créateur'),
        (SUBSCRIBER,'Abonnée')
    )
    profile_photo = models.ImageField(verbose_name='Profile de photo')
    role = models.CharField(max_length=30 , choices=Role_Choices,verbose_name='Role')
"""
Le fait de désigner le  CREATOR  (créateur) et leSUBSCRIBER  (abonné) comme des constantes
 vous permet de vérifier la valeur du champ  role  (rôle) sans écrire la valeur en dur. 
  Par exemple, si user.role == user.CREATOR
"""