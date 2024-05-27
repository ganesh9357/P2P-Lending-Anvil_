
from ._anvil_designer import FTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import main_form_module as main_form_module


class F(FTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.user_id=main_form_module.userId

    # Any code you write here will run before the form opens.
    user_profile=app_tables.fin_user_profile.get(customer_id=self.user_id)
    if user_profile: 
      self.name_label.text=user_profile['full_name']
      self.email_id_label.text=user_profile['email_user']
      self.name_text_box.text=user_profile['full_name']
      self.email_tx.text=user_profile['email_user']
      self.mobile_tx.text=user_profile['mobile']
      self.d_o_b_text_box.text=user_profile['date_of_birth']
      self.city_tx.text=user_profile['city']
      self.g_i_1_tx.text=user_profile['aadhaar_no']
      self.g_i_2_tx.text=user_profile['pan_number']
      self.gender_dropdown.selected_value=user_profile['gender']
      self.Language_tx.text=user_profile['mouther_tounge']
      self.image_1.source = user_profile['user_photo']
      self.marrital_tx.text=user_profile['marital_status']
      self.state_tx.text=user_profile['state']
      self.present_addres_dropdown.selected_value=user_profile['present_address']
      self.address_1_tx.text=user_profile['street_adress_1']
      self.address_2_tx.text=user_profile['street_address_2']
      self.how_long_stay_tx.text=user_profile['duration_at_address']
      self.pincode_tx.text=user_profile['pincode']
      # self.gender_tx.text=user_profile['home_loan']
      self.Language_tx.text=user_profile['other_loan']
      self.age_tx.text = user_profile['user_age']
      self.vehicle_loan_tx.text=user_profile['vehicle_loan']
      self.credit_tx.text=user_profile['credit_card_loans']
      self.qualification_dropdown.selected_value=user_profile['qualification']
      self.profession_dropdown.selected_value=user_profile['profession']

      options = app_tables.fin_gender.search()
      option_strings = [str(option['gender']) for option in options]
      self.gender_dropdown.items = option_strings

      options = app_tables.fin_present_address.search()
      option_strings = [str(option['present_address']) for option in options]
      self.present_addres_dropdown.items = option_strings

      options = app_tables.fin_borrower_profession.search()
      option_strings = [str(option['borrower_profession']) for option in options]
      self.profession_dropdown.items = option_strings

      options = app_tables.fin_borrower_qualification.search()
      options_string = [str(option['borrower_qualification']) for option in options]
      self.qualification_dropdown.items = options_string






      
# # profile details
#       self.profession_dropdown.selected_value=user_profile['cre']
#       self.profession_dropdown.selected_value=user_profile['qualification']
# profession details
      self.college_name_tx.text=user_profile['college_name']
      self.college_id_tx.text =user_profile['college_id']
      self.college_address_tx.text=user_profile['college_address']
      self.college_proof.source=user_profile['college_proof']

#bank details
     # profession details
      self.college_name_tx.text=user_profile['college_name']
      self.college_id_tx.text =user_profile['college_id']
      self.college_address_tx.text=user_profile['college_address']
      self.college_proof.source=user_profile['college_proof']

#employee details
      self.company_name_tx.text=user_profile['company_name']
      self.occupation_dropdown.selected_value=user_profile['occupation_type']
      self.employee_dropdown.selected_value=user_profile['employment_type']
      self.organization_dropdown.selected_value=user_profile['organization_type']
      self.company_address_tx.text=user_profile['company_address']
      self.landmark_tx.text=user_profile['company_landmark']
      self.company_no_tx.text=user_profile['business_no']
      self.annual_salary_tx.text=user_profile['annual_salary']
      self.salary_type_dropdown.selected_value=user_profile['salary_type']
      self.designation_tx.text = user_profile['designation']
      self.emp_id_proof.source=user_profile['emp_id_proof']
      self.last_six_month_proof.source=user_profile['last_six_month_bank_proof']

      options_1 = app_tables.fin_borrower_employee_type.search()
      option_strings_1 = [str(option['borrower_employee_type']) for option in options_1]
      self.employee_dropdown.items = option_strings_1
  
          # Populate drop_down_2 with data from 'organization_type' column
      options_2 = app_tables.fin_borrower_organization_type.search()
      option_strings_2 = [str(option['borrower_organization_type']) for option in options_2]
      self.organization_dropdown.items = option_strings_2
  
      options = app_tables.fin_occupation_type.search()
      option_strings = [str(option['occupation_type']) for option in options]
      self.occupation_dropdown.items = option_strings

      options = app_tables.fin_borrower_salary_type.search()
      option_strings = [str(option['borrower_salary_type']) for option in options]
      self.salary_type_dropdown.items = option_strings

# former dtails
      self.type_of_land_dropdown.selected_value=user_profile['land_type']
      self.no_of_acers.text=user_profile['total_acres']
      self.crop_name.text=user_profile['crop_name']
      self.yearly_income.text=user_profile['farmer_earnings']

      options_2 = app_tables.fin_borrower_land_type.search()
      option_strings_2 = [str(option['land_type']) for option in options_2]
      self.type_of_land_dropdown.items = option_strings_2

# business details
      self.business_name_tex.text=user_profile['business_name']
      self.business_address_tex.text=user_profile['business_add']
      self.business_type_dropdown.selected_value=user_profile['business_type']
      self.no_of_emp_dropdown.selected_value=user_profile['employees_working']
      self.year_of_yest_tx.text=user_profile['year_estd']
      self.industry_type_dropdown.selected_value=user_profile['industry_type']
      self.last_six_turnover_tx.text=user_profile['six_month_turnover']
      self.last_six_month_for_business.source=user_profile['last_six_month_bank_proof']
      self.din_tx.text=user_profile['din']
      self.cin_tx.text = user_profile['cin']
      self.office_address_tx.text=user_profile['registered_off_add']
      self.proof_varification.source=user_profile['proof_verification']

      options_1 = app_tables.fin_borrower_business_type.search()
      option_strings_1 = [str(option['borrower_business_type']) for option in options_1]
      self.business_type_dropdown.items = option_strings_1

      options_2 = app_tables.fin_borrower_no_of_employees.search()
      option_strings_2 = [str(option['borrower_no_of_employees']) for option in options_2]
      self.no_of_emp_dropdown.items = option_strings_2

      user_profile.update()





      

  # profile information
      borrower_details = app_tables.fin_borrower.get(customer_id=self.user_id)
      if borrower_details:
        self.credit_limit_tx.text = borrower_details['credit_limit']
        self.member_since_tx.text = borrower_details['borrower_since']

  def personal_information_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.personal_information_panel.visible = True
    self.employee_information_panel.visible = False
    self.business_information_panel.visible = False
    self.professional_information_paenl.visible = False
    self.profile_information_paenl.visible = False
    self.farmer_information_panel.visible = False
    self.bank_details_panel.visible = False

  def Profile_Information_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.personal_information_panel.visible = False
    self.employee_information_panel.visible = False
    self.business_information_panel.visible = False
    self.professional_information_paenl.visible = False
    self.profile_information_paenl.visible = True
    self.farmer_information_panel.visible = False
    self.bank_details_panel.visible = False

  def Student_information_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.personal_information_panel.visible = False
    self.employee_information_panel.visible = False
    self.business_information_panel.visible = False
    self.professional_information_paenl.visible = True
    self.profile_information_paenl.visible = False
    self.farmer_information_panel.visible = False
    self.bank_details_panel.visible = False

  def Employee_Information_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.personal_information_panel.visible = False
    self.employee_information_panel.visible = False
    self.business_information_panel.visible = False
    self.professional_information_paenl.visible = False
    self.employee_information_panel.visible = True
    self.farmer_information_panel.visible = False
    self.bank_details_panel.visible = False

  def farmer_infromation_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.personal_information_panel.visible = False
    self.professional_information_paenl.visible = False
    self.business_information_panel.visible = False
    self.profile_information_paenl.visible = False
    self.employee_information_panel.visible = False
    self.farmer_information_panel.visible = True
    self.bank_details_panel.visible = False

  def Business_Information_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.personal_information_panel.visible = False
    self.professional_information_paenl.visible = False
    self.business_information_panel.visible = True
    self.profile_information_paenl.visible = False
    self.employee_information_panel.visible = False
    self.farmer_information_panel.visible = False
    self.bank_details_panel.visible = False

  def Bank_Details_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.personal_information_panel.visible = False
    self.professional_information_paenl.visible = False
    self.business_information_panel.visible = False
    self.profile_information_paenl.visible = False
    self.employee_information_panel.visible = False
    self.farmer_information_panel.visible = False
    self.bank_details_panel.visible = True

  def Edit_personal_detials_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def Edit_business_details_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

