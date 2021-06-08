import requests
import json

api_key = ""
domain = ""
password = ""

# Id of the contact to be updated
contact_id = 'CONTACT_ID'

contact_info = { "priority" : "Administrator" }
headers = { "Content-Type" : "application/json" }

r = requests.put("https://"+ domain +".freshdesk.com/api/v2/contacts/"+contact_id, auth = (api_key, password), data = json.dumps(contact_info), headers = headers)

if r.status_code == 200:
  print ("Contact updated successfully, the response is given below")
  print (r.content)
else:
  print ("Failed to update contact, errors are displayed below,")
  response = json.loads(r.content)
  print (response["errors"])

  print ("x-request-id : " + r.headers['x-request-id'])
  print ("Status Code : " + r.status_code)
