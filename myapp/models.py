from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    POSITION_CHOICES = [
        ('Golman', 'Golman'),           # Goalkeeper
        ('Zadnji vezni', 'Zadnji vezni'),       # Defender
        ('Prednji vezni', 'Prednji vezni'), # Midfielder
        ('Špic', 'Špic'),         # Forward
        ('Levo krilo', 'Levo krilo'),     # Left Forward
        ('Desno krilo', 'Desno krilo'),     # Right Forward
        ('Levi bek', 'Levi bek'),       # Left Back
        ('Desni bek', 'Desni bek'),     # Right Back
        ('Štoper', 'Štoper'),          # Center Back
    ]

    NOGA_CHOICES = [
        ('Leva', 'Leva'),   # Left Foot
        ('Desna', 'Desna'), # Right Foot
    ]

    ime = models.CharField(max_length=200, blank=True, null=True)  # Allow null and blank values
    prezime = models.CharField(max_length=200)
    pozicija = models.CharField(
        max_length=20,  # Change max_length to accommodate full position names
        choices=POSITION_CHOICES,
        default='Prednji vezni',  # Default to Midfielder (Prednji vezni)
        blank=True, 
        null=True
    )
    nedostaci = models.TextField()
    prednosti = models.TextField()
    visina = models.FloatField()  # Use FloatField for height (in cm, for example)
    tezina = models.FloatField()  # Use FloatField for weight (in kg, for example)
    noga = models.CharField(
        max_length=5, 
        choices=NOGA_CHOICES,  # Add choices for Left or Right Foot
        blank=True, 
        null=True
    )
    time = models.DateTimeField(default=timezone.now, blank=True)  # Corrected to use callable
    image = models.ImageField(upload_to='images/posts/', blank=True, null=True)  # Define the image field here    
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ForeignKey to User
    
    # New video URL field
    video_url = models.TextField(blank=True, null=True)  # Use TextField for the iframe embed code

    # New date of birth field
    datum_rođenja = models.DateField(blank=True, null=True)  # DateField for storing birth date
    
    def __str__(self):
        return f"{self.ime} {self.prezime} - {self.pozicija}"  # Display full position name
