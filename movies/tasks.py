from celery import shared_task

from movies import omdb_intergration


@shared_task
def search_and_save(search):
    return omdb_intergration.search_and_save(search)
