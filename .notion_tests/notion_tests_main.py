import secrets
from notion_modules import NotionAutomations
from notion_modules.NotionWorkspace import NotionWorkspace

databaseFrom_id = "7311c70648f349b4bb963cac5c147bce"
databaseTo_id = "17b68e76dacc470294be67195af8439b"

personalWorkspace = NotionWorkspace(secrets.KEY)
databaseFrom = personalWorkspace.addDatabase("databaseFrom", databaseFrom_id)
databaseTo = personalWorkspace.addDatabase("databaseTo", databaseTo_id)

#print(databaseFrom.getDatabaseDataToPrint())

NotionAutomations.copyEntriesBetweenDatabases(databaseFrom, databaseTo)