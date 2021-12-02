import requests
import json

class Userdata:


    def __init__(self,age=0,weight=0,height=0,gender='',activity_level=0,desired_weight=0,intensity=0):
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
        self.intensity = intensity

    
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
        out_file = open(f'assets/{self.filename}.json', 'w')
        json.dump(response.json(), out_file, indent=4)
        res = json.loads(response.text)
        out_file.close()
        return res['data']['bmi']


    def calories(self,filename = 'Calories'):
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
            "activitylevel":f"level_{self.activity_level}"
            }

        response = requests.get(self.url, headers=self.headers, params=self.querystring)
        out_file = open(f'assets/{self.filename}.json', 'w')
        json.dump(response.json(), out_file, indent=4)
        res = json.loads(response.text)
        out_file.close()
        goals = res['data']['goals']
        
        # if self.desired_weight > self.weight:
        #     self.intensity += 1
        
        primary_goal = ["maintain weight", 'Mild weight loss', 'Weight loss', 'Extreme weight loss', 'Mild weight gain', 'Weight gain', 'Extreme weight gain']
        # print(self.intensity)
        return goals["maintain weight"], goals[primary_goal[self.intensity]]["calory"]


    def macronutrients(self,filename="macronutrients"):
        '''
        
        '''

        self.url = "https://fitness-calculator.p.rapidapi.com/macrocalculator"
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
            "activitylevel":self.activity_level,
            "goal":self.goal
        }

        response = requests.get(self.url, headers=self.headers, params=self.querystring)
        out_file = open(f'assets/{self.filename}.json', 'w')
        json.dump(response.json(), out_file, indent=4)
        res = json.loads(response.text)
        goals = res['data']
        out_file.close()
        return goals


    def saveData(self,control):
        '''
        
        '''

        self.height = control.textboxes.sprites()[0].user_text
        self.age = control.textboxes.sprites()[1].user_text
        self.weight = control.textboxes.sprites()[2].user_text
        self.activity_level = control.textboxes.sprites()[3].user_text
        self.desired_weight = control.textboxes.sprites()[4].user_text
        self.intensity = int(control.textboxes.sprites()[5].user_text)
        self.gender = control.textboxes.sprites()[6].user_text.lower()

# test=Userdata(18,60,180,"male",2,70,1)
# print(test.bmi())
# print(test.calories())
