import hashlib

from django.db import models

# Create your models here.


class FilterDelManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_delete=False)


class User(models.Model):

    u_name = models.CharField(max_length=32, primary_key=True, db_column='u_name')
    u_pwd = models.CharField(max_length=32)
    u_email = models.CharField(max_length=32, unique=True)
    u_icon = models.ImageField(upload_to='icons')
    is_active = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    objects = FilterDelManager()

    def __str__(self):
        return self.u_name

    class Meta:
        db_table = 'user'

    @staticmethod
    def __generate_hash(password):
        sha = hashlib.sha512()
        sha.update(password.encode('utf-8'))
        return sha.hexdigest()

    def set_pwd(self, password):
        self.pwd = self.__generate_hash(password)

    def check_pwd(self, password):
        return self.pwd == self.__generate_hash(password)
