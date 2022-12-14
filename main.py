
"""import libraries"""

from typing import Dict, List, TYPE_CHECKING, Any
from datetime import datetime
from dataclasses import dataclass
from random import randint
from collections import defaultdict


@dataclass
class PersonalInfo:
    """
    Attributes:

    _id (int): Developers ID, is incremented for each instance.
    first_name (str): First name
    second_name (str): Second name
    address (str): address
    phone_number (str): Phone number
    email (str): Email
    position (int): Position
    rank (str): Rank
    salary (float): Salary
    """

    def __init__(self, _id: int, first_name: str, second_name: str, address: str, phone_number: str,
                 email: str, position: int, rank: str, salary: float):
        self.main_id = _id
        self.first_name = first_name
        self.second_name = second_name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.position = position
        self.rank = rank
        self.salary = salary

    """Getter"""
    @property
    def full_name(self):
        return self.first_name + " " + self.second_name

    """Setter"""
    @full_name.setter
    def full_name(self, fullname):
        try:
            buffer_full_name = fullname.split(" ")
            self.first_name = buffer_full_name[0]
            self.second_name = buffer_full_name[1]
        except NameError:
            print("Most likely, the data was entered incorrectly.\n It should look like this:")
            print("first_name + " " + second_name")


class Employee:
    """
    Attributes:
    personal_info (PersonalInfo): Personal info
    """

    def __init__(self, personal_info: PersonalInfo):
        self.personal_info = personal_info

    # There are two methods which should be abstract

    def calculate_salary(self) -> None:  # Use isinstance
        if isinstance(self.personal_info.salary, (int, float)):
            print(f"Monthly salary =  {self.personal_info.salary}$")
            print(f"Annual salary =  {self.personal_info.salary * 12}$")
            print(f"Annual salary with bonus 10% =  {self.personal_info.salary * 12 * 1.1}$")
        else:
            print("An error occurred.")
            print("Most likely, the Salary variable is not an INT or a FLOAT.")

    def ask_sick_leave(self, project_manager) -> bool:  # project_manager: ProjectManager
        random_int = randint(0, 10)
        if random_int == 5:
            return True
        else:
            return False


class Project:
    """
    Attributes:
        task_list (list[int]) Task list
    """

    def __init__(self, task_list: list[int]):
        self.task_list = task_list

    def get_specific_employees(self, employee_type) -> List[Employee]:
        pass


class ProjectManager(Employee):
    """
    Attributes:
    employee_requests (Any): Employee requests
    """

    def __init__(self, employee_requests: Any):
        self.employee_requests = employee_requests

    def calculate_salary(self) -> None:
        if isinstance(self.personal_info.salary, (int, float)):
            print(f"Monthly salary =  {self.personal_info.salary}$")
            print(f"Annual salary =  {self.personal_info.salary * 12}$")
            print(f"Annual salary with bonus 10% =  {self.personal_info.salary * 12 * 1.1}$")
        else:
            print("An error occurred.")
            print("Most likely, the Salary variable is not an INT or a FLOAT.")

    def discuss_progress(self, engineer: Employee) -> None:  # we will fill this method then, leave it blank.
        pass


class Developer(Employee):

    def calculate_salary(self) -> None:  # Use isinstance
        if isinstance(self.personal_info.salary, (int, float)):
            print(f"Monthly salary =  {self.personal_info.salary}$")
            print(f"Annual salary =  {self.personal_info.salary * 12}$")
            print(f"Annual salary with bonus 10% =  {self.personal_info.salary * 12 * 1.1}$")
        else:
            print("An error occurred.")
            print("Most likely, the Salary variable is not an INT or a FLOAT.")

    def ask_sick_leave(self, project_manager) -> bool:  # project_manager: ProjectManager
        random_int = randint(0, 10)
        if random_int == 5:
            return True
        else:
            return False


class AssignManagement:
    """
    Attributes:
    employee (Employee): Employee
    project (Project): Project
    """

    def __init__(self) -> None:
        self.project_employee = defaultdict(list)
        self.employee_project = defaultdict(list)

    def assign(self, employee_id, project_title) -> None:
        self.project_employee[employee_id].append(project_title)
        self.employee_project[project_title].append(employee_id)

    def unassign(self, employee_id, project_title) -> None:
        if project_title in self.project_employee and employee_id in self.employee_project:
            self.project_employee[employee_id].remove(project_title)
            self.employee_project[project_title].remove(employee_id)
        else:
            print("It is not possible to retrieve a connection that does not exist!")


class Task:
    """
    Attributes:
    _id (int): Developers ID, is incremented for each instance.
    title (str): Task name
    deadline (datetime): Deadline date
    items (List[str]): Items
    status (Any): # is_done or in_progress
    related_project (str): # project title
    """

    def __init__(self, _id: int, title: str, deadline: datetime, items: List[str], status: List[str], related_project: str):
        self.main_id = _id
        self.title = title
        self.deadline = deadline
        self.items = items
        self.status = status
        self.related_project = related_project

    def implement_item(self, item_name: str) -> str:
        self.items.append(item_name)
        return f"Added part with title {item_name}"

    def add_comment(self, comment: str) -> None:
        self.status = comment


class Assignment:
    """
    Attributes:
    received_tasks (dict[Task]): Received tasks
    """

    def __init__(self, received_tasks: dict[Task]):
        self.received_tasks = received_tasks

    def get_tasks_to_date(self, date: datetime) -> List:  # Returns all tasks before date in arguments.
        """
        Arguments:
            date: datatime
        """
        return [value for key, value in dict.items() if key <= date]


class QualityAssurance(Employee):

    def calculate_salary(self) -> None:  # Use isinstance
        if isinstance(self.personal_info.salary, (int, float)):
            print(f"Monthly salary =  {self.personal_info.salary}$")
            print(f"Annual salary =  {self.personal_info.salary * 12}$")
            print(f"Annual salary with bonus 10% =  {self.personal_info.salary * 12 * 1.1}$")
        else:
            print("An error occurred.")
            print("Most likely, the Salary variable is not an INT or a FLOAT.")

    def ask_sick_leave(self, project_manager) -> bool:  # project_manager: ProjectManager
        random_int = randint(0, 10)
        if random_int == 5:
            return True
        else:
            return False

    def add_ticket(self) -> None:  # we will fill this method then, leave it blank.
        pass


person_01 = PersonalInfo(0, "Ivan", "Dobro", "Lviv", "+380-97-676-11-22", "ivandobro@gmail.com", 6, "Junior", 1200)
print(person_01.first_name)
person_01.full_name = "Petro Duda"
print(person_01.full_name)

person_01_employee = Employee(person_01)
person_01_employee.calculate_salary()

print(person_01_employee.ask_sick_leave(person_01))

project_01 = Project([0, 1, 3, 4, 5])
task_01 = Task( 2, "Task_02", (2020, 3, 12), ["Item_01","Item_02","Item_03","Item_04"], ["is_done"], "Project_01")

managment = AssignManagement()

managment.assign(person_01.main_id, task_01.related_project)

