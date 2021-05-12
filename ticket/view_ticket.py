import requests
import json as json

api_key = "yVo3CHnI7VFYP9MHST"
domain = "omniaccesssandbox"
password = "Markkimoo22@@"

# Id of the ticket to be updated
ticket_id = '1042'

r = requests.get("https://"+ domain +".freshdesk.com/api/v2/tickets/"+ticket_id, auth = (api_key, password))

if r.status_code == 200:
  print ("Request processed successfully, the response is given below") #+ r.content)
  print (r.content)
else:
  print ("Failed to read ticket, errors are displayed below,")
  response = json.loads(r.content)
  print (response["errors"])

  print ("x-request-id : " + r.headers['x-request-id'])
  print ("Status Code : " + str(r.status_code))