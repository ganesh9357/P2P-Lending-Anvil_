from ._anvil_designer import editing_detabase_detailsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class editing_detabase_details(editing_detabase_detailsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.set_data_grid_properties()
    self.repeating_panel_1.items = app_tables.fin_loan_details.search()
    self.repeating_panel_2.items = app_tables.fin_emi_table.search()
    self.repeating_panel_3.items = app_tables.fin_extends_loan.search()
    self.repeating_panel_4.items = app_tables.fin_foreclosure.search()

    # self.set_data_grid_properties()

  def set_data_grid_properties(self):
    for data_grid in [self.data_grid_1, self.data_grid_2, self.data_grid_3, self.data_grid_4]:
      data_grid.role = 'my-scrollable-container'
      for col in data_grid.columns:
        col['width'] = '500px'

  
  def button_1_copy_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.loan_management')

  def loan_details_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.data_grid_1.visible = True
    self.data_grid_2.visible = False
    self.data_grid_3.visible = False
    self.data_grid_4.visible = False

    self.loan_details_label.visible = True
    self.emi_details_label.visible = False
    self.extension_details_label.visible = False
    self.foreclosure_details_label.visible = False

  def emi_details_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.data_grid_1.visible = False
    self.data_grid_2.visible = True
    self.data_grid_3.visible = False
    self.data_grid_4.visible = False

    self.loan_details_label.visible = False
    self.emi_details_label.visible = True
    self.extension_details_label.visible = False
    self.foreclosure_details_label.visible = False
    
  def extension_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.data_grid_1.visible = False
    self.data_grid_2.visible = False
    self.data_grid_3.visible = True
    self.data_grid_4.visible = False

    self.loan_details_label.visible = False
    self.emi_details_label.visible = False
    self.extension_details_label.visible = True
    self.foreclosure_details_label.visible = False

  def foreclosure_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.data_grid_1.visible = False
    self.data_grid_2.visible = False
    self.data_grid_3.visible = False
    self.data_grid_4.visible = True

    self.loan_details_label.visible = False
    self.emi_details_label.visible = False
    self.extension_details_label.visible = False
    self.foreclosure_details_label.visible = True