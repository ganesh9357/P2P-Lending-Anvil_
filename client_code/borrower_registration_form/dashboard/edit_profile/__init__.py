from ._anvil_designer import edit_profileTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import main_form_module as main_form_module

class edit_profile(edit_profileTemplate):
  def __init__(self, **properties):
    self.user_id=main_form_module.userId
    #self.user_id=1000  
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    user_profile=app_tables.fin_user_profile.get(customer_id=self.user_id)
    if user_profile: 
      self.borrower_full_name_text.text=user_profile['full_name']
      self.mail_text.text=user_profile['email_user']
      self.mobile_text.text=user_profile['mobile']
      self.date_label.text=user_profile['date_of_birth']
      self.city_text.text=user_profile['city']
      self.pan_text.text=user_profile['pan_number']
      self.image_1.source = user_profile['user_photo']

      photo_1 = self.file_loader_1.file
      if photo_1:
        self.image_1.source = photo_1
        
      
      
      
      options = app_tables.fin_gender.search()
      options_string = [str(option['gender']) for option in options]
      self.gender_down.items = options_string
      
      self.mother_label.text=user_profile['mouther_tounge']
      

      # if uploaded_image :
      #   user_profile['user_photo'] = uploaded_image
    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    user_profile=app_tables.fin_user_profile.get(customer_id=self.user_id)
    if user_profile: 
     user_profile['full_name']=self.borrower_full_name_text.text
     user_profile['email_user']=self.mail_text.text
     user_profile['mobile']=self.mobile_text.text
     user_profile['date_of_birth']=self.date_label.text
     user_profile['city']=self.city_text.text
     user_profile['pan_number']=self.pan_text.text
     user_profile['gender']=self.gender_down.selected_value
     user_profile['mouther_tounge']=self.mother_label.text
     photo = self.file_loader_1.file
     if photo:
      user_profile['user_photo'] = photo
     user_profile.update()
    alert('saved sucessfully')
    open_form('borrower_registration_form.dashboard')

  def home_borrower_registration_form_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('borrower_registration_form.dashboard')
