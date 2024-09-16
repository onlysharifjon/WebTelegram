import smtplib, random
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from email.mime.multipart import MIMEMultipart
from .models import Foydalanuvchilar
from rest_framework.views import APIView
from .serializers import RegistrationSeralizer, LoginSeralizer,ChatSerializer
from email.mime.text import MIMEText


# class Registratsiya(APIView):
#     serializer_class = RegistrationSeralizer
#     def post(self, request):
#         serializer = RegistrationSeralizer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"Xabar": "Saved User in Database"})
#         else:
#             return Response(serializer.errors)

class Registratsiya(APIView):
    serializer_class = RegistrationSeralizer

    def post(self, request):
        ismi = request.data.get("name")
        familiya = request.data.get("surname")
        email = request.data.get("email")
        nikname = request.data.get("username")
        Foydalanuvchilar.objects.create(name=ismi, surname=familiya, email=email, username=nikname)

        return Response({"Xabar": "Backend ga keldi ma`lumot"})


class LoginApi(APIView):

    def post(self, request):
        email = request.data.get("email")
        user = Foydalanuvchilar.objects.filter(email=email).first()

        if user:
            sender_email = "mominovsharif12@gmail.com"
            receiver_email = email
            password = "jzut iarx gaks ybut"
            smtp_server = "smtp.gmail.com"
            smtp_port = 587

            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, password)

            message = MIMEMultipart()
            body = "For Test 804 Group"
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = "For Test"
            message.attach(MIMEText(body, "plain"))

            server.sendmail(sender_email, receiver_email, message.as_string())
            server.quit()

            return Response({'message': 'Email sent successfully!'}, 200)

        else:
            return Response({"message": "Bunday email mavjud emas !"}, 404)


class YozishmaAPI(APIView):
    serializer_class = ChatSerializer
    def post(self,request):
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Xabar": 'Sizning xabaringiz jo`natildi'})
        else:
            return Response(serializer.errors)
