import secrets
from notion_modules.NotionWorkspace import NotionWorkspace

personalWorkspace = NotionWorkspace(secrets.KEY)

databaseFrom_id = "7311c70648f349b4bb963cac5c147bce"
databaseTo_id = "17b68e76dacc470294be67195af8439b"

print(personalWorkspace.getDatabaseDataToPrint(databaseFrom_id))