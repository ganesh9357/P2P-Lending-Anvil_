from ._anvil_designer import foreclose_detailsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime ,timedelta


class foreclose_details(foreclose_detailsTemplate):
    def __init__(self, selected_row, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.selected_row = selected_row
        self.name.text = f"{selected_row['borrower_name']}"
        self.loan.text = f"{selected_row['loan_amount']}"
        self.interest_rate.text = f"{selected_row['interest_rate']}"
        self.foreclose_fee.text = f"{selected_row['foreclose_fee']}"
        self.foreclose_amount.text = f"{selected_row['foreclose_amount']}"
        self.total.text = f"{selected_row['paid_amount']}"
        self.oa.text = f"{selected_row['outstanding_amount']}"
        self.reason.text = f"{selected_row['reason']}"
        self.due_amount.text = f"{selected_row['total_due_amount']}"

        loan_id = selected_row['loan_id']
        foreclosure_rows = app_tables.fin_foreclosure.search(loan_id=loan_id)

        if foreclosure_rows:
          for extend_row in foreclosure_rows :
            if extend_row['status'] not in ('approved', 'rejected'):
              approval_days_row = app_tables.fin_approval_days.get(loans='Foreclosure')
            
              if approval_days_row:
                  approval_days = approval_days_row['days_for_approval']
                  
                  # Calculate the time difference between now and the request date
                  print("Extension Request Date:", extend_row['requested_on'])
                  time_difference = datetime.now() - datetime.combine(extend_row['requested_on'], datetime.min.time())
                  print("Time Difference (seconds):", time_difference.total_seconds())
      
                  # Check if the time difference is more than the approval days
                  if time_difference.total_seconds() > (approval_days * 86400):  # 86400 seconds in a day
                      extend_row['status'] = 'approved'
                      extend_row['status_timestamp '] = datetime.now()
                      extend_row.update()
                      self.approve.visible = False
                      self.decline.visible = False
                      Notification("Your request has been accepted.").show()

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form("lendor.dashboard.view_loan_foreclosure_Requests")

    def approve_click(self, **event_args):
        """This method is called when the 'Approve' button is clicked"""      
        self.selected_row['status'] = 'approved'
        # Save changes to the table
        self.selected_row.update()
        Notification("Borrower will get notified").show()

        # Update status in the fin_foreclosure table
        self.update_foreclosure_status('approved')

        loan = app_tables.fin_loan_details.get(loan_id=self.selected_row['loan_id'])
        loan['loan_updated_status'] = "foreclosure"
        open_form("lendor.dashboard.view_loan_foreclosure_Requests")

    def decline_click(self, **event_args):
        """This method is called when the 'Decline' button is clicked"""
        self.selected_row['status'] = 'rejected'
        self.selected_row.update()
        self.update_foreclosure_status('rejected')
        Notification("Borrower will get notified").show()
        open_form("lendor.dashboard.view_loan_foreclosure_Requests")
      
    def update_foreclosure_status(self, new_status):
        """Update the status in the fin_foreclosure table"""
        foreclosure_row = app_tables.fin_foreclosure.get(loan_id=self.selected_row['loan_id'])
        if foreclosure_row is not None:
            foreclosure_row['status'] = new_status
            foreclosure_row['status_timestamp '] = datetime.now()
            foreclosure_row.update()
