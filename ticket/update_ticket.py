import requests
import json

api_key = "yVo3CHnI7VFYP9MHST"
domain = "omniaccesssandbox"
password = "Markimoo22@@"

# Id of the ticket to be updated
ticket_id = '57'

headers = { 'Content-Type' : 'application/json' }

ticket = {
  'subject' : 'Updated Title',
  'description' : 'Updated description',
  'priority' : 3,
}

r = requests.put("https://"+ domain +".freshdesk.com/api/v2/tickets/"+ticket_id, auth = (api_key, password), headers = headers, data = json.dumps(ticket))

if r.status_code == 200:
  print ("Ticket updated successfully, the response is given below") #+ r.content
  print (r.content)
else:
  print ("Failed to update ticket, errors are displayed below,")
  response = json.loads(r.content)
  print (response["errors"])

  print ("x-request-id : " + r.headers['x-request-id'])
  print ("Status Code : " + r.status_code)