import requests
import json
url = "https://fitness-calculator.p.rapidapi.com/bmi"
querystring = {"age":"19","weight":"65","height":"180"}
headers = {
'x-rapidapi-host': "fitness-calculator.p.rapidapi.com",
'x-rapidapi-key': "b00889a22bmsh3979cb9bd3fcb8dp1b279fjsn69211ab78ad7"
}

response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)
res = json.loads(response.text)
print(res["data"]["bmi"])