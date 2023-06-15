import employee_info

employee_data = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
]
def test_get_employees_by_age_range():
    result = []
    result = employee_info.get_employees_by_age_range(28,38)

    assert (result == [{'age': 30, 'department': 'Sales', 'name': 'John', 'salary': 50000},
 {'age': 35, 'department': 'Engineering', 'name': 'Chloe', 'salary': 70000},
 {'age': 32, 'department': 'Engineering', 'name': 'Mike', 'salary': 65000}])

def test_calculate_average_salary():
    result = employee_info.calculate_average_salary()

    assert (result == 60166.666666666664)

def test_get_employees_by_dept():
    result = employee_info.get_employees_by_dept('Sales')

    assert (result == {'age': 30, 'department': 'Sales', 'name': 'John', 'salary': 50000},
 {'age': 40, 'department': 'Sales', 'name': 'Peter', 'salary': 60000})
