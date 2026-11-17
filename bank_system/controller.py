
from model import BankAccount
from bank_dao import BankDAO


class BankController:

    def __init__(self):
        self.dao = BankDAO()

    # Create Account
    def create_account(self, name, age, address,
                       phone, email, balance):

        bank_obj = BankAccount(
            None,
            name,
            age,
            address,
            phone,
            email,
            balance
        )

        return self.dao.create_account(bank_obj)

    # Display All Accounts
    def get_all_accounts(self):

        return self.dao.get_all_accounts()

    # Search Account
    def search_account(self, account_no):

        return self.dao.search_account(account_no)

    # Update Account
    def update_account(self, account_no, name, age,
                       address, phone, email):

        bank_obj = BankAccount(
            account_no,
            name,
            age,
            address,
            phone,
            email,
            None
        )

        return self.dao.update_account(bank_obj)

    # Delete Account
    def delete_account(self, account_no):

        return self.dao.delete_account(account_no)
