from django.test import TestCase


def projecthomepage(request):
    return render(request, 'adminapp/projecthomepage.html')
