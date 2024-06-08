class Employee:
    employee_count = 0

    def __init__(self, employee_id: str, name: str):
        if not self.is_valid_id(employee_id):
            raise ValueError("Invalid employee ID format. Must be a string of digits.")
        self.employee_id = employee_id
        self.name = name
        Employee.increment_count()

    @classmethod
    def increment_count(cls) -> None:
        cls.employee_count += 1

    @classmethod
    def get_employee_count(cls) -> int:
        return cls.employee_count

    @staticmethod
    def is_valid_id(employee_id: str) -> bool:
        return employee_id.isdigit()
try:
    emp1 = Employee("12345", "John Doe")
    emp2 = Employee("67890", "Jane Smith")
    print(f"Total employees: {Employee.get_employee_count()}")  
    emp3 = Employee("12A45", "Invalid ID Employee")
except ValueError as e:
    print(e)