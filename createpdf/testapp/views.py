from django.shortcuts import render,redirect
#from django.views import View
import os
from django.http import HttpResponse
from createpdf import utils
from . import forms
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.conf import settings
from django.template import Context



def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    # use short variable names
    sUrl = settings.STATIC_URL      # Typically /static/
    sRoot = settings.STATIC_DIRS    # Typically /home/userX/project_static/

    # convert URIs to absolute system paths
    if uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))
    else:
        return uri  # handle absolute uri (ie: http://some.tld/foo.png)

    # make sure that file exists
    if not os.path.isfile(path):
        raise Exception(
            'media URI must start with %s or %s' % (sUrl, mUrl)
        )
    return path

def render_pdf(request):
    try:
        data={"fname":request.session['fname'],
        "lname":request.session['lname'],
        "address":request.session['address'],
        "number":request.session['number'],
        "email":request.session['email'],
        "education":request.session['education'],
        "skills":request.session['skills'],
        "pdetails":request.session['pdetails'],
        "project":request.session['project'],
        "declaration":request.session['declaration']
        }

    except:
        form=forms.ResumeForm()
        return render(request,'testapp/form.html', {"error":True,"form":form})
    
    template_path = 'testapp/pdf_template.html'

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'

    template = get_template(template_path)
    html = template.render(data)

    pisaStatus = pisa.pisaDocument(html, dest=response,encoding='utf8', link_callback=link_callback)
    if pisaStatus.err:
        return HttpResponse('We had some errors with code %s <pre>%s</pre>' % (pisaStatus.err,html))
    else:
        return response


def form_view(request):
    form=forms.ResumeForm()
    if request.method == 'POST': 
        request.session['fname']=request.POST.get('fname')
        request.session['lname']=request.POST.get('lname')
        request.session['address']=request.POST.get('address')
        request.session['number']=request.POST.get('number')
        request.session['email']=request.POST.get('email')
        request.session['education']=request.POST.get('education')
        request.session['pdetails']=request.POST.get('pdetails')
        request.session['skills']=request.POST.get('skills')
        request.session['project']=request.POST.get('project')
        request.session['declaration']=request.POST.get('declaration')
    return render(request,'testapp/form.html')


