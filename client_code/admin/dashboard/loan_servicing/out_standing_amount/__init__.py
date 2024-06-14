from ._anvil_designer import out_standing_amountTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class out_standing_amount(out_standing_amountTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.load_loan_and_emi_details()

  def load_loan_and_emi_details(self):
        # Fetch loan details from the fin_loan_details table
        loans = app_tables.fin_loan_details.search()

        loan_emi_details = []
        for loan in loans:
            loan_id = loan['loan_id']
            loan_details = {
                'loan_id': loan_id,
                'loan_amount': loan['loan_amount'],
                'product_name': loan['product_name'],
                'borrower_full_name': loan['borrower_full_name'],
                'total_repayment_amount': loan['total_repayment_amount'],
                'remaining_amount': loan['remaining_amount'],
                'borrower_customer_id': loan['borrower_customer_id'],
                'tenure': loan['tenure'],
            }

            # Fetch the EMI entries for this loan
            emi_entries = list(app_tables.fin_emi_table.search(q.all_of(loan_id=loan_id)))
            if emi_entries:
                emi_entries.sort(key=lambda x: x['emi_number'], reverse=True)
                last_emi = emi_entries[0]
                loan_details.update({
                    'emi_number': last_emi['emi_number'],
                    'remaining_tenure': last_emi['remaining_tenure'],
                    # 'emi_date': last_emi['emi_date']
                })
            else:
                loan_details.update({
                    'emi_number': 'N/A',
                    'remaining_tenure': 'N/A',
                    # 'emi_date': 'N/A'
                })

            loan_emi_details.append(loan_details)

        # Assuming you have a repeating panel in your form named `repeating_panel`
        self.repeating_panel_1.items = loan_emi_details

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.Tracking')



  