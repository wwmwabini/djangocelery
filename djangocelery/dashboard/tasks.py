from .functions import html_to_pdf
from celery import shared_task

@shared_task()
def background_html_to_pdf_task(user_id):
    html_to_pdf(user_id)
    return "File Ready for Download"