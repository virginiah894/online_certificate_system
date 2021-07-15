from io import BytesIO
import matplotlib.pyplot as plt
import base64


from django.http import HttpResponse
from django.template.loader import get_template
from .emailutils import  email_change
from django.views.generic import View


class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('invoice.html')
        context = {
            "certificate_id": 123,
            "Name": "John Cooper",
            "today": "Today",
        }
        html = template.render(context)
        pdf = render_to_pdf('certficate.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Certificate_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
                email_change(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")

def get_graph():
    safety = BytesIO()
    plt.savefig(safety, format ='png')
    safety.seek(0)
    image_png = safety.getvalue()
    graph = graph.decode('utf-8')
    safety.close()
    return graph





def get_plot(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(12,6))
    plt.title('Current Statistics of Students Certificates')
    plt.plot(x,y)
    plt.xtics(rotation =45)
    plt.xlabel('students')
    plt.ylabel('courses')
    plt.tight_layout()

    graph = get_graph()
    return graph
