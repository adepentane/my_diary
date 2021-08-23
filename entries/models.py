from django.db import models

# Create your models here.
# For Every Class in your Models, is a Table in your Database.
# Then you run the python manage.py migrate command to link it up.


class Entry(models.Model):
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Entry #{}'.format(self.id)

    class Meta:
        verbose_name_plural = 'entries'