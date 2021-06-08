import requests
import json

api_key = ""
domain = ""
password = ""

#agent_id = '1080007544991'
#params = (
#    ('email', 'mail@mail.com'),
#)

#Filter per ID agent
#r = requests.get("https://"+ domain +".freshdesk.com/api/v2/agents/"+agent_id, auth=(api_key, password))

#Filter per email agent
#r = requests.get("https://"+ domain +".freshdesk.com/api/v2/agents/",params=params, auth=(api_key, password))

if r.status_code == 200:
  print ("Request processed successfully, the response is given below") #+ r.content)
  print (r.content)
else:
  print ("Failed to read agent, errors are displayed below,")
  response = json.loads(r.content)
  print (response["errors"])

  print ("x-request-id : " + r.headers['x-request-id'])
  print ("Status Code : " + str(r.status_code))
