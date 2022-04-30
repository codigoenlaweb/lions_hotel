from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

def create_reservation_email(self, email_of_person, confirmation_code):
    # get template 
    template = get_template("email/create_reservation.html")
    
    context = {
        "confirmation_code":confirmation_code
    }
    # conte para el template
    content = template.render(context)
    
    # creating estructure email
    email_create = EmailMultiAlternatives(
        "Confirm your reservation at lions hotel",
        "Confirm your reservation at lions hotel",
        settings.EMAIL_HOST_USER,
        [email_of_person]
    )

    # email with content
    email_create.attach_alternative(content, 'text/html')
    
    # email send
    email_create.send()
    
# localizador of reservation email
def localizador_email(self, email_of_person, localizador):
    # get template 
    template = get_template("email/localizador.html")
    
    context = {
        "localizador":localizador
    }
    # conte para el template
    content = template.render(context)
    
    # creating estructure email
    email_create = EmailMultiAlternatives(
        "Unique locator for your reservation",
        "Unique locator for your reservation",
        settings.EMAIL_HOST_USER,
        [email_of_person]
    )

    # email with content
    email_create.attach_alternative(content, 'text/html')
    
    # email send
    email_create.send()