from django.db import models

from cumulus.storage import CloudFilesStorage

cloudfiles_storage = CloudFilesStorage()

class Upload(models.Model):
    "A dummy model to use for tests."
    def upload_to(self, name):
        return '%s/%s' % (self.upload_to, name)
    image = models.ImageField(storage=cloudfiles_storage, upload_to=upload_to)
    document = models.FileField(storage=cloudfiles_storage, upload_to=upload_to)
    custom = models.FileField(storage=cloudfiles_storage, upload_to=upload_to)

    class Meta:
        abstract = True

class Thing(Upload):

    upload_to = 'cumulus-tests'

class Second(Upload):
    upload_to = 'secondcontainer:cumulus-second-tests'
