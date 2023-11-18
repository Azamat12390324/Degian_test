from django.db import models

class Home(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Homes'

class About(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

class Services(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='Services/detail_picture/%Y/%m/%d', blank=True)
    icon_title = models.CharField(max_length=255, blank=True)
    icon_sub_title = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

class Contact(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='Services/detail_picture/%Y/%m/%d', blank=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'


