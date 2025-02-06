from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    POSITION_CHOICES = [
        ('Golman', 'Golman'),          
        ('Zadnji vezni', 'Zadnji vezni'),     
        ('Prednji vezni', 'Prednji vezni'), 
        ('Špic', 'Špic'),         
        ('Levo krilo', 'Levo krilo'),     
        ('Desno krilo', 'Desno krilo'),     
        ('Levi bek', 'Levi bek'),      
        ('Desni bek', 'Desni bek'),     
        ('Štoper', 'Štoper'),        
    ]

    NOGA_CHOICES = [
        ('Leva', 'Leva'),   
        ('Desna', 'Desna'), 
    ]

    ime = models.CharField(max_length=200, blank=True, null=True)  
    prezime = models.CharField(max_length=200)
    pozicija = models.CharField(
        max_length=20,  
        choices=POSITION_CHOICES,
        default='Prednji vezni',  
        blank=True, 
        null=True
    )
    nedostaci = models.TextField()
    prednosti = models.TextField()
    visina = models.FloatField()  
    tezina = models.FloatField()  
    noga = models.CharField(
        max_length=5, 
        choices=NOGA_CHOICES,  
        blank=True, 
        null=True
    )
    time = models.DateTimeField(default=timezone.now, blank=True)  
    image = models.ImageField(upload_to='images/posts/', blank=True, null=True)  
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    
    # New video URL field
    video_url = models.TextField(blank=True, null=True)  

    # New date of birth field
    datum_rođenja = models.DateField(blank=True, null=True)  
    
    def __str__(self):
        return f"{self.ime} {self.prezime} - {self.pozicija}"  
