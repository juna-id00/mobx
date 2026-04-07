from django.db import models


class mobile(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    ram = models.CharField(max_length=50, null=True, blank=True)
    storage = models.CharField(max_length=50, null=True, blank=True)
    battery = models.CharField(max_length=50, null=True, blank=True)
    processor = models.CharField(max_length=100, null=True, blank=True)
    camera = models.CharField(max_length=100, null=True, blank=True)
    display = models.CharField(max_length=100, null=True, blank=True)
    specifications = models.TextField(max_length=1000, null=True, blank=True)

    reviewer1_name = models.CharField(max_length=100, blank=True, null=True)
    reviewer1_profile = models.ImageField(upload_to='reviewers/', blank=True, null=True)
    review1 = models.TextField(blank=True, null=True)

    reviewer2_name = models.CharField(max_length=100, blank=True, null=True)
    reviewer2_profile = models.ImageField(upload_to='reviewers/', blank=True, null=True)
    review2 = models.TextField(blank=True, null=True)

    reviewer3_name = models.CharField(max_length=100, blank=True, null=True)
    reviewer3_profile = models.ImageField(upload_to='reviewers/', blank=True, null=True)
    review3 = models.TextField(blank=True, null=True)

    reviewer4_name = models.CharField(max_length=100, blank=True, null=True)
    reviewer4_profile = models.ImageField(upload_to='reviewers/', blank=True, null=True)
    review4 = models.TextField(blank=True, null=True)

    reviewer5_name = models.CharField(max_length=100, blank=True, null=True)
    reviewer5_profile = models.ImageField(upload_to='reviewers/', blank=True, null=True)
    review5 = models.TextField(blank=True, null=True)

    reviewer6_name = models.CharField(max_length=100, blank=True, null=True)
    reviewer6_profile = models.ImageField(upload_to='reviewers/', blank=True, null=True)
    review6 = models.TextField(blank=True, null=True)

    image = models.ImageField(upload_to='mobiles/')

    def __str__(self):
        return f"{self.brand} {self.name}"


class laptop(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    ram = models.CharField(max_length=50, null=True, blank=True)
    storage = models.CharField(max_length=50, null=True, blank=True)
    battery = models.CharField(max_length=50, null=True, blank=True)
    processor = models.CharField(max_length=100, null=True, blank=True)
    camera = models.CharField(max_length=100, null=True, blank=True)
    display = models.CharField(max_length=100, null=True, blank=True)
    specifications = models.TextField(max_length=1000, null=True, blank=True)

    reviewer1_name = models.CharField(max_length=100, blank=True, null=True)
    reviewer1_profile = models.ImageField(upload_to='reviewers/', blank=True, null=True)
    review1 = models.TextField(blank=True, null=True)

    reviewer2_name = models.CharField(max_length=100, blank=True, null=True)
    reviewer2_profile = models.ImageField(upload_to='reviewers/', blank=True, null=True)
    review2 = models.TextField(blank=True, null=True)

    reviewer3_name = models.CharField(max_length=100, blank=True, null=True)
    reviewer3_profile = models.ImageField(upload_to='reviewers/', blank=True, null=True)
    review3 = models.TextField(blank=True, null=True)

    reviewer4_name = models.CharField(max_length=100, blank=True, null=True)
    reviewer4_profile = models.ImageField(upload_to='reviewers/', blank=True, null=True)
    review4 = models.TextField(blank=True, null=True)

    reviewer5_name = models.CharField(max_length=100, blank=True, null=True)
    reviewer5_profile = models.ImageField(upload_to='reviewers/', blank=True, null=True)
    review5 = models.TextField(blank=True, null=True)

    reviewer6_name = models.CharField(max_length=100, blank=True, null=True)
    reviewer6_profile = models.ImageField(upload_to='reviewers/', blank=True, null=True)
    review6 = models.TextField(blank=True, null=True)

    image = models.ImageField(upload_to='mobiles/')

    def __str__(self):
        return f"{self.brand} {self.name}"


class tablet(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    ram = models.CharField(max_length=50, null=True, blank=True)
    storage = models.CharField(max_length=50, null=True, blank=True)
    battery = models.CharField(max_length=50, null=True, blank=True)
    processor = models.CharField(max_length=100, null=True, blank=True)
    camera = models.CharField(max_length=100, null=True, blank=True)
    display = models.CharField(max_length=100, null=True, blank=True)
    specifications = models.TextField(max_length=1000, null=True, blank=True)

    reviewer1_name = models.CharField(max_length=100, blank=True, null=True)
    reviewer1_profile = models.ImageField(upload_to='reviewers/', blank=True, null=True)
    review1 = models.TextField(blank=True, null=True)

    reviewer2_name = models.CharField(max_length=100, blank=True, null=True)
    reviewer2_profile = models.ImageField(upload_to='reviewers/', blank=True, null=True)
    review2 = models.TextField(blank=True, null=True)

    reviewer3_name = models.CharField(max_length=100, blank=True, null=True)
    reviewer3_profile = models.ImageField(upload_to='reviewers/', blank=True, null=True)
    review3 = models.TextField(blank=True, null=True)

    reviewer4_name = models.CharField(max_length=100, blank=True, null=True)
    reviewer4_profile = models.ImageField(upload_to='reviewers/', blank=True, null=True)
    review4 = models.TextField(blank=True, null=True)

    reviewer5_name = models.CharField(max_length=100, blank=True, null=True)
    reviewer5_profile = models.ImageField(upload_to='reviewers/', blank=True, null=True)
    review5 = models.TextField(blank=True, null=True)

    reviewer6_name = models.CharField(max_length=100, blank=True, null=True)
    reviewer6_profile = models.ImageField(upload_to='reviewers/', blank=True, null=True)
    review6 = models.TextField(blank=True, null=True)

    image = models.ImageField(upload_to='mobiles/')


class smartwatch(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    ram = models.CharField(max_length=50, null=True, blank=True)
    storage = models.CharField(max_length=50, null=True, blank=True)
    battery = models.CharField(max_length=50, null=True, blank=True)
    processor = models.CharField(max_length=100, null=True, blank=True)
    camera = models.CharField(max_length=100, null=True, blank=True)
    display = models.CharField(max_length=100, null=True, blank=True)
    specifications = models.TextField(max_length=1000, null=True, blank=True)

    reviewer1_name = models.CharField(max_length=100, blank=True, null=True)
    reviewer1_profile = models.ImageField(upload_to='reviewers/', blank=True, null=True)
    review1 = models.TextField(blank=True, null=True)

    reviewer2_name = models.CharField(max_length=100, blank=True, null=True)
    reviewer2_profile = models.ImageField(upload_to='reviewers/', blank=True, null=True)
    review2 = models.TextField(blank=True, null=True)

    reviewer3_name = models.CharField(max_length=100, blank=True, null=True)
    reviewer3_profile = models.ImageField(upload_to='reviewers/', blank=True, null=True)
    review3 = models.TextField(blank=True, null=True)

    reviewer4_name = models.CharField(max_length=100, blank=True, null=True)
    reviewer4_profile = models.ImageField(upload_to='reviewers/', blank=True, null=True)
    review4 = models.TextField(blank=True, null=True)

    reviewer5_name = models.CharField(max_length=100, blank=True, null=True)
    reviewer5_profile = models.ImageField(upload_to='reviewers/', blank=True, null=True)
    review5 = models.TextField(blank=True, null=True)

    reviewer6_name = models.CharField(max_length=100, blank=True, null=True)
    reviewer6_profile = models.ImageField(upload_to='reviewers/', blank=True, null=True)
    review6 = models.TextField(blank=True, null=True)

    image = models.ImageField(upload_to='mobiles/')


class headphones(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)


    battery = models.CharField(max_length=50, null=True, blank=True)
    specifications = models.TextField(max_length=1000, null=True, blank=True)

    reviewer1_name = models.CharField(max_length=100, blank=True, null=True)
    reviewer1_profile = models.ImageField(upload_to='reviewers/', blank=True, null=True)
    review1 = models.TextField(blank=True, null=True)

    reviewer2_name = models.CharField(max_length=100, blank=True, null=True)
    reviewer2_profile = models.ImageField(upload_to='reviewers/', blank=True, null=True)
    review2 = models.TextField(blank=True, null=True)

    reviewer3_name = models.CharField(max_length=100, blank=True, null=True)
    reviewer3_profile = models.ImageField(upload_to='reviewers/', blank=True, null=True)
    review3 = models.TextField(blank=True, null=True)

    reviewer4_name = models.CharField(max_length=100, blank=True, null=True)
    reviewer4_profile = models.ImageField(upload_to='reviewers/', blank=True, null=True)
    review4 = models.TextField(blank=True, null=True)

    reviewer5_name = models.CharField(max_length=100, blank=True, null=True)
    reviewer5_profile = models.ImageField(upload_to='reviewers/', blank=True, null=True)
    review5 = models.TextField(blank=True, null=True)

    reviewer6_name = models.CharField(max_length=100, blank=True, null=True)
    reviewer6_profile = models.ImageField(upload_to='reviewers/', blank=True, null=True)
    review6 = models.TextField(blank=True, null=True)

    image = models.ImageField(upload_to='mobiles/')
      
    def __str__(self):
        return f"{self.brand} {self.name}"
      