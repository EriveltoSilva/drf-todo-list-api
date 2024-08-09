from django.conf import settings
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


def send_register_welcome(user, email: str, project_name: str, company_address: str,
                          action_url: str, support_email: str = "", login_url: str = "",
                          project_website: str = ""):
    subject = 'Bem-vindo(a) ao TasKing'
    list_emails = [email,]

    html_content = render_to_string(
        'emails/register-welcome.html',
        {
            "user": user,
            "project_name": project_name,
            "company_address": company_address,
            "action_url": action_url,
            "support_email": support_email,
            "login_url": login_url,
            "project_website": project_website,
        }
    )
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives(subject=subject, body=text_content,
                                   from_email=settings.EMAIL_HOST_USER, to=list_emails)
    email.attach_alternative(html_content, 'text/html')
    email.send()


def send_password_reset(user, email: str, project_name: str, company_address: str, action_url: str):
    subject = 'TasKing - Definir Palavra-passe'
    list_emails = [email,]

    html_content = render_to_string(
        'emails/password-reset.html',
        {
            "user": user,
            "project_name": project_name,
            "company_address": company_address,
            "action_url": action_url
        }
    )
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives(subject=subject, body=text_content,
                                   from_email=settings.EMAIL_HOST_USER, to=list_emails)
    email.attach_alternative(html_content, 'text/html')
    email.send()
