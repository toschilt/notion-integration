#Retrieves a database from a Notion page.
#secrets.py must be created with private KEY variable.

import requests
import secrets

base_url = "https://api.notion.com/v1/datsabases/"

header = {"Authorization":secrets.KEY, 
          "Notion-Version":"2021-08-16"}

database_id = "7311c70648f349b4bb963cac5c147bce"

response = requests.get(base_url + database_id, 
                        headers = header)

print(response.json())