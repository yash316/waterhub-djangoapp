from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name}  {self.last_name}"

    # Is User exists
    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    message = models.CharField(max_length=122)

    def __str__(self):
        return self.name
