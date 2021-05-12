import requests
import json

api_key = "yVo3CHnI7VFYP9MHST"
domain = "omniaccesssandbox"
password = "Markimoo22@@"

headers = { 'Content-Type' : 'application/json' }

ticket = {
    'subject' : 'Test API Ticket 2',
    'description' : 'This is a test',
    'email' : 'test@test.com',
    'priority' : 1,
    'status' : 2,
    'cc_emails' : ['marta.segui@omniaccess.com', 'support@omniaccesssandbox.freshdesk.com'],
    'type' : 'Request',
    'custom_fields': { 'cf_scope':'Information Technologies', 
                      'cf_service549480':'Applications',
                      'cf_area245988':'Other'  }

}

r = requests.post("https://"+ domain +".freshdesk.com/api/v2/tickets", auth = (api_key, password), headers = headers, data = json.dumps(ticket))

if r.status_code == 201:
  print ("Ticket created successfully, the response is given below") #+ r.content)
  print (r.content)
  print ("Location Header : " + r.headers['Location'])
else:
  print ("Failed to create ticket, errors are displayed below,")
  response = json.loads(r.content)
  print (response["errors"])

  print ("x-request-id : " + r.headers['x-request-id'])
  print ("Status Code : " + str(r.status_code))