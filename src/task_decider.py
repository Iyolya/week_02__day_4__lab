class Task():

    def __init__(self, description, duration ):
        self.description = description
        self.duration = duration

    
    def decide_tasks(self, task_1, task_2):
        
        if task_1 == wash_dishes and task_2 == cook_dinner:
            return task_1.description
        elif task_1 == cooking_dinner and task_2 == cleaning_windows:
            return task_1.description
        elif task_1 == cleaning_windows and task_2 == cooking_dinner:
            return task_1.description

    # def decide_task(self, task_1, task_2):
    #     if task_1 == wash_dishes and task_2 == cook_dinner:
    #         return wash_dishes.description