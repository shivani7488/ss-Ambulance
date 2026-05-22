from django.db import models
from django.contrib.auth.models import User

# 1. User Profile Model (Singers aur Writers ki details ke liye)
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('singer', 'Singer'),
        ('writer', 'Writer'),
        ('musician', 'Musician'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES) # Sahi: max_length
    bio = models.TextField(blank=True, default="")
    skills = models.CharField(max_length=255, blank=True, help_text="Comma-separated skills (e.g. Classical, Pop, Rap)")
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"


# 2. Music & Lyrics Post Model (Talent upload karne ke liye)
class MusicPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200) # Sahi: max_length (Pehle yahan galti thi)
    
    # Lyrics ke liye text field (Writers ke liye)
    lyrics = models.TextField(blank=True, null=True)  
    
    # Audio field (Singers ke liye)
    audio_file = models.FileField(upload_to='songs/', blank=True, null=True)  
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.user.username}"


# 3. Collaboration Request Model (Ek dusre se connect karne ke liye)
class CollaborationRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_requests')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_requests')
    message = models.TextField(help_text="Aap kyu collaborate karna chahte hain?")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Req from {self.sender.username} to {self.receiver.username} ({self.status})"


# 4. Chat Message Model (In-app communication ke liye)
class ChatMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f"From {self.sender.username} to {self.receiver.username} at {self.timestamp}"