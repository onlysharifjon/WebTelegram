from django.db import models




class Foydalanuvchilar(models.Model):
    photo = models.ImageField(upload_to="uploads/profile_photo",null=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100,unique=False,null=True)




class ChatModel(models.Model):
    kim_yozdi = models.ForeignKey(Foydalanuvchilar,on_delete=models.CASCADE,related_name="jonatdi")
    kimga_yozdi = models.ForeignKey(Foydalanuvchilar,on_delete=models.CASCADE,related_name='qabul_qildi')
    vaqt = models.DateTimeField(auto_now_add=True)
    xabar_text = models.TextField(max_length=300)



