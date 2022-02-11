from bot_modules.google_modules.GoogleDocument import GoogleDocument

#Encapsules all manipulations for a sprint document.
class SprintDocument(GoogleDocument):

    #Constructor. Needs the path to the json credentials file
    #and the ID of the Google document.
    def __init__(self, jsonCredentials, documentID):
        super().__init__(jsonCredentials, documentID)

    def insertNewRegister(self, text):
        #Gets the last index of the document.
        documentInfo = self.retrieveAllDocumentAsJSON()
        lastIndex = documentInfo["body"]["content"][-1]["endIndex"] - 1
        
        newTextSize = len(text)
        #endIndex = lastIndex + newTextSize

        self.insertTextAtIndex(text, lastIndex)
        self.executeChanges()