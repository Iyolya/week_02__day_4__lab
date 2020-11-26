import unittest

from src.task_decider import *

class TestTask_Decider(unittest.TestCase):

    def setUp(self):
        self.wash_dishes = Task("wash dishes", 20)
        self.cooking_dinner = Task("cooking dinner", 30) 
        self.cleaning_windows = Task("cleaning windows", 40)
   
    def test_wash_dishes_preferred_over_cook_dinner(self):
       #wash_dishes_preferred_over_cook_dinner(self, was, task_2)
        self.assertEqual("wash dishes", self.wash_dishes.description) #wash_dishes_preferred_over_cook_dinner(self, wash_dishes, cooking_dinner))

        # result = wash_dishes_preferred_over_cook_dinner(wash_dishes, cooking_dinner)
        # self.assertEqual("wash dishes", result)

    # def test_cook_dinner_preferred_clean_windows(self):
    #     self.assertEqual("cooking dinner", self.task.cooking_dinner)

    # def test_cleaning_windows_preferred_over_wash_dishes(self):
    #     self.assertEqual("cleaning windows", self.task.cleaning_windows)
