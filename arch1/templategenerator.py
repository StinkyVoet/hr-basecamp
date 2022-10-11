"""
Usually companies use a predefined templates in their emails. 
A company named XYZ would like to have a Python program that collects basic information and generates the content of the email. 
You are assigned to implement the program with the following criteria:

- There are only two templates: Job Offer and Rejection.
- For the Job Offer email, the program asks: first name, last name, job title, annual salary, starting date.
- For the Rejection email, the program asks: first name, last name, job title, with or without feedback, one feedback statement in case it is with feedback.
- The program must check valid input formats.
- First and last names: each minimum two characters and maximum ten characters; cotaining only alphabets, both starting with capital letters.
- Job title: minimum 10 characters without numbers.
- Salary: valid floating point number between (and including) 20.000,00 and 80.000,00.
- Date: only in YYYY-MM-DD format, no negative numbers, days between 1 - 31, month between 1 - 12, year only 2021 and 2022.
- Feedback: if the email contains a feedback there is an extra line in the text otherwise that line must be removed (check the example below).
- The program will generate emails until the user answers No to the More Letters? question.
- In case of invalid input from the user, the program must proper message and then repeats the question again.
- A sample execution is presented below. Use this sample execution for the templates of the emails. Your program must have only two templates:

More Letters?(Yes or No)Yes
Job Offer or Rejection?Job Offer
First Name? John
Last Name? Hartman
Job Title? Junior Python Programmer
Annual Salary? 30.500,50
Start Date?(YYYY-MM-DD) 2021-01-01
Here is the final letter to send:
Dear John Hartman, 
 After careful evaluation of your application for the position of Junior Python Programmer, 
 we are glad to offer you the job. Your salary will be 30.500,50 euro annually. 
Your start date will be on 2021-01-01. Please do not hesitate to contact us with any questions. 
Sincerely, 
HR Department of XYZ 

More Letters?(Yes or No)Yes
Job Offer or Rejection?Rejection
First Name? David
Last Name? Johanson
Job Title? Junior C++ Programmer
Feedback? (Yes or No) No
Here is the final letter to send:
Dear David Johanson, 
After careful evaluation of your application for the position of Junior C++ Programmer, 
at this moment we have decided to proceed with another candidate. 
We wish you the best in finding your future desired career. Please do not hesitate to contact us with any questions. 
Sincerely, 
HR Department of XYZ 

More Letters?(Yes or No)Yes
Job Offer or Rejection?Rejection
First Name? David
Last Name? Chan
Job Title? Software Tester
Feedback? (Yes or No) Yes
Enter your Feedback (One Statement): You have sufficient testing knowledge but we expected to see more experience in web application testing techniques.
Here is the final letter to send:
Dear David Chan, 
After careful evaluation of your application for the position of Software Tester, 
at this moment we have decided to proceed with another candidate. 
Here we would like to provide you our feedback about the interview.
You have sufficient testing knowledge but we expected to see more experience in web application testing techniques. 
We wish you the best in finding your future desired career. Please do not hesitate to contact us with any questions. 
Sincerely, 
HR Department of XYZ 

More Letters?(Yes or No)No
"""

from dataclasses import dataclass
from datetime import date, datetime
import re
import typing


@dataclass
class EmailTemplate:
    first_name: typing.Optional[str] = None
    last_name: typing.Optional[str] = None
    job_title: typing.Optional[str] = None

    @property
    def first_name(self):
        return self._first_name
    @first_name.setter
    def first_name(self, value):
        if type(value) != str: return
        if not re.match(r"^[A-Z][a-z]{1,9}$", value):
            raise Exception("First Name must be min 2 and max 10 characters, may only contain alphabetical characters and must start with a capital letter.")
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name
    @last_name.setter
    def last_name(self, value):
        if type(value) != str: return
        if not re.match(r"^[A-Z][a-z]{1,9}$", value):
            raise Exception("Last Name must be min 2 and max 10 characters, may only contain alphabetical characters and must start with a capital letter.")
        self._last_name = value

    @property
    def job_title(self):
        return self._job_title
    @job_title.setter
    def job_title(self, value):
        if type(value) != str: return
        if not re.match(r"^[A-Za-z +-]{10,}$", value):
            raise Exception("Job Title must be at least 10 characters, numbers are not allowed.")
        self._job_title = value

    def getInput(self, attr, prompt):
        while True:
            try:
                setattr(self, attr, input(prompt))
            except Exception as e:
                print(e)
                continue
            break

@dataclass
class JobOfferEmail(EmailTemplate):
    annual_salary: float = None
    start_date: typing.Optional[date] = None

    @property
    def annual_salary(self):
        return self._annual_salary
    @annual_salary.setter
    def annual_salary(self, value):
        if type(value) == property: return
        try: 
            value = float(value) 
        except ValueError: 
            raise Exception("Not a number")
        if value < 20000.00 or value > 80000.00:
            raise Exception("Annual salary must be between 20,000.00 and 80,000.00.")
        self._annual_salary = value
    
    @property
    def start_date(self):
        return self._start_date
    @start_date.setter
    def start_date(self, value):
        if type(value) != str: return
        try:
            value = datetime.strptime(value, '%Y-%m-%d').date()
        except ValueError:
            raise Exception("Invalid date. Please use format YYYY-MM-DD.")

        if value.year not in (2021, 2022):
            raise Exception("Date can only be in the years 2021 or 2022")

        self._start_date = value

    def generate(self) -> str:
        return f"""Dear {self.first_name} {self.last_name},
After careful evaluation of your application for the position of {self.job_title}, 
we are glad to offer you the job. Your salary will be {self.annual_salary} euro annually. 
Your start date will be on {self.start_date}. Please do not hesitate to contact us with any questions.  
Sincerely, 
HR Department of XYZ
"""

@dataclass
class RejectionEmail(EmailTemplate):
    feedback: typing.Optional[str] = None

    def generate(self) -> str:
        return f"""Dear {self.first_name} {self.last_name},
After careful evaluation of your application for the position of {self.job_title}, 
at this moment we have decided to proceed with another candidate.
""" + (f"""Here we would like to provide you our feedback about the interview.\n{self.feedback}""" if self.feedback != None else None) + """
We wish you the best in finding your future desired career. Please do not hesitate to contact us with any questions. 
Sincerely, 
HR Department of XYZ 
"""


def main():
    print("Email Template Generator\n")
    while True:
        match input("Job Offer or Rejection? ").lower():
            case "job offer":
                email = JobOfferEmail()
            case "rejection":
                email = RejectionEmail()
            case _:
                print("Invalid option.")
                continue
        
        email.getInput("first_name", "First name: ")
        email.getInput("last_name", "Last name: ")
        email.getInput("job_title", "Job title: ")

        if type(email) == JobOfferEmail:
            email.getInput("annual_salary", "Annual salary: ")
            email.getInput("start_date","Start date: ")
        elif type(email) == RejectionEmail:
            email.getInput("feedback", "Feedback (Leave blank for none): ")
        
        print("\n" + email.generate())

        match input("\nMore letters? ").lower():
            case "yes"|"y":
                print()
                continue
            case "no"|"n":
                break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        quit()