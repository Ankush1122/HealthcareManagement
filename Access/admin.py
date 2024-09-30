from django.contrib import admin
from .models import AccessPermission, EmergencyAccessLog, RecordDeletionRequest, InsuranceAccessRequest, LegalAccessRequest

admin.site.register(AccessPermission)
admin.site.register(EmergencyAccessLog)
admin.site.register(RecordDeletionRequest)
admin.site.register(InsuranceAccessRequest)
admin.site.register(LegalAccessRequest)
