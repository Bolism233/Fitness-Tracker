from typing import MutableMapping
import requests
import json
from requests.models import Response

class Userdata:


    def __init__(self,age=0,weight=0,height=0,gender='',activity_level=0,desired_weight=0,goal=0):
        """
        Stores user information inside the user class
        param gender
        param age
        param weight
        param height
        param desired_weight
        param activity_level
        return: None
        """

        self.age = age
        self.weight = weight
        self.height = height
        self.gender = gender
        self.activity_level = activity_level
        self.desired_weight = desired_weight
        self.goal = goal

    
    def bmi(self,weight,filename):
        '''
        Finds user's BMI and desired BMI
        param age: age
        param weight: weight
        param height: height
        param filename: name of json file that BMI info will be stored in
        return: user's BMI
        '''

        self.url = "https://fitness-calculator.p.rapidapi.com/bmi"
        self.headers = {
            'x-rapidapi-host': "fitness-calculator.p.rapidapi.com",
            'x-rapidapi-key': "b00889a22bmsh3979cb9bd3fcb8dp1b279fjsn69211ab78ad7"
        }
        
        self.filename = filename
        self.querystring = {
            "age":self.age,
            "weight":weight,
            "height":self.height
            }
        
        response = requests.get(self.url, headers=self.headers, params=self.querystring)
        out_file = open(f'src/{self.filename}.json', 'w')
        json.dump(response.json(), out_file, indent=4)
        res = json.loads(response.text)
        return res['data']['bmi']


    def calories(self,loss,filename = 'Calories'):
        '''
        Determines how many calories the user should intake daily in order to gain, lose, or maintain weight based on activity level
        '''

        self.url = "https://fitness-calculator.p.rapidapi.com/dailycalorie"
        self.headers = {
            'x-rapidapi-host': "fitness-calculator.p.rapidapi.com",
            'x-rapidapi-key': "0f022dc93emsh5eb4b83a47b9176p165de5jsn277741953564"
            }

        self.filename = filename
        self.querystring = {
            "age":self.age,
            "gender":self.gender,
            "height":self.height,
            "weight":self.weight,
            "activitylevel":self.activity_level}

        response = requests.get(self.url, headers=self.headers, params=self.querystring)
        out_file = open(f'src/{self.filename}.json', 'w')
        json.dump(response.json(), out_file, indent=4)
        res = json.loads(response.text)
        goals = res['data']['goals']
        primary_goal = [goals['maintain weight'], goals['Extreme weight loss']['calory'], goals['Weight loss']['calory'], goals['Mild weight loss']['calory'], goals['Mild weight gain']['calory'], goals['Weight gain']['calory'], goals['Extreme weight gain']['calory']]
        return primary_goal[0], primary_goal[loss]

    # def macronutrients(self,filename):
    #     '''
        
    #     '''
    #     self.url = "https://fitness-calculator.p.rapidapi.com/macrocalculator"
    #     self.headers = {
    #         'x-rapidapi-host': "fitness-calculator.p.rapidapi.com",
    #         'x-rapidapi-key': "0f022dc93emsh5eb4b83a47b9176p165de5jsn277741953564"
    #         }

    #     self.filename = filename
    #     self.querystring = {
    #         "age":"25",
    #         "gender":"male",
    #         "height":"180",
    #         "weight":"70",
    #         "activitylevel":"5",
    #         "goal":"extremelose"
    #         }
    #     self.querystring = {
    #         "age":self.age,
    #         "gender":self.gender,
    #         "height":self.height,
    #         "weight":self.weight,
    #         "activitylevel":self.activity_level,
    #         "goal":self.goal
    #     }

    #     response = requests.request("GET", url, headers=headers, params=querystring)

    #     print(response.text)
        