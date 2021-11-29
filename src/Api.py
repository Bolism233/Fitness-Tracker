from typing import MutableMapping
import requests
import json
from requests.models import Response

class Api:


    def __init__(self, age = 0, weight = 0, height = 0, gender = None, activity_level = 1):

        self.age = age
        self.weight = weight
        self.height = height
        self.gender = gender
        self.activitiy_level = activity_level

    
    def bmi(self, age, weight, height, filename):

        self.url = "https://fitness-calculator.p.rapidapi.com/bmi"
        self.headers = {
            'x-rapidapi-host': "fitness-calculator.p.rapidapi.com",
            'x-rapidapi-key': "b00889a22bmsh3979cb9bd3fcb8dp1b279fjsn69211ab78ad7"
        }
        
        self.age = age
        self.weight = weight
        self.height = height
        self.filename = filename
        self.querystring = {
            "age":self.age,
            "weight":self.weight,
            "height":self.height
            }
        
        response = requests.get(self.url, headers=self.headers, params=self.querystring)
        out_file = open(f'{self.filename}.json', 'w')
        json.dump(response.json(), out_file, indent=4)
        res = json.loads(response.text)
        return res['data']['bmi']


    def calories(self,age,gender,height,weight,activity_level,loss,filename = 'Calories',):

        self.url = "https://fitness-calculator.p.rapidapi.com/dailycalorie"
        self.headers = {
            'x-rapidapi-host': "fitness-calculator.p.rapidapi.com",
            'x-rapidapi-key': "0f022dc93emsh5eb4b83a47b9176p165de5jsn277741953564"
            }

        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.activity_level = activity_level
        self.filename = filename
        self.querystring = {"age":self.age,"gender":self.gender,"height":self.height,"weight":self.weight,"activitylevel":self.activity_level}

        response = requests.get(self.url, headers=self.headers, params=self.querystring)
        out_file = open(f'{self.filename}.json', 'w')
        json.dump(response.json(), out_file, indent=4)
        res = json.loads(response.text)
        goals = res['data']['goals']
        primary_goal = [goals['maintain weight'], goals['Extreme weight loss']['calory'], goals['Weight loss']['calory'], goals['Mild weight loss']['calory'], goals['Mild weight gain']['calory'], goals['Weight gain']['calory'], goals['Extreme weight gain']['calory']]
        return primary_goal[0], primary_goal[loss]



# AGE='25'
# GENDER='male'
# HEIGHT='180'
# WEIGHT='60'
# ACTIVITY_LEVEL='level_1'
# LOSS = 6

# calories_per_day = Api().calories(AGE,GENDER,HEIGHT,WEIGHT,ACTIVITY_LEVEL,LOSS)

# for i in range(10):
#     print('')

# print(calories_per_day)
