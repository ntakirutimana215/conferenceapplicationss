from datetime import date
from django.db import models

from speakers.models import  Speaker

class Category(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def __str__(self):
        return str(self.name)


class Conference(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    category = models.CharField(max_length=200)
    venue = models.CharField(max_length=100)
    theme = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Session(models.Model):
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    speakers = models.ManyToManyField(Speaker)

    def __str__(self):
        return self.title


class Attendee(models.Model):
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    selected_sessions = models.ManyToManyField(Session, blank=True)
    payment_made = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class SessionReminder(models.Model):
    attendee = models.ForeignKey(Attendee, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    reminder_sent = models.BooleanField(default=False)

    def __str__(self):
        return f'Reminder for {self.session} to {self.attendee}'


class Rating(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    attendee = models.ForeignKey(Attendee, on_delete=models.CASCADE)
    rating = models.IntegerField()

    def __str__(self):
        return f'Rating {self.rating} for {self.session} by {self.attendee}'
    
# def create_dummy_conferences():
#     category = Category.objects.create(name="Category")
#     for i in range(10):
#         Conference.objects.create(
#             title=f"Conference {i}",
#             category=category,
#             date=date(2023, 6, 1),
#             venue="Venue",
#             theme="Theme"
#         )

# create_dummy_conferences()

