import requests
import json

api_key = ""
domain = ""
password = ""

# Return the tickets that are new or opend & assigned to you
# To fetch all tickets remove the filter query param
r = requests.get("https://"+ domain +".freshdesk.com/api/v2/tickets?filter=new_and_my_open", auth = (api_key, password))

if r.status_code == 200:
  print ("Request processed successfully, the response is given below")
  print (r.content)
else:
  print ("Failed to read tickets, errors are displayed below,")
  response = json.loads(r.content)
  print (response["errors"])

  print ("x-request-id : " + r.headers['x-request-id'])
  print ("Status Code : " + str(r.status_code))
