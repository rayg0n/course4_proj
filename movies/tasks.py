from celery import shared_task

from movies import omdb_intergration
from django.core.mail import mail_admins


@shared_task
def search_and_save(search):
    return omdb_intergration.search_and_save(search)

@shared_task
def notify_of_new_search_term(search_term):
    mail_admins("New Search Term", f"A new search term was used: '{search_term}'")

