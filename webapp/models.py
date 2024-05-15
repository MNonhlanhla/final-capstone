from django.db import models

''' Create the Enquiry class which wil hold the enquiry info.'''
class Enquiry(models.Model):
    subject_text = models.CharField(max_length=50)
    message_text = models.CharField(max_length=200)
    email_address_text = models.CharField(max_length=5)
    phone_number_text = models.CharField(max_length=15)

    def __str__(self):
        return self.subject_text + self.message_text
