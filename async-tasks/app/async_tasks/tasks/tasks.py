from celery import shared_task
from time import sleep


@shared_task()
def compute():
    # Simulation of a task to take long
    sleep(20)
