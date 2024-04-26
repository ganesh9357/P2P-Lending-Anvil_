from ._anvil_designer import signup_pageTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...user_form import user_module
from .. import main_form_module
import re


class signup_page(signup_pageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    email = self.text_box_1.text.strip()
        # Get the password
    password = self.text_box_2.text.strip()
    retype_password = self.text_box_3.text.strip()

    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            self.retype_password_error_label.text = ' Please enter a valid email address.'
            self.retype_password_error_label.visible = True
            return
      
    if password != retype_password:
            self.retype_password_error_label.text = 'Passwords do not match. Please re-enter.'
            self.retype_password_error_label.visible = True
            return

    # hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    if email:
      print(email)
      check_user_already_exist = user_module.check_user_profile(email)
      if check_user_already_exist is None:
                print("main if statement was executed")
                user_module.add_email_and_user_id(email ,password)
                main_form_module.email = email
                main_form_module.flag = True
                open_form('bank_users.main_form.basic_registration_form')
      else:
        self.retype_password_error_label.text = 'Email is already exists'
        self.retype_password_error_label.visible = True

  def check_box_1_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    self.password_visible = self.check_box_1.checked
    if self.password_visible:
         self.text_box_3.hide_text = False  # Show decrypted password
    else:
        self.text_box_3.hide_text = True

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('bank_users.main_form.login_page')
