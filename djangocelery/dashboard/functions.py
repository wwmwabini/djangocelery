import pdfkit, secrets, time
from django.http import HttpResponse
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.conf import settings

def html_to_pdf(user_id):
    time.sleep(30) # introduce a delay

    download_file_name="users-"+secrets.token_hex(8)+".pdf"
    media_root = settings.MEDIA_ROOT
    output_path = media_root + "/" + download_file_name

    template = get_template('dashboard/index.html')
    context = {
        'data': User.objects.all(),
        'user': User.objects.get(id=user_id)
    }
    html = template.render(context)

    # Configure PDFKit with the wkhtmltopdf path (adjust as needed)
    config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')

    # Generate the PDF
    pdf = pdfkit.from_string(html, output_path, configuration=config)

    # Create a response with appropriate content type and filename
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename='+download_file_name

    return response
