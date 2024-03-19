# from ._anvil_designer import dashboard_report_a_problemTemplate
# from anvil import *
# import anvil.server
# import anvil.google.auth, anvil.google.drive
# from anvil.google.drive import app_files
# import anvil.users
# import anvil.tables as tables
# import anvil.tables.query as q
# from anvil.tables import app_tables
# import datetime

# class dashboard_report_a_problem(dashboard_report_a_problemTemplate):
#   def __init__(self, **properties):
#     # Set Form properties and Data Bindings.
#     self.init_components(**properties)

#     # Any code you write here will run before the form opens.
#   def button_2_click(self, **event_args):
#         name = self.name_box.text
#         email = self.email_box.text
#         mobile = self.mobile_box.text
#         mobile = int (mobile)
#         issue = self.issue_box.text
#         description = self.description_box.text
#         current_datetime = datetime.datetime.now()

#         app_tables.fin_reported_problems.add_row(name=name, email=email, mobile_number=mobile, issue_occured=issue, issue_description=description, report_date=current_datetime)

#         # Show success message to the user
#         alert('Problem reported successfully. Thank you for your feedback!')

#         # Open dashboard form or any other form
#         open_form('borrower_registration_form.dashboard')
from ._anvil_designer import dashboard_report_a_problemTemplate
from anvil import *
import datetime
from anvil.tables import app_tables
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files



class dashboard_report_a_problem(dashboard_report_a_problemTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

    def button_2_click(self, **event_args):
        # Get input values from text boxes
        name = self.name_box.text
        email = self.email_box.text
        mobile = self.mobile_box.text
        issue = self.issue_box.text
        description = self.description_box.text

        # Validate if all required fields are filled
        if not name or not email or not mobile or not issue or not description:
            alert("Please fill in all required fields.")
            return

        # Validate mobile number
        try:
            mobile = int(mobile)
        except ValueError:
            alert("Mobile number must be a valid number.")
            return

        # Check if a file is uploaded
        if not self.file_loader_1.file:
            alert("Please upload a file.")
            return

        current_datetime = datetime.datetime.now()

        # Get the file uploaded via file_loader_1
        file = self.file_loader_1.file

        # Add a row to the fin_reported_problems table with file details
        app_tables.fin_reported_problems.add_row(name=name,
                                                  email=email,
                                                  mobile_number=mobile,
                                                  issue_occured=issue,
                                                  issue_description=description,
                                                  report_date=current_datetime,
                                                  user_photo=file)

        # Show success message to the user
        alert('Problem reported successfully. Thank you for your feedback!')

        # Open dashboard form or any other form
        open_form('borrower_registration_form.dashboard')
