from django.db import models

# Creating models here.
class Speaker(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    contact_info = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='speakers/')
    expertise = models.CharField(max_length=100)

def __str__(self):
    return self.name





# creating dummy data for speakers app
# def create_dummy_speakers():
#     for i in range(10):
#         Speaker.objects.create(
#             name=f"Speaker {i}",
#             bio="Speaker Bio",
#             contact_info="Contact Info",
#             profile_picture="speakers/default_profile.png",
#             expertise="Expertise"
#         )

# create_dummy_speakers()