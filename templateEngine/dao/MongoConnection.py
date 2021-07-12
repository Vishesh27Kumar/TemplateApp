from pymongo import MongoClient
from django.conf import settings


class MongoConnection(object):
    def __init__(self):
        DATABASES = settings.DATABASES
        self.client = MongoClient(host=[DATABASES['TemplateEngine']['HOST']], username=DATABASES['TemplateEngine']['USERNAME'], password=DATABASES['TemplateEngine']['PASSWORD'],
                             authSource=DATABASES['TemplateEngine']['AUTH_DATABASE'])
        self.db = self.client[DATABASES['TemplateEngine']['DATABASE']]

    def get_collection(self, name):
        self.collection = self.db[name]