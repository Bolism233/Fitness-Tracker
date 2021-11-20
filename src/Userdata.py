class Userdata:
    def __init__(self, gender = '0' , age = '0', weight = '0', height = '0', desired_weight = '0', activity_level = '0'):
        """
        Stores user information inside the user class
        :param gender
        :param age
        :param weight
        :param height
        :param desired_weight
        :param activity_level
        .:return: None
        """
        self.gender = gender
        self.age = age
        self.height = height
        self.weight = weight
        self.activity_level = activity_level
        self.desired_weight = desired_weight
        self.bmi = bmi_index
        self.calories = calories

    def bmi(self, bmi_index):
        """
        Stores user object's bmi number
        :param bmi_index:
        :return: None
        """
        self.bmi = bmi_index

    def calorie(self, calories):
        """
        Stores user object's calorie
        :param calories:
        :return:
        """
        self.calorie = calories
