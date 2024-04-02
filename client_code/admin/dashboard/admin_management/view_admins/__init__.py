from ._anvil_designer import view_adminsTemplate
from anvil import *
import anvil.server

class view_admins(view_adminsTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.populate_admins()

    def populate_admins(self):
        
        self.data = tables.app_tables.fin_admin_users.search()

        if not self.data:
            Notification("No Data Available Here!").show()
        else:
            self.result = [{'admin_email': i['admin_email'],
                            'full_name': i['full_name'],
                            'admin_role': i['admin_role'],
                            'ref_admin_name': i['ref_admin_name'],
                            'join_date': i['join_date'],
                            'admin_id': i['admin_id'],
                            'join_date': i['join_date'],
                           }
                           for i in self.data]

            self.repeating_panel.items = self.result

    def button_1_click(self, **event_args):
      """This method is called when the button is clicked"""
      open_form('admin.dashboard.admin_management')











