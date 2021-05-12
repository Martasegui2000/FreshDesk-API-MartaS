import requests
import json

api_key = "yVo3CHnI7VFYP9MHST"
domain = "omniaccesssandbox"
password = "Markimoo22@@"

agent_info = { "name" : "Test API User2", 
                "email" : "test_api_user2@example.com",
                "ticket_scope" :  1 #1-->Global Access, 2-->Group Access, 3-->Restricted Access
                "occasional" : "true",
                "group_ids" : "",
                #"role_ids" : "",
                #"skill_ids" : ""
                }
headers = { "Content-Type" : "application/json" }

r = requests.post("https://"+ domain +".freshdesk.com/api/v2/agents/", auth = (api_key, password), data = json.dumps(agent_info), headers = headers)

if r.status_code == 201:
  print ("Agent created successfully, the response is given below") #+ r.content
  print (r.content)
  print ("Location Header : " + r.headers['Location'])
else:
  print ("Failed to create agent, errors are displayed below,")
  response = json.loads(r.content)
  print (response["errors"])

  print ("x-request-id : " + r.headers['x-request-id'])
  print ("Status Code : " + str(r.status_code))