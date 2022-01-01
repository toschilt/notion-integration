#Query a database from a Notion page.
#Gets data from the database with filters.

#[!] secrets.py must be created with private KEY variable.

import secrets
import requests
import json

base_url_db = "https://api.notion.com/v1/databases/"
base_url_post = "https://api.notion.com/v1/pages"

headerGetData = {"Authorization":secrets.KEY, 
                 "Notion-Version":"2021-08-16",
                 "Content-Type":"application/json"}

#Gets the "to" database JSON
rTableTo = requests.post(base_url_db + databaseTo_id + "/query",
                         headers = headerGetData)
json_rTableTo = rTableTo.json()

#Gets the "from" database JSON
rTableFrom = requests.post(base_url_db + databaseFrom_id + "/query",
                           headers = headerGetData)
json_rTableFrom = rTableFrom.json()


dataModel = {
    "parent": {
        "database_id": databaseTo_id
    },
    "properties": {
        "Name": {
            "title": [
                {
                    "text": {
                        "content": "aloooooooooooo"
                    }
                }
            ]
        },
        "Tags": {
            "type": "multi_select",
            "multi_select": [
                {
                    "name": "b1",
                }
            ]
        }
    }
}

response_create = requests.post(base_url_post,
                                headers = headerGetData,
                                data = json.dumps(dataModel))

print(json.dumps(response_create.json(), indent = 2))


#for row in json_rTableFrom["results"]:
#    data = dataModel
#    data["properties"] = row["properties"]
#
#    print(json.dumps(data, indent = 2))
#
#   response_create = requests.post(base_url_post,
#                                headers = headerGetData,
#                                data = json.dumps(data))
#
#    print(response_create)