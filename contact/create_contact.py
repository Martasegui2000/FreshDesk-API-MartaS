import requests
import json

api_key = ""
domain = ""
password = ""

contact_info = { "name" : "Test API User3", 
                 "email" : "test_api_user3@example.com",
                 "job_title" : "",
                 #"avatar" : "" #Maximum file size is 5MB
                 #"company_id" : ,
                 #"other_companies" :,
                 #"unique_external_id" : "",
                 #"custom_fields" : {"type":"", "department":""}
                 }
headers = { "Content-Type" : "application/json" }

r = requests.post("https://"+ domain +".freshdesk.com/api/v2/contacts", auth = (api_key, password), data = json.dumps(contact_info), headers = headers)

if r.status_code == 201:
  print ("Contact created successfully, the response is given below") #+ r.content
  print (r.content)
  print ("Location Header : " + r.headers['Location'])
else:
  print ("Failed to create contact, errors are displayed below,")
  response = json.loads(r.content)
  print (response["errors"])

  print ("x-request-id : " + r.headers['x-request-id'])
  print ("Status Code : " + str(r.status_code))
