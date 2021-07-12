from templateEngine.dao.MongoConnection import MongoConnection

class TemplatesDAO(MongoConnection):
    def __init__(self):
        super(TemplatesDAO, self).__init__()
        self.get_collection('templates')

    def getSystemTemplates(self):
        return list(self.collection.find({'customerId': 'system'}))

    def getTemplateByCustomerId(self, customerId):
        return self.collection.find_one({'customerId': customerId})
    
    def createTemplate(self, template):
        insertOneResult = self.collection.insert_one(template)
        return insertOneResult.inserted_id


