from ._anvil_designer import ItemTemplate25Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
# from ......borrower.dashboard import main_form_module


class ItemTemplate25(ItemTemplate25Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # self.user_id = main_form_module.userId
        
    # user_data = app_tables.fin_loan_details.search()
        
    # # Iterate over each row in user_data
    # for row in user_data:
    #     borrower_customer_id = row['borrower_customer_id']
    #     lender_customer_id = row['lender_customer_id']
            
    #       # Retrieve borrower and lender profiles
    #     borrower_profile = app_tables.fin_user_profile.get(customer_id=borrower_customer_id)
    #     lender_profile = app_tables.fin_user_profile.get(customer_id=lender_customer_id)
    #     self.image_1.source = borrower_profile['user_photo']
    #     self.image_1_copy.source = lender_profile['user_photo']

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    value_to_pass = self.loan_id.text
    open_form('admin.dashboard.manage_loan_details.loan_management.not_payable_amount.view_profile_9', value_to_pass)

 

