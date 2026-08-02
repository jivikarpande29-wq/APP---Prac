# ==========================================================
# Dynamic Report Generator using Decorators, Class Methods,
# Static Methods and Magic Methods
# ==========================================================


# Decorator Function
def report_decorator(func):
    def wrapper(*args, **kwargs):
        print("=" * 60)
        print("DYNAMIC REPORT GENERATOR".center(60))
        print("=" * 60)
        # Call the original function
        func(*args, **kwargs)
        print("=" * 60)
        print("END OF REPORT".center(60))
        print("=" * 60)

    return wrapper


# Report Class
class Report:
    # Class Variable (Shared by all objects)
    company_name = "ABC Technologies Pvt. Ltd."

    # Constructor
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.contents = []

    # Instance Method
    def add_content(self, text):
        self.contents.append(text)

    # Class Method
    @classmethod
    def change_company(cls, new_company):
        cls.company_name = new_company

    # Static Method
    @staticmethod
    def line():
        print("-" * 60)

    # Magic Method
    def __str__(self):
        return f"Report Title : {self.title}\nAuthor : {self.author}"

    # Magic Method
    def __len__(self):
        return len(self.contents)

    # Decorated Method
    @report_decorator
    def display_report(self):
        print("Company :", Report.company_name)
        print(self)
        Report.line()
        print("Report Contents:")
        for i, item in enumerate(self.contents, start=1):
            print(f"{i}. {item}")
        Report.line()
        print("Total Sections :", len(self))


# ==========================================================
# Interactive User Input Driven Execution
# ==========================================================


def generate_report_1():
    r1 = Report("Advanced Python Practical Report", "Mandar Joshi")
    r1.add_content("Completed Experiment No. 2 successfully.")
    r1.add_content(
        "Implemented Decorators, Class Methods, Static Methods and Magic Methods."
    )
    r1.add_content("Learned Object-Oriented Programming concepts.")
    r1.add_content("Report prepared by Mandar Joshi.")
    r1.display_report()


def generate_report_2():
    # Demonstrating class method to change company name dynamically
    Report.change_company("MIT ADT University")

    r2 = Report("Employee Performance Report", "Mandar Joshi")
    r2.add_content("Attendance : 98%")
    r2.add_content("Projects Completed : 8")
    r2.add_content("Rating : Excellent")
    r2.add_content("Department : Computer Engineering")
    r2.add_content("Recommendation : Promotion Approved")
    r2.display_report()


def generate_report_3():
    r3 = Report("Student Result Report", "Mandar Joshi")
    r3.add_content("Student Name : Rahul")
    r3.add_content("Roll No : 101")
    r3.add_content("CGPA : 9.25")
    r3.add_content("Status : Pass with Distinction")
    r3.add_content("Result : Pass")
    r3.display_report()


# Main Loop for User Input
while True:
    print("\n" + "=" * 40)
    print("      REPORT GENERATOR MENU")
    print("=" * 40)
    print("1. Practical Report")
    print("2. Employee Performance Report")
    print("3. Student Result Report")
    print("4. Exit")

    choice = input("\nEnter your choice (1-4): ").strip()

    if choice == "1":
        generate_report_1()
    elif choice == "2":
        generate_report_2()
    elif choice == "3":
        generate_report_3()
    elif choice == "4":
        print("\nExiting Report Generator. Goodbye!")
        break
    else:
        print("\nInvalid choice! Please select a valid option (1-4).")