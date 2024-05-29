from ._anvil_designer import lender_view_profileTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import main_form_module as main_form_module


class lender_view_profile(lender_view_profileTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.user_id = main_form_module.userId
    self.disable_personal_fields()
    # self.disable_profession_fields()
    self.disable_business_details_fields()
    self.disable_bank_details_fields()
    self.load_user_profile()
    self.disable_company_employment_fields()
    self.disable_lender_details_fields()


    # Any code you write here will run before the form opens.

  def load_user_profile(self):
    user_profile = app_tables.fin_user_profile.get(customer_id=self.user_id)
    borrower_details = app_tables.fin_borrower.get(customer_id=self.user_id)

    if user_profile:
      self.name_label.text = user_profile["full_name"]
      self.email_id_label.text = user_profile["email_user"]
      self.name_text_box.text = user_profile["full_name"]
      self.email_tx.text = user_profile["email_user"]
      self.mobile_tx.text = user_profile["mobile"]
      self.d_o_b_text_box.text = user_profile["date_of_birth"]
      self.city_tx.text = user_profile["city"]
      self.g_i_1_tx.text = user_profile["aadhaar_no"]
      self.g_i_2_tx.text = user_profile["pan_number"]
      self.govt_id_1_image.source = user_profile["aadhaar_photo"]
      self.govt_id_2_image.source = user_profile["pan_photo"]
      self.gender_dropdown.selected_value = user_profile["gender"]
      self.Language_tx.text = user_profile["mouther_tounge"]
      self.image_1.source = user_profile["user_photo"]
      self.marrital_status_dropdown.selected_value = user_profile["marital_status"]
      self.state_tx.text = user_profile["state"]
      self.present_addres_dropdown.selected_value = user_profile["present_address"]
      self.address_1_tx.text = user_profile["street_adress_1"]
      self.address_2_tx.text = user_profile["street_address_2"]
      self.how_long_stay_tx.text = user_profile["duration_at_address"]
      self.pincode_tx.text = user_profile["pincode"]
      self.age_tx.text = user_profile["user_age"]
      self.vehicle_loan_tx.text = user_profile["vehicle_loan"]
      self.credit_tx.text = user_profile["credit_card_loans"]
      self.qualification_dropdown.selected_value = user_profile["qualification"]
      self.profession_dropdown.selected_value = user_profile["profession"]
      self.company_name_tx.text = user_profile["company_name"]
      self.occupation_dropdown.selected_value = user_profile["occupation_type"]
      self.employee_dropdown.selected_value = user_profile["employment_type"]
      self.organization_dropdown.selected_value = user_profile["organization_type"]
      self.company_address_tx.text = user_profile["company_address"]
      self.landmark_tx.text = user_profile["company_landmark"]
      self.company_no_tx.text = user_profile["business_no"]
      self.annual_salary_tx.text = user_profile["annual_salary"]
      self.salary_type_dropdown.selected_value = user_profile["salary_type"]
      self.designation_tx.text = user_profile["designation"]
      self.emp_id_proof.source = user_profile["emp_id_proof"]
      self.last_six_month_proof.source = user_profile["last_six_month_bank_proof"]
      # self.college_name_tx.text = user_profile["college_name"]
      # self.college_id_tx.text = user_profile["college_id"]
      # self.college_address_tx.text = user_profile["college_address"]
      # self.college_proof.source = user_profile["college_proof"]
      # self.type_of_land_dropdown.selected_value = user_profile["land_type"]
      # self.no_of_acers.text = user_profile["total_acres"]
      # self.crop_name.text = user_profile["crop_name"]
      # self.yearly_income.text = user_profile["farmer_earnings"]
      self.business_name_tex.text = user_profile["business_name"]
      self.business_address_tex.text = user_profile["business_add"]
      self.business_type_dropdown.selected_value = user_profile["business_type"]
      self.no_of_emp_dropdown.selected_value = user_profile["employees_working"]
      self.year_of_yest_tx.text = user_profile["year_estd"]
      self.industry_type_tx.text = user_profile["industry_type"]
      self.last_six_turnover_tx.text = user_profile["six_month_turnover"]
      self.last_six_month_for_business.source = user_profile[
        "last_six_month_bank_proof"
      ]
      self.din_tx.text = user_profile["din"]
      self.cin_tx.text = user_profile["cin"]
      self.office_address_tx.text = user_profile["registered_off_add"]
      self.proof_varification.source = user_profile["proof_verification"]
      self.holder_name_tx.text = user_profile["account_name"]
      self.account_no_tx.text = user_profile["account_number"]
      self.brach_name_tx.text = user_profile["account_bank_branch"]
      self.bank_id_tx.text = user_profile["bank_id"]
      self.bank_name_tx.text = user_profile["bank_name"]
      self.acccount_type_dropdown.selected_value = user_profile["account_type"]

      if user_profile['lending_type'] == 'Individual' :
        self.institutional_button.visible = False

      if user_profile['lending_type'] == 'Institutional' :
        self.individual_button.visible = False



      options = app_tables.fin_lendor_account_type.search()
      options_string =[str(option['lendor_account_type']) for option in options]
      self.acccount_type_dropdown.items = options_string

      options = app_tables.fin_lendor_marrital_status.search()
      options_string = [str(option['lendor_marrital_status']) for option in options]
      self.marrital_status_dropdown.items = options_string


      options = app_tables.fin_gender.search()
      self.gender_dropdown.items = [str(option["gender"]) for option in options]

      options = app_tables.fin_present_address.search()
      self.present_addres_dropdown.items = [
        str(option["present_address"]) for option in options
      ]

      options = app_tables.fin_borrower_profession.search()
      self.profession_dropdown.items = [
        str(option["borrower_profession"]) for option in options
      ]

      # options = app_tables.fin_borrower_qualification.search()
      # self.qualification_dropdown.items = [
      #   str(option["borrower_qualification"]) for option in options
      # ]
      options = app_tables.fin_lendor_qualification.search()
      options_string = [str(option['lendor_qualification']) for option in options]
      self.qualification_dropdown.items = options_string

      options = app_tables.fin_lendor_employee_type.search()
      options_string = [str(option['lendor_employee_type']) for option in options]
      self.employee_dropdown.items = options_string
  
      options = app_tables.fin_lendor_organization_type.search()
      options_string = [str(option['lendor_organization_type']) for option in options]
      self.organization_dropdown.items = options_string
  
      options = app_tables.fin_occupation_type.search()
      option_strings = [str(option['occupation_type']) for option in options]
      self.occupation_dropdown.items = option_strings

      # options = app_tables.fin_borrower_salary_type.search()
      # option_strings = [str(option["borrower_salary_type"]) for option in options]
      # self.salary_type_dropdown.items = option_strings

      options = app_tables.fin_lendor_salary_type.search()
      option_strings = [str(option['lendor_salary_type']) for option in options]
      self.salary_type_dropdown.items = option_strings

      options = app_tables.fin_lendor_business_type.search()
      options_string = [str(option['lendor_business_type']) for option in options]
      self.business_type_dropdown.items = options_string
  
      options = app_tables.fin_lendor_no_of_employees.search()
      options_string = [str(option['lendor_no_of_employees']) for option in options]
      self.no_of_emp_dropdown.items = options_string

      lender_details = app_tables.fin_lender.get(customer_id=self.user_id)
      if lender_details:
        self.investment_tx.text = lender_details["investment"]
        self.membership_tx.text = lender_details["membership"]
        self.lender_returns_tx.text = lender_details["return_on_investment"]
        self.lending_period_dropdown.selected_value = lender_details["lending_period"]

      options = app_tables.fin_lendor_lending_period.search()
      options_string =[str(option['lendor_lending_period']) for option in options]
      self.lending_period_dropdown.items = options_string

  def disable_personal_fields(self):
    self.name_text_box.enabled = False
    self.email_tx.enabled = False
    self.mobile_tx.enabled = False
    self.d_o_b_text_box.enabled = False
    self.city_tx.enabled = False
    self.g_i_1_tx.enabled = False
    self.g_i_2_tx.enabled = False
    self.gender_dropdown.enabled = False
    self.Language_tx.enabled = False
    self.marrital_status_dropdown.enabled = False
    self.state_tx.enabled = False
    self.present_addres_dropdown.enabled = False
    self.address_1_tx.enabled = False
    self.address_2_tx.enabled = False
    self.how_long_stay_tx.enabled = False
    self.pincode_tx.enabled = False
    self.age_tx.enabled = False
    self.vehicle_loan_tx.enabled = False
    self.credit_tx.enabled = False
    self.qualification_dropdown.enabled = False
    self.profession_dropdown.enabled = False

  def enable_personal_fields(self):
    self.name_text_box.enabled = True
    # self.email_tx.enabled = True
    self.mobile_tx.enabled = True
    # self.d_o_b_text_box.enabled = True
    self.city_tx.enabled = True
    # self.g_i_1_tx.enabled = True
    # self.g_i_2_tx.enabled = True
    self.gender_dropdown.enabled = True
    self.Language_tx.enabled = True
    self.marrital_status_dropdown.enabled = True
    self.state_tx.enabled = True
    self.present_addres_dropdown.enabled = True
    self.address_1_tx.enabled = True
    self.address_2_tx.enabled = True
    self.how_long_stay_tx.enabled = True
    self.pincode_tx.enabled = True
    self.age_tx.enabled = True
    self.vehicle_loan_tx.enabled = True
    self.credit_tx.enabled = True
    self.qualification_dropdown.enabled = True
    self.profession_dropdown.enabled = True

  def edit_personal_details_click(self, **event_args):
    self.enable_personal_fields()
    self.save_personal_details_button.visible = True
    self.edit_personal_details_button.visible = False
    self.govt_1_file_loader_1.visible = True
    self.govt_2_file_loader_2.visible = True

  def save_personal_details_click(self, **event_args):
    user_profile = app_tables.fin_user_profile.get(customer_id=self.user_id)
    if user_profile:
      user_profile["full_name"] = self.name_text_box.text
      # user_profile['email_user'] = self.email_tx.text
      user_profile["mobile"] = self.mobile_tx.text
      user_profile["date_of_birth"] = self.d_o_b_text_box.text
      user_profile["city"] = self.city_tx.text
      user_profile["aadhaar_no"] = self.g_i_1_tx.text
      user_profile["pan_number"] = self.g_i_2_tx.text
      user_profile["gender"] = self.gender_dropdown.selected_value
      user_profile["mouther_tounge"] = self.Language_tx.text
      user_profile["marital_status"] = self.marrital_status_dropdown.selected_value
      user_profile["state"] = self.state_tx.text
      user_profile["present_address"] = self.present_addres_dropdown.selected_value
      user_profile["street_adress_1"] = self.address_1_tx.text
      user_profile["street_address_2"] = self.address_2_tx.text
      user_profile["duration_at_address"] = self.how_long_stay_tx.text
      user_profile["pincode"] = self.pincode_tx.text
      user_profile["user_age"] = int(self.age_tx.text)
      user_profile["vehicle_loan"] = self.vehicle_loan_tx.text
      user_profile["credit_card_loans"] = self.credit_tx.text
      user_profile["qualification"] = self.qualification_dropdown.selected_value
      user_profile["profession"] = self.profession_dropdown.selected_value
      user_profile["other_loan"] = self.Language_tx.text
      self.govt_1_file_loader_1.visible = False
      self.govt_2_file_loader_2.visible = False
      self.name_label.text = self.name_text_box.text

      photo = self.govt_1_file_loader_1.file
      if photo:
        user_profile["aadhaar_photo"] = photo

      photo = self.govt_2_file_loader_2.file
      if photo:
        user_profile["pan_photo"] = photo
      # user_profile.update()

      # wallet = app_tables.fin_wallet.get(customer_id=self.user_id)
      # if wallet:
      #   wallet['user_email'] = self.email_tx.text
      #   wallet.update()

      # wallet = app_tables.fin_wallet.get(customer_id=self.user_id)
      # if wallet:
      #   wallet['user_email'] = self.email_tx.text
      #   wallet.update()

    self.disable_personal_fields()
    self.save_personal_details_button.visible = False
    self.edit_personal_details_button.visible = True

  def disable_company_employment_fields(self):
    # Disable company and employment fields
    self.company_name_tx.enabled = False
    self.occupation_dropdown.enabled = False
    self.employee_dropdown.enabled = False
    self.organization_dropdown.enabled = False
    self.company_address_tx.enabled = False
    self.landmark_tx.enabled = False
    self.company_no_tx.enabled = False
    self.annual_salary_tx.enabled = False
    self.salary_type_dropdown.enabled = False
    self.designation_tx.enabled = False
    self.emp_id_proof.enabled = False
    self.last_six_month_proof.enabled = False

  def enable_company_employment_fields(self):
    # Enable company and employment fields
    self.company_name_tx.enabled = True
    self.occupation_dropdown.enabled = True
    self.employee_dropdown.enabled = True
    self.organization_dropdown.enabled = True
    self.company_address_tx.enabled = True
    self.landmark_tx.enabled = True
    self.company_no_tx.enabled = True
    self.annual_salary_tx.enabled = True
    self.salary_type_dropdown.enabled = True
    self.designation_tx.enabled = True
    self.emp_id_proof.enabled = True
    self.last_six_month_proof.enabled = True

  def edit_company_employment_details_click(self, **event_args):
    self.enable_company_employment_fields()
    self.save_company_employment_details_button.visible = True
    self.edit_company_employment_details_button.visible = False
    self.employee_id_image.visible = True
    self.employee_last_six_bank_state_image.visible = True

  def save_company_employment_details_click(self, **event_args):
    user_profile = app_tables.fin_user_profile.get(customer_id=self.user_id)
    if user_profile:
      user_profile["company_name"] = self.company_name_tx.text
      user_profile["occupation_type"] = self.occupation_dropdown.selected_value
      user_profile["employment_type"] = self.employee_dropdown.selected_value
      user_profile["organization_type"] = self.organization_dropdown.selected_value
      user_profile["company_address"] = self.company_address_tx.text
      user_profile["company_landmark"] = self.landmark_tx.text
      user_profile["business_no"] = self.company_no_tx.text
      user_profile["annual_salary"] = self.annual_salary_tx.text
      user_profile["salary_type"] = self.salary_type_dropdown.selected_value
      user_profile["designation"] = self.designation_tx.text
      user_profile["emp_id_proof"] = self.emp_id_proof.source
      user_profile["last_six_month_bank_proof"] = self.last_six_month_proof.source

      photo = self.employee_id_image.file
      if photo:
        user_profile["emp_id_proof"] = photo

      photo = self.employee_last_six_bank_state_image.file
      if photo:
        user_profile["last_six_month_bank_proof"] = photo

    self.disable_company_employment_fields()
    self.save_company_employment_details_button.visible = False
    self.edit_company_employment_details_button.visible = True
    self.employee_id_image.visible = False
    self.employee_last_six_bank_state_image.visible = False



  def disable_business_details_fields(self):
    self.business_name_tex.enabled = False
    self.business_address_tex.enabled = False
    self.business_type_dropdown.enabled = False
    self.no_of_emp_dropdown.enabled = False
    self.year_of_yest_tx.enabled = False
    self.industry_type_tx.enabled = False
    self.last_six_turnover_tx.enabled = False
    self.last_six_month_for_business.enabled = False
    self.din_tx.enabled = False
    self.cin_tx.enabled = False
    self.office_address_tx.enabled = False
    self.proof_varification.enabled = False

  def enable_business_details_fields(self):
    self.business_name_tex.enabled = True
    self.business_address_tex.enabled = True
    self.business_type_dropdown.enabled = True
    self.no_of_emp_dropdown.enabled = True
    # self.year_of_yest_tx.enabled = True
    self.industry_type_tx.enabled = True
    self.last_six_turnover_tx.enabled = True
    self.last_six_month_for_business.enabled = True
    self.din_tx.enabled = True
    self.cin_tx.enabled = True
    self.office_address_tx.enabled = True
    self.proof_varification.enabled = True

  def edit_business_details_click(self, **event_args):
    self.enable_business_details_fields()
    self.save_business_details_button.visible = True
    self.edit_business_details_button.visible = False
    self.business_bank_st_image.visible = True
    self.business_proof_varificaions_image.visible = True

  def save_business_details_click(self, **event_args):
    user_profile = app_tables.fin_user_profile.get(customer_id=self.user_id)
    if user_profile:
      user_profile["business_name"] = self.business_name_tex.text
      user_profile["business_add"] = self.business_address_tex.text
      user_profile["business_type"] = self.business_type_dropdown.selected_value
      user_profile["employees_working"] = self.no_of_emp_dropdown.selected_value
      # user_profile['year_estd'] = self.year_of_yest_tx.text
      user_profile["industry_type"] = self.industry_type_tx.text
      user_profile["six_month_turnover"] = self.last_six_turnover_tx.text
      user_profile["last_six_month_bank_proof"] = (
        self.last_six_month_for_business.source
      )
      user_profile["din"] = self.din_tx.text
      user_profile["cin"] = self.cin_tx.text
      user_profile["registered_off_add"] = self.office_address_tx.text
      user_profile["proof_verification"] = self.proof_varification.source

      photo = self.business_bank_st_image.file
      if photo:
        user_profile["last_six_month_bank_proof"] = photo

      photo = self.business_proof_varificaions_image.file
      if photo:
        user_profile["proof_verification"] = photo

    self.disable_business_details_fields()
    self.save_business_details_button.visible = False
    self.edit_business_details_button.visible = True
    self.business_bank_st_image.visible = False
    self.business_proof_varificaions_image.visible = False

  def disable_bank_details_fields(self):
    self.holder_name_tx.enabled = False
    self.account_no_tx.enabled = False
    self.brach_name_tx.enabled = False
    self.bank_id_tx.enabled = False
    self.bank_name_tx.enabled = False
    self.acccount_type_dropdown.enabled = False

  def enable_bank_details_fields(self):
    self.holder_name_tx.enabled = True
    self.account_no_tx.enabled = True
    self.brach_name_tx.enabled = True
    self.bank_id_tx.enabled = True
    self.bank_name_tx.enabled = True
    self.acccount_type_dropdown.enabled = True

  def edit_bank_details_click(self, **event_args):
    self.enable_bank_details_fields()
    self.save_bank_details_button.visible = True
    self.edit_bank_details_button.visible = False

  def save_bank_details_click(self, **event_args):
    user_profile = app_tables.fin_user_profile.get(customer_id=self.user_id)
    if user_profile:
      user_profile["account_name"] = self.holder_name_tx.text
      user_profile["account_number"] = self.account_no_tx.text
      user_profile["account_bank_branch"] = self.brach_name_tx.text
      user_profile["bank_id"] = self.bank_id_tx.text
      user_profile["bank_name"] = self.bank_name_tx.text
      user_profile["account_type"] = self.acccount_type_dropdown.selected_value

    self.disable_bank_details_fields()
    self.save_bank_details_button.visible = False
    self.edit_bank_details_button.visible = True

  def disable_lender_details_fields(self):
    self.investment_tx.enabled = False
    self.membership_tx.enabled = False
    self.lender_returns_tx.enabled = False
    self.lending_period_dropdown.enabled = False

  def enable_lender_details_fields(self):
    self.investment_tx.enabled = True
    self.membership_tx.enabled = True
    # self.lender_returns_tx.enabled = True
    self.lending_period_dropdown.enabled = True

  def edit_lender_details_click(self, **event_args):
    self.enable_lender_details_fields()
    self.save_lender_details_button.visible = True
    self.edit_lender_details_button.visible = False

  def save_lender_details_click(self, **event_args):
    lender_details = app_tables.fin_lender.get(customer_id=self.user_id)
    if lender_details:
      lender_details["investment"] = float(self.investment_tx.text)
      lender_details["membership"] = self.membership_tx.text
      # lender_details["return_on_investment"] = self.lender_returns_tx.text
      lender_details["lending_period"] = self.lending_period_dropdown.selected_value

    self.disable_lender_details_fields()
    self.save_lender_details_button.visible = False
    self.edit_lender_details_button.visible = True

  
  def personal_information_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.personal_information_panel.visible = True
    self.profile_information_paenl.visible = False
    self.institutional_panel.visible = False
    self.Individual_panel.visible = False
    self.bank_details_panel.visible = False

  def Profile_Information_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass


  def Employee_Information_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.personal_information_panel.visible = False
    self.profile_information_paenl.visible = False
    self.institutional_panel.visible = False
    self.Individual_panel.visible = True
    self.bank_details_panel.visible = False


  def Business_Information_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.personal_information_panel.visible = False
    self.profile_information_paenl.visible = False
    self.institutional_panel.visible = True
    self.Individual_panel.visible = False
    self.bank_details_panel.visible = False

  def Bank_Details_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.personal_information_panel.visible = False
    self.profile_information_paenl.visible = False
    self.institutional_panel.visible = False
    self.Individual_panel.visible = False
    self.bank_details_panel.visible = True

  

  def govt_1_file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    if file:
      # Update Image_1 with the uploaded image
      self.govt_id_1_image.source = self.govt_1_file_loader_1.file

  def govt_2_file_loader_2_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    if file:
      # Update Image_1 with the uploaded image
      self.govt_id_2_image.source = self.govt_2_file_loader_2.file

  def business_bank_st_image_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    if file:
      # Update Image_1 with the uploaded image
      self.last_six_month_for_business.source = self.business_bank_st_image.file

  def business_proof_varificaions_image_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    if file:
      # Update Image_1 with the uploaded image
      self.proof_varification.source = self.business_proof_varificaions_image.file

  def employee_id_image_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    if file:
      # Update Image_1 with the uploaded image
      self.emp_id_proof.source = self.employee_id_image.file

  def employee_last_six_bank_state_image_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    if file:
      # Update Image_1 with the uploaded image
      self.last_six_month_proof.source = self.employee_last_six_bank_state_image.file


  def user_photo_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    if file:
      # Update Image_1 with the uploaded image
      self.image_1.source = self.user_photo.file
      user_profile = app_tables.fin_user_profile.get(customer_id=self.user_id)
      if user_profile:
        photo = self.user_photo.file
        if photo:
          user_profile["user_photo"] = photo
        user_profile.update()

  def Profile_Information_clickk(self, **event_args):
    """This method is called when the button is clicked"""
    self.personal_information_panel.visible = False
    self.profile_information_paenl.visible = True
    self.institutional_panel.visible = False
    self.Individual_panel.visible = False
    self.bank_details_panel.visible = False
