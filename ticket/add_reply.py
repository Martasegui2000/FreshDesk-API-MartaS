import requests
import json

api_key = ""
domain = ""
password = ""

# id of the ticket to add a note
ticket_id = '57'

headers = { 'Content-Type' : 'application/json' }

note = {
  # 'body' : 'Test reply'
}

r = requests.post("https://"+ domain +".freshdesk.com/api/v2/tickets/"+ticket_id+"/reply", auth = (api_key, password), headers = headers, data = json.dumps(note))

if r.status_code == 201:
  print ("Reply added successfully, the response is given below") #+ r.content
  print (r.content)
  print ("Location Header: " + r.headers['Location'])
else:
  print ("Failed to add reply, errors are displayed below,")
  response = json.loads(r.content)
  print (response["errors"])

  print ("x-request-id : " + r.headers['x-request-id'])
  print ("Status Code : " + str(r.status_code))
