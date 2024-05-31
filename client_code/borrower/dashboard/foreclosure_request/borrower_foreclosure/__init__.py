from ._anvil_designer import borrower_foreclosureTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime ,timedelta
import sys as sys

class borrower_foreclosure(borrower_foreclosureTemplate):
    def __init__(self, selected_row, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        # self.label_loan_id.text = f"{selected_row['loan_id']}"
        self.label_name.text = f"{selected_row['borrower_full_name']}"
        self.label_loan_amount.text = f"{selected_row['loan_amount']}"
        self.label_loan_tenure.text = f"{selected_row['tenure']} Months"
        self.label_interest_rate.text = f"{selected_row['interest_rate']} % pa"
        self.label_credit_limit.text = f"{selected_row['credit_limit']}"
        self.label_3.text = "Foreclosure Request Under Process......"  
        self.label_5.text = "Foreclosure Request Rejected"
        self.label_8.text = "Foreclosure is not available for this product.."
        product_id_to_search = selected_row['product_id']
        data = tables.app_tables.fin_product_details.search(product_id=product_id_to_search)
        self.foreclosure_type_lst = []    
        for i in data:
            self.foreclosure_type_lst.append(i['foreclose_type'])
        
        self.foreclose_type.text = self.foreclosure_type_lst[0]
        print(self.foreclose_type.text)

        # Check status for the selected loan ID
        loan_id = selected_row['loan_id']
        foreclosure_rows = app_tables.fin_foreclosure.search(loan_id=loan_id)

        if foreclosure_rows:
          for extend_row in foreclosure_rows :
            if extend_row['status'] not in ('approved', 'rejected'):
              approval_days_row = app_tables.fin_approval_days.get(loans='Extension')
            
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

      
        foreclosure_rows = app_tables.fin_foreclosure.search(loan_id=loan_id)

        approved_status = False
        rejected_status = False

        for row in foreclosure_rows:
            if row['status'] == 'approved':
                approved_status = True
                break
            elif row['status'] == 'rejected':
                rejected_status = True
                break

        if approved_status:
            # If there is an approved status, make "Pay" button visible
            self.button_foreclose.visible = False
            self.button_2.visible = False
            self.button_3.visible = True
            self.button_4.visible = True
            Notification("Your request has been accepted.").show()
        elif rejected_status:
            # If there is a reject status, show an alert
            Notification('Your request has been rejected.').show()
            self.button_foreclose.visible = False
            self.button_2.visible = False
            self.button_3.visible = False
            self.label_5.visible = True
            self.button_5.visible = False
            self.foreclose_again.visible = True
            self.foreclose_back.visible = True
        else:
            # If there is no approved or reject status, check if the loan ID is in foreclosure table
            existing_requests = app_tables.fin_foreclosure.search(loan_id=loan_id)
            if len(existing_requests) == 0 and self.foreclose_type.text != "Not Eligible":
                # If the loan ID is not in the foreclosure table, make "Foreclose" button and button2 visible
                self.button_foreclose.visible = True
                self.button_2.visible = True
                self.button_3.visible = False
                self.button_4.visible = False
            elif self.foreclose_type.text == "Not Eligible":
                # If the loan ID is in the foreclosure table, make other buttons visible
                self.button_foreclose.visible = False
                self.button_2.visible = False 
                self.button_4.visible = False
                self.button_3.visible = False
                self.label_8.visible = True
                self.button_5.visible = True
            else:
                self.button_foreclose.visible = False
                self.button_2.visible = False 
                self.button_4.visible = False
                self.button_3.visible = False
                self.label_3.visible = True
                self.button_5.visible = True

        # Save selected_row as an instance variable for later use
        self.selected_row = selected_row
  
        product_id = selected_row['product_id']
        product_details_row = app_tables.fin_product_details.get(product_id=product_id)
        self.min_months = product_details_row['min_months']
        self.min_months = int(self.min_months)

        loan_id = selected_row['loan_id']
        # Fetching the last row data for the specified loan_id from the fin_emi_table
        last_emi_rows = app_tables.fin_emi_table.search(loan_id=loan_id)
        try:
            if last_emi_rows:
                # Convert LiveObjectProxy to list
                last_emi_list = list(last_emi_rows)
                
                if last_emi_list:
                    # Sort the list of rows based on the 'emi_number' column in reverse order
                    last_emi_list.sort(key=lambda x: x['emi_number'], reverse=True)
                    
                    # Extract the 'emi_number' from the first row, which represents the highest 'emi_number'
                    total_payments_made = last_emi_list[0]['emi_number']
                    
                    print("Total payment made:", total_payments_made)
                    # Set the label text
                    self.label_tpm.text = f"{total_payments_made} months"
                    self.total_payments_made = total_payments_made

                    next_payment_date = last_emi_list[0]['next_payment']
                    if next_payment_date:
                        if (next_payment_date - timedelta(days=2)) > datetime.now().date():
                            self.is_payment_date_valid = True
                        else:
                            self.is_payment_date_valid = False
                            alert("The next payment date must be at least two days before today's date for foreclosure.")
                    else:
                        self.is_payment_date_valid = False
                        alert("Next payment date not found.")
                else:
                    total_payments_made = 0
                    alert("No EMIs found for this loan.")                    
            else:
                total_payments_made = 0
                alert("No EMIs found for this loan.")                
        except ValueError as e:
            alert(str(e))
        
    def button_foreclose_click(self, **event_args):
        selected_row = self.selected_row
        # loan_id = selected_row['loan_id']
        # total_payments_made = self.loan_details_row['total_payments_made']
        if self.total_payments_made >= self.min_months and self.is_payment_date_valid:
            open_form('borrower.dashboard.foreclosure_request.borrower_foreclosure.foreclose', selected_row=selected_row, total_payments_made=self.total_payments_made)
        else:
            if not self.is_payment_date_valid:
                alert('The next payment date must be at least two days before today\'s date for foreclosure.')
            else:
                alert('You are not eligible for foreclosure! You have to pay at least ' + str(self.min_months) + ' months.')
            open_form('borrower.dashboard.foreclosure_request')

  
    def button_2_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('borrower.dashboard.foreclosure_request')

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('borrower.dashboard')

    def button_4_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('borrower.dashboard.foreclosure_request')

    def button_5_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('borrower.dashboard.foreclosure_request')

    def foreclose_again_click(self, **event_args):
        """This method is called when the button is clicked"""
        loan_id = self.selected_row['loan_id']
    
        # Search for the corresponding row in the fin_foreclosure table
        foreclosure_row = app_tables.fin_foreclosure.get(loan_id=loan_id)
        
        # Update the status to "Under Process"
        foreclosure_row['status'] = 'under process'
        
        # Update the requested_on column with today's date and time
        foreclosure_row['requested_on'] = datetime.now()
        
        # Save the changes
        foreclosure_row.update()
        alert("Your Foreclosure request is submitted.")
        open_form('borrower.dashboard')
  
        # selected_row = self.selected_row
        # # loan_id = selected_row['loan_id']
        # # total_payments_made = self.loan_details_row['total_payments_made']
        # if self.total_payments_made >= self.min_months:
        #     open_form('borrower.dashboard.foreclosure_request.borrower_foreclosure.foreclose',  selected_row=selected_row, total_payments_made=self.total_payments_made)
        # else:
        #     alert('You are not eligible for foreclosure! You have to pay at least ' + str(self.min_months) + ' months.')
        #     open_form('borrower.dashboard.foreclosure_request')

    def again_back_click(self, **event_args):
      """This method is called when the button is clicked"""
      open_form('borrower.dashboard.foreclosure_request')



