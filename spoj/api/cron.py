from .final  import scraper
from django.shortcuts import render
from spoj.settings import EMAIL_HOST_USER
from django.core.mail import send_mail	

def my_cron_job():
    subject = 'Welcome to Codedigger'
    message = 'Hope you are enjoying our Problems'
    recepient = 'aaradhyaberi777@gmail.com'
    send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
    scraper()