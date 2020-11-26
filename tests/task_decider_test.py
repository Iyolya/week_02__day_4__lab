import unittest

from src.task_decider import Task

class TestTask_Decider(unittest.TestCase):

    def setUp(self):
        self.wash_dishes = Task("wash dishes", 20)
        self.cooking_dinner = Task("cooking dinner", 30) 
        self.cleaning_windows = Task("cleaning windows", 40)


    def wash_dishes_has_description(self):
        self.assertEqual("wash dishes", self.wash_dishes.description)

    def cooking_dinner_has_description(self):
        self.assertEqual("cooking dinner", self.cooking_dinner.description)
   
    def cleaning_windows_has_description(self):
        self.assertEqual("cleaning windows", self.cleaning_windows.description)


    def test_wash_dishes_preferred_over_cook_dinner(self):
        #decide_tasks(wash_dishes, cooking_dinner)
        self.assertEqual("wash dishes", self.decide_tasks(wash_dishes, cooking_dinner)) 

    def test_cook_dinner_preferred_clean_windows(self):
        self.assertEqual("cooking dinner", self.cooking_dinner.description)

    def test_cleaning_windows_preferred_over_wash_dishes(self):
        self.assertEqual("cleaning windows", self.cleaning_windows.description)

        
