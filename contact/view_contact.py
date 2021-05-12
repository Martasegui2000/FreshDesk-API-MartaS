import requests
import json

api_key = "yVo3CHnI7VFYP9MHST"
domain = "omniaccesssandbox"
password = "Markimoo22@@"

contact_id = '50000008661831'

r = requests.get("https://"+ domain +".freshdesk.com/api/v2/contacts/"+contact_id, auth=(api_key, password))

if r.status_code == 200:
  print ("Request processed successfully, the response is given below") #+ r.content)
  print (r.content)
else:
  print ("Failed to read contact, errors are displayed below,")
  response = json.loads(r.content)
  print (response["errors"])

  print ("x-request-id : " + r.headers['x-request-id'])
  print ("Status Code : " + str(r.status_code))