from ._anvil_designer import manage_loan_detailsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class manage_loan_details(manage_loan_detailsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def loan_settings(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.manage_loan_details.loan_settings')

  def view_loans(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.manage_loan_details.loan_management')

  def button_1_copy_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard')
