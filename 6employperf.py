class EmployeeEvaluation:
    def __init__(self):
        self.employee_ratings = {}

    def evaluate_performance(self, employee_name, rating):
        self.employee_ratings[employee_name] = rating

    def get_performance(self, employee_name):
        return self.employee_ratings.get(employee_name, "No evaluation found.")

evaluation_system = EmployeeEvaluation()
evaluation_system.evaluate_performance("John Doe", 85)
evaluation_system.evaluate_performance("Jane Smith", 90)

print("John's Performance:", evaluation_system.get_performance("John Doe"))
print("Jane's Performance:", evaluation_system.get_performance("Jane Smith"))
