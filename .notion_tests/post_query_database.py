#Query a database from a Notion page.
#Gets data from the database with filters.

#[!] secrets.py must be created with private KEY variable.

import secrets
import requests
import json


base_url = "https://api.notion.com/v1/databases/"
database_id = "7311c70648f349b4bb963cac5c147bce"

header = {"Authorization":secrets.KEY, 
          "Notion-Version":"2021-08-16",
          "Content-Type":"application/json"}


response = requests.post(base_url + database_id + "/query",
                         headers = header)

print(json.dumps(response.json(), indent = 2))