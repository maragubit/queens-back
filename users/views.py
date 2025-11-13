from datetime import datetime
from django.shortcuts import render,redirect
from django.contrib import messages
from users.models import User,EmailList
from users.serializers import UserSimpleSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from rest_framework import permissions
from students.models import Student
from courses.models import Course
import os
from dotenv import load_dotenv
load_dotenv()





# Create your views here.

def register_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        obj, created = EmailList.objects.get_or_create(email=email)
        if not created:
            messages.error(request, f"El correo {email} ya ha sido registrado previamente.")
            return redirect('admin:index')
        front_domain=os.getenv("FRONT_DOMAIN")
        link = f"{front_domain}/register/{email}"

        # Contexto para la plantilla HTML
        context = {
            'name': email,
            'invite_link': link,
            'year': datetime.now().year,
        }

        # Renderizar la plantilla de correo
        html_content = render_to_string('emails/invitacion.html', context)
        text_content = f"Hola {email}, registrate usando este enlace: {link}"

        # Crear y enviar el correo con contenido HTML
        msg = EmailMultiAlternatives(
            subject='invitación para unirte al aula virtual',
            body=text_content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[email],
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        messages.success(request, f"Correo enviado a {email}")
        return redirect('admin:index')

    return redirect('admin:index')
      
    

class UserSimpleViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSimpleSerializer
    http_method_names = ['get','patch']
    permission_classes = [IsAuthenticated]  # Allow only authenticated users
    
    @action(detail=False, methods=['get'], url_path='me')
    def me(self, request, pk=None):
        user = self.request.user
        serializer = UserSimpleSerializer(user, context={'request': request})
        return Response(serializer.data)


class RegisterUserViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['post'], url_path='register_api', permission_classes=[permissions.AllowAny])
    def register(self, request, *args, **kwargs):
        email=request.data.get('email')
        emaillist=EmailList.objects.filter(email=email).first()
        if not emaillist:
            return JsonResponse({'message': 'El usuario no tiene invitación'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'message': 'El usuario ya existe'}, status=400)
        password=request.data.get('password')
        first_name=request.data.get('first_name')
        last_name=request.data.get('last_name')
        phone=request.data.get('phone')
        birthdate=request.data.get('birthdate')
        birthdate=datetime.strptime(birthdate, '%Y-%m-%d').date() if birthdate else None
        print(password)
        user=User.objects.create(
            username=email,
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            birthdate=birthdate,
            role="student"
        )
        user.set_password(password)
        user.save()
       
        Student.objects.create(user=user)
        return JsonResponse({'message': 'Usuario registrado correctamente'}, status=201)
        
    