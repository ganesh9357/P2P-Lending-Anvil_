from ._anvil_designer import view_loansTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import main_form_module as main_form_module

class view_loans(view_loansTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.user_id = main_form_module.userId
        print(self.user_id, ' idddd')

        # Fetch data based on loan status and user ID
        open_loans = app_tables.fin_loan_details.search(
            loan_updated_status=q.like('approved%'), 
            borrower_customer_id=self.user_id
        )

        borrower_profiles = []
        for loan in open_loans:
            user_profile = app_tables.fin_user_profile.get(customer_id=loan['lender_customer_id'])
            if user_profile is not None:
                borrower_profiles.append({
                    'mobile': user_profile['mobile'],
                    'interest_rate': loan['interest_rate'],
                    'loan_amount': loan['loan_amount'],
                    'tenure': loan['tenure'],
                    'loan_disbursed_timestamp': loan['loan_disbursed_timestamp'],
                    'product_name': loan['product_name'],
                    'product_description': loan['product_description'],
                    'lender_full_name': loan['lender_full_name'],
                    'product_id': loan['product_id'],
                    'loan_id': loan['loan_id'],
                    'borrower_loan_created_timestamp': loan['borrower_loan_created_timestamp'],
                    'loan_updated_status' : loan['loan_updated_status']
                })

        self.repeating_panel_6.items = borrower_profiles

        # Fetch data based on loan status and user ID
        closed_loans = app_tables.fin_loan_details.search(
            loan_updated_status=q.like('close%'), 
            borrower_customer_id=self.user_id
        )

        borrower_profiles1 = []
        for loan in closed_loans:
            user_profile = app_tables.fin_user_profile.get(customer_id=loan['lender_customer_id'])
            if user_profile is not None:
                borrower_profiles1.append({
                    'mobile': user_profile['mobile'],
                    'interest_rate': loan['interest_rate'],
                    'loan_amount': loan['loan_amount'],
                    'tenure': loan['tenure'],
                    'loan_disbursed_timestamp': loan['loan_disbursed_timestamp'],
                    'product_name': loan['product_name'],
                    'product_description': loan['product_description'],
                    'lender_full_name': loan['lender_full_name'],
                    'product_id': loan['product_id'],
                    'loan_id': loan['loan_id'],
                    'borrower_loan_created_timestamp': loan['borrower_loan_created_timestamp'],
                    'loan_updated_status' : loan['loan_updated_status']
                })

        self.repeating_panel_7.items = borrower_profiles1


        # Fetch data based on loan status and user ID
        under_process = app_tables.fin_loan_details.search(
            loan_updated_status=q.like('under process%'), 
            borrower_customer_id=self.user_id
        )

        borrower_profiles2 = []
        for loan in under_process:
            user_profile = app_tables.fin_user_profile.get(customer_id=loan['lender_customer_id'])
            if user_profile is not None:
                borrower_profiles2.append({
                    'mobile': user_profile['mobile'],
                    'interest_rate': loan['interest_rate'],
                    'loan_amount': loan['loan_amount'],
                    'tenure': loan['tenure'],
                    'loan_disbursed_timestamp': loan['loan_disbursed_timestamp'],
                    'product_name': loan['product_name'],
                    'product_description': loan['product_description'],
                    'lender_full_name': loan['lender_full_name'],
                    'product_id': loan['product_id'],
                    'loan_id': loan['loan_id'],
                    'borrower_loan_created_timestamp': loan['borrower_loan_created_timestamp'],
                    'loan_updated_status' : loan['loan_updated_status']
                })

        self.repeating_panel_9.items = borrower_profiles2

        rejected_loans = app_tables.fin_loan_details.search(
            loan_updated_status=q.like('rejected%'), 
            borrower_customer_id=self.user_id
        )

        borrower_profiles3 = []
        for loan in rejected_loans:
            user_profile = app_tables.fin_user_profile.get(customer_id=loan['lender_customer_id'])
            if user_profile is not None:
                borrower_profiles3.append({
                    'mobile': user_profile['mobile'],
                    'interest_rate': loan['interest_rate'],
                    'loan_amount': loan['loan_amount'],
                    'tenure': loan['tenure'],
                    'loan_disbursed_timestamp': loan['loan_disbursed_timestamp'],
                    'product_name': loan['product_name'],
                    'product_description': loan['product_description'],
                    'lender_full_name': loan['lender_full_name'],
                    'product_id': loan['product_id'],
                    'loan_id': loan['loan_id'],
                    'borrower_loan_created_timestamp': loan['borrower_loan_created_timestamp'],
                    'loan_updated_status' : loan['loan_updated_status']
                })

        self.repeating_panel_8.items = borrower_profiles3

        foreclose = app_tables.fin_loan_details.search(
            loan_updated_status=q.like('foreclose%'), 
            borrower_customer_id=self.user_id
        )

        borrower_profiles4 = []
        for loan in foreclose:
            user_profile = app_tables.fin_user_profile.get(customer_id=loan['lender_customer_id'])
            if user_profile is not None:
                borrower_profiles4.append({
                    'mobile': user_profile['mobile'],
                    'interest_rate': loan['interest_rate'],
                    'loan_amount': loan['loan_amount'],
                    'tenure': loan['tenure'],
                    'loan_disbursed_timestamp': loan['loan_disbursed_timestamp'],
                    'product_name': loan['product_name'],
                    'product_description': loan['product_description'],
                    'lender_full_name': loan['lender_full_name'],
                    'product_id': loan['product_id'],
                    'loan_id': loan['loan_id'],
                    'borrower_loan_created_timestamp': loan['borrower_loan_created_timestamp'],
                    'loan_updated_status' : loan['loan_updated_status']
                })

        self.repeating_panel_10.items = borrower_profiles4

        

        # self.repeating_panel_7.items = app_tables.fin_loan_details.search(loan_updated_status=q.like('close%'), borrower_customer_id=self.user_id)
        # self.repeating_panel_8.items = app_tables.fin_loan_details.search(loan_updated_status=q.like('reject%'), borrower_customer_id=self.user_id)
        # self.repeating_panel_9.items = app_tables.fin_loan_details.search(loan_updated_status=q.like('under process%'), borrower_customer_id=self.user_id)
        # self.repeating_panel_10.items = app_tables.fin_loan_details.search(loan_updated_status=q.like('foreclosure%'), borrower_customer_id=self.user_id)

        # Update label texts with the count of items in each repeating panel
        self.label_5.text = str(len(self.repeating_panel_6.items))
        self.label_6.text = str(len(self.repeating_panel_7.items))
        self.label_7.text = str(len(self.repeating_panel_8.items))
        self.label_8.text = str(len(self.repeating_panel_9.items))
        self.label_9.text = str(len(self.repeating_panel_10.items))

    def home_borrower_registration_form_copy_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('borrower_registration_form.dashboard')

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        self.label_1.visible = True
        self.label_2.visible = False
        self.label_3.visible = False
        self.label_4.visible = False
        self.label_10.visible = False
        self.repeating_panel_6.visible = True
        self.repeating_panel_7.visible = False
        self.repeating_panel_8.visible = False
        self.repeating_panel_9.visible = False
        self.repeating_panel_10.visible = False

    def button_2_click(self, **event_args):
        """This method is called when the button is clicked"""
        self.label_1.visible = False
        self.label_2.visible = True
        self.label_3.visible = False
        self.label_4.visible = False
        self.label_10.visible = False
        self.repeating_panel_6.visible = False
        self.repeating_panel_7.visible = True
        self.repeating_panel_8.visible = False
        self.repeating_panel_9.visible = False
        self.repeating_panel_10.visible = False 

    def button_3_click(self, **event_args):
        """This method is called when the button is clicked"""
        self.label_1.visible = False
        self.label_2.visible = False
        self.label_3.visible = True
        self.label_4.visible = False
        self.label_10.visible = False
        self.repeating_panel_6.visible = False
        self.repeating_panel_7.visible = False
        self.repeating_panel_8.visible = True
        self.repeating_panel_9.visible = False
        self.repeating_panel_10.visible = False

    def button_4_click(self, **event_args):
        """This method is called when the button is clicked"""
        self.label_1.visible = False
        self.label_2.visible = False
        self.label_3.visible = False
        self.label_4.visible = True
        self.label_10.visible = False
        self.repeating_panel_6.visible = False
        self.repeating_panel_7.visible = False
        self.repeating_panel_8.visible = False
        self.repeating_panel_9.visible = True
        self.repeating_panel_10.visible = False

    def button_5_click(self, **event_args):
        """This method is called when the button is clicked"""
        self.label_1.visible = False
        self.label_2.visible = False
        self.label_3.visible = False
        self.label_4.visible = False
        self.label_10.visible = True
        self.repeating_panel_6.visible = False
        self.repeating_panel_7.visible = False
        self.repeating_panel_8.visible = False
        self.repeating_panel_9.visible = False
        self.repeating_panel_10.visible = True  