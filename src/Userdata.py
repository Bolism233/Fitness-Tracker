import requests
import json

class Userdata:


    def __init__(self,age=0,weight=0,height=0,gender='',activity_level=0,desired_weight=0,intensity=0):
        """
        Stores user information inside the user class
        param gender: user gender input
        param age: age input
        param weight: user weight input
        param height: user height input
        param desired_weight: user desired_weight input
        param activity_level: user desired_level input
        param intensity: user intensity input
        return: None
        """
        self.age = age
        self.weight = weight
        self.height = height
        self.gender = gender
        self.activity_level = activity_level
        self.desired_weight = desired_weight
        self.intensity = intensity
        self.url = "https://fitness-calculator.p.rapidapi.com/"
        self.headers = {
            'x-rapidapi-host': "fitness-calculator.p.rapidapi.com",
            'x-rapidapi-key': "b00889a22bmsh3979cb9bd3fcb8dp1b279fjsn69211ab78ad7"
        }

    def bmi(self,weight,filename):
        '''
        Finds user's BMI and desired BMI
        param filename: name of json file that BMI info will be stored in
        return: user's BMI
        '''
        self.url = "https://fitness-calculator.p.rapidapi.com/bmi"
        self.filename = filename
        self.querystring = {
            "age":self.age,
            "weight":weight,
            "height":self.height
            }
        response = requests.get(self.url, headers=self.headers, params=self.querystring)
        res = response.json()
        out_file = open(f'assets/{self.filename}.json', 'w')
        json.dump(res, out_file, indent=4)
        out_file.close()
        return res['data']['bmi']


    def calories(self,filename = 'Calories'):
        '''
        Determines how many calories the user should intake daily in order to gain, lose, or maintain weight based on activity level
        param filename: name of json file that calorie info will be stored in
        return: how many calories a day the user should be eating to maintain weight and to reach their target weight
        '''
        self.url = "https://fitness-calculator.p.rapidapi.com/dailycalorie"
        self.filename = filename
        self.querystring = {
            "age":self.age,
            "gender":self.gender,
            "height":self.height,
            "weight":self.weight,
            "activitylevel":f"level_{self.activity_level}"
            }

        response = requests.get(self.url, headers=self.headers, params=self.querystring)
        res = response.json()
        out_file = open(f'assets/{self.filename}.json', 'w')
        json.dump(res, out_file, indent=4)
        out_file.close()
        goals = res['data']['goals']

        primary_goal = ["maintain weight", 'Mild weight loss', 'Weight loss', 'Extreme weight loss', 'Mild weight gain', 'Weight gain', 'Extreme weight gain']
        return goals["maintain weight"], goals[primary_goal[int(self.intensity)]]["calory"]


    def macronutrients(self,filename="Macronutrients"):
        """
        Determines the optimal ratios of macronutrients that the user should consume, and generates 4 different plans.
        :param filename: name of the file that will be created that holds all the macronutrient data
        :return: 4 plans with different ratios of macronutrients.
        """
        self.url = "https://fitness-calculator.p.rapidapi.com/macrocalculator"
        macro_goal = ['maintain','mildlose','weightlose','extremelose','mildgain','weightgain','extremegain']

        self.filename = filename
        self.querystring = {
            "age":self.age,
            "gender":self.gender,
            "height":self.height,
            "weight":self.weight,
            "activitylevel":self.activity_level,
            "goal":macro_goal[int(self.intensity)]
        }

        response = requests.get(self.url, headers=self.headers, params=self.querystring)
        res = response.json()
        out_file = open(f'assets/{self.filename}.json', 'w')
        json.dump(res, out_file, indent=4)
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
        self.intensity = control.textboxes.sprites()[5].user_text
        if self.intensity == '': self.intensity = 0            
        if self.desired_weight > self.weight:
            intensity = int(self.intensity)
            intensity += 3
            self.intensity = intensity
        self.gender = control.textboxes.sprites()[6].user_text.lower()
