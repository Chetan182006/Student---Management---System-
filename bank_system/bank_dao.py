import mysql.connector
from model import BankAccount

class BankDAO:

    def connect(self):
    
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="Chetan@9352",
            database="bank_db"
            )

    def create_account(self,account):

        con = self.connect()
        cursor = con.cursor()

        try:
            query = """
                INSERT INTO accounts
                (name,age,address,phone,email,balance)
                VALUES(%s,%s,%s,%s,%s,%s)
                """

            values = (
                account.get_name(),
                account.get_age(),
                account.get_address(),
                account.get_phone(),
                account.get_email(),
                account.get_balance()
            )

            cursor.execute(query,values)
            con.commit()

            return True

        except Exception:
            con.rollback()
            raise

        finally:
            cursor.close()
            con.close()


    def get_all_accounts(self):
        con = self.connect()
        cursor = con.cursor()

        try:
            query = "SELECT * FROM accounts ORDER BY account_no"
            cursor.execute(query)

            records = cursor.fetchall()

            return records

        finally:
            cursor.close()
            con.close()


    def search_account(self,account_no):
        con = self.connect()
        cursor = con.cursor()

        try:
            query = "SELECT * FROM accounts WHERE account_no=%s"
            cursor.execute(query,(account_no,))

            records = cursor.fetchone()

            return records

        finally:
            cursor.close()
            con.close()


    def update_account(self,account):
        con = self.connect()
        cursor = con.cursor()

        try:

            query = """
                UPDATE accounts
                SET name=%s,
                    age=%s,
                    address=%s,
                    phone=%s,
                    email=%s
                WHERE account_no=%s"""

            values = (
                account.get_name(),
                account.get_age(),
                account.get_address(),
                account.get_phone(),
                account.get_email(),
                account.get_account_no()
            )

            cursor.execute(query,values)

            con.commit()

            return cursor.rowcount > 0

        except Exception:
            con.rollback()
            raise

        finally:
            cursor.close()
            con.close()


    def delete_account(self,account_no):
        con = self.connect()
        cursor = con.cursor()

        try:
            query = "DELETE FROM accounts WHERE account_no=%s"
            cursor.execute(query,(account_no,))

            con.commit()
            return cursor.rowcount > 0

        except Exception:
            con.rollback()
            raise

        finally:
            cursor.close()
            con.close()
