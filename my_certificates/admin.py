from django.contrib import admin
from my_certificates.models import Certificates

class CertificatesAdmin(admin.ModelAdmin):
     pass
    
    
admin.site.register(Certificates, CertificatesAdmin)