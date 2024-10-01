from django.db import models
# from bosq.models.users import Users

class Overseer(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    email = models.EmailField(max_length=20)
    username = models.CharField(max_length=13, unique=True)
    password = models.CharField(max_length=13)
    # akun = models.ForeignKey(Users,on_delete=models.CASCADE)
    


    def __str__(self):
        return self.username