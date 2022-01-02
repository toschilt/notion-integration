from notion_modules.NotionWorkspace import NotionWorkspace
from notion_modules.NotionDatabase import NotionDatabase
import json

# Resets the newPageData dictionary to insert a new entry.
def resetNewPageData(databaseTo):
    defaultPageData = {
        "parent": {
            "database_id": databaseTo.id
        },
        "properties": {}
    }

    return defaultPageData


# Search the attributes from the "databaseFrom" database
# and copy them to the "databaseTo" database.
# Both databases has to have the same attribute structure.
def copyEntriesBetweenDatabases(databaseFrom, databaseTo):
    #Getting info prom the "databaseFrom" database. 
    databaseFromData = databaseFrom.getDatabaseDataInJSON()
    entries = databaseFromData["results"]

    for entry in entries:
        #Initialize the data dictionary for page creation.
        newPageData = resetNewPageData(databaseTo)

        # For each entry of the database...
        properties = entry["properties"]

        for prop in properties:
            # For each attribute of the entry...
            newPageData["properties"][prop] = properties[prop]

            # In portuguese, the next few code lines are called "GAMBIARRA".
            # TODO Is there a better way to remove unwanted properties?
            if "id" in newPageData["properties"][prop]:
                del newPageData["properties"][prop]["id"]

            if newPageData["properties"][prop]["type"] == "multi_select":
                del newPageData["properties"][prop]["multi_select"][0]["id"]
                del newPageData["properties"][prop]["multi_select"][0]["color"]

        #TODO For many entries, the request frequency can be too high. 
        print(json.dumps(databaseTo.insertEntry(newPageData).json(), indent = 2))