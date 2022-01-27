from django.db import models
from datetime import date
from datetime import datetime


class Person(models.Model):
    iin = models.CharField(max_length=12)
    age = models.CharField(max_length=3, blank=True, editable=False)

    def save(self, *args, **kwargs):
        today = datetime.today()
        birth_date = datetime.strptime(self.iin[:6], '%y%m%d')

        # days_in_year = 365.2425
        # self.age = int((date.today() - birth_date).days / days_in_year)
        if birth_date.year > datetime.today().year:
            birth_date = datetime.strptime(str(birth_date.year - 100) + str(birth_date.month) + str(birth_date.day), '%Y%m%d')

        self.age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

        super(Person, self).save(*args, **kwargs)