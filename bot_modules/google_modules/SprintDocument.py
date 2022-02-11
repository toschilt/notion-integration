from bot_modules.google_modules.GoogleDocument import GoogleDocument

#Encapsules all manipulations for a sprint document.
class SprintDocument(GoogleDocument):

    #Constructor. Needs the path to the json credentials file
    #and the ID of the Google document.
    def __init__(self, jsonCredentials, documentID):
        super().__init__(jsonCredentials, documentID)

    #Insert a new sprint register. Needs the date and text.
    def insertNewRegister(self, date, text):
        self.skipLine()
        self.skipLine()
        self.insertTextAtLastIndex(str(date))
        self.skipLine()
        self.insertTextAtLastIndex(text)
        self.executeChanges()