
from tkinter import *
from tkinter import ttk, messagebox

from controller import BankController


class BankView:

    def __init__(self, root):

        self.root = root
        self.root.title("Bank Management System")
        self.root.geometry("1000x650")
        self.root.resizable(False, False)

        self.controller = BankController()
        self.selected_account = None

        self.create_widgets()
        self.display_accounts()

    # Convert account data into a consistent tuple
    def get_account_values(self, account):

        if hasattr(account, "keys"):
            return (
                account["account_no"],
                account["name"],
                account["balance"],
                account["account_type"]
            )

        return (
            account[0],
            account[1],
            account[2],
            account[3]
        )

    # Create All GUI Widgets
    def create_widgets(self):

        # Title
        title = Label(
            self.root,
            text="Bank Management System",
            font=("Arial", 22, "bold"),
            bg="#54089A",
            fg="white",
            pady=15
        )
        title.pack(fill="x")

        # Main Frame
        main_frame = Frame(
            self.root,
            padx=20,
            pady=15
        )
        main_frame.pack(fill="both", expand=True)

        # Account Details Form
        form_frame = LabelFrame(
            main_frame,
            text="Account Details",
            font=("Arial", 12, "bold"),
            padx=15,
            pady=15
        )
        form_frame.pack(fill="x", pady=10)

        # Account Number
        Label(
            form_frame,
            text="Account Number:"
        ).grid(row=0, column=0, padx=10, pady=8, sticky="w")

        self.account_entry = Entry(
            form_frame,
            width=25
        )
        self.account_entry.grid(row=0, column=1, padx=10, pady=8)

        # Account Holder
        Label(
            form_frame,
            text="Account Holder:"
        ).grid(row=0, column=2, padx=10, pady=8, sticky="w")

        self.name_entry = Entry(
            form_frame,
            width=25
        )
        self.name_entry.grid(row=0, column=3, padx=10, pady=8)

        # Balance
        Label(
            form_frame,
            text="Balance:"
        ).grid(row=1, column=0, padx=10, pady=8, sticky="w")

        self.balance_entry = Entry(
            form_frame,
            width=25
        )
        self.balance_entry.grid(row=1, column=1, padx=10, pady=8)

        # Account Type
        Label(
            form_frame,
            text="Account Type:"
        ).grid(row=1, column=2, padx=10, pady=8, sticky="w")

        self.type_combo = ttk.Combobox(
            form_frame,
            values=["Savings", "Current"],
            width=22,
            state="readonly"
        )
        self.type_combo.grid(row=1, column=3, padx=10, pady=8)

        # Buttons Frame
        button_frame = Frame(main_frame)
        button_frame.pack(fill="x", pady=10)

        # Create Account
        Button(
            button_frame,
            text="Create Account",
            width=15,
            bg="green",
            fg="white",
            command=self.create_account
        ).pack(side="left", padx=5)

        # Update Details
        Button(
            button_frame,
            text="Update Details",
            width=15,
            bg="blue",
            fg="white",
            command=self.update_account
        ).pack(side="left", padx=5)

        # Delete Account
        Button(
            button_frame,
            text="Delete Account",
            width=15,
            bg="red",
            fg="white",
            command=self.delete_account
        ).pack(side="left", padx=5)

        # Clear Fields
        Button(
            button_frame,
            text="Clear Fields",
            width=15,
            bg="gray",
            fg="white",
            command=self.clear_fields
        ).pack(side="left", padx=5)

        # Search Frame
        search_frame = Frame(main_frame)
        search_frame.pack(fill="x", pady=10)

        Label(
            search_frame,
            text="Search Account:",
            font=("Arial", 11, "bold")
        ).pack(side="left", padx=5)

        self.search_entry = Entry(
            search_frame,
            width=30
        )
        self.search_entry.pack(side="left", padx=5)

        # Search Button
        Button(
            search_frame,
            text="Search",
            width=12,
            bg="#54089A",
            fg="white",
            command=self.search_account
        ).pack(side="left", padx=5)

        # Show All Button
        Button(
            search_frame,
            text="Show All",
            width=12,
            command=self.display_accounts
        ).pack(side="left", padx=5)

        # Account Table Frame
        table_frame = Frame(main_frame)
        table_frame.pack(fill="both", expand=True, pady=10)

        # Table Columns
        columns = (
            "account_no",
            "name",
            "balance",
            "account_type"
        )

        # Treeview
        self.account_table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=10
        )

        # Table Headings
        self.account_table.heading(
            "account_no",
            text="Account Number"
        )

        self.account_table.heading(
            "name",
            text="Account Holder"
        )

        self.account_table.heading(
            "balance",
            text="Balance"
        )

        self.account_table.heading(
            "account_type",
            text="Account Type"
        )

        # Column Width
        self.account_table.column("account_no", width=180)
        self.account_table.column("name", width=250)
        self.account_table.column("balance", width=180)
        self.account_table.column("account_type", width=180)

        # Scrollbar
        scrollbar = ttk.Scrollbar(
            table_frame,
            orient=VERTICAL,
            command=self.account_table.yview
        )

        self.account_table.configure(
            yscrollcommand=scrollbar.set
        )

        self.account_table.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        # Select Table Row
        self.account_table.bind(
            "<<TreeviewSelect>>",
            self.select_account
        )

    # Create Account
    def create_account(self):

        account_no = self.account_entry.get().strip()
        name = self.name_entry.get().strip()
        balance = self.balance_entry.get().strip()
        account_type = self.type_combo.get()

        if not account_no or not name or not balance or not account_type:
            messagebox.showerror("Error", "Please fill all fields")
            return

        try:
            balance = float(balance)

            if balance < 0:
                messagebox.showerror("Error", "Balance cannot be negative")
                return

            self.controller.create_account(
                account_no, name, balance, account_type
            )

            messagebox.showinfo(
                "Success",
                "Account created successfully"
            )

            self.clear_fields()
            self.display_accounts()

        except ValueError:
            messagebox.showerror("Error", "Invalid balance")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Display All Accounts
    def display_accounts(self):

        for row in self.account_table.get_children():
            self.account_table.delete(row)

        try:
            accounts = self.controller.get_all_accounts()

            for account in accounts:

                values = self.get_account_values(account)

                self.account_table.insert(
                    "",
                    END,
                    values=values
                )

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Search Account
    def search_account(self):

        keyword = self.search_entry.get().strip()

        if not keyword:
            messagebox.showwarning(
                "Warning",
                "Please enter account number"
            )
            return

        try:
            account = self.controller.search_account(keyword)

            for row in self.account_table.get_children():
                self.account_table.delete(row)

            if account:

                values = self.get_account_values(account)

                self.account_table.insert(
                    "",
                    END,
                    values=values
                )

            else:
                messagebox.showinfo(
                    "Not Found",
                    "Account not found"
                )

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Select Account
    def select_account(self, event):

        selected = self.account_table.selection()

        if selected:

            values = self.account_table.item(
                selected[0],
                "values"
            )

            self.selected_account = values[0]

            self.account_entry.delete(0, END)
            self.account_entry.insert(0, values[0])

            self.name_entry.delete(0, END)
            self.name_entry.insert(0, values[1])

            self.balance_entry.delete(0, END)
            self.balance_entry.insert(0, values[2])

            self.type_combo.set(values[3])

    # Update Account
    def update_account(self):

        if not self.selected_account:
            messagebox.showwarning(
                "Warning",
                "Please select an account first"
            )
            return

        account_no = self.account_entry.get().strip()
        name = self.name_entry.get().strip()
        balance = self.balance_entry.get().strip()
        account_type = self.type_combo.get()

        if not account_no or not name or not balance or not account_type:
            messagebox.showerror("Error", "Please fill all fields")
            return

        try:
            balance = float(balance)

            if balance < 0:
                messagebox.showerror(
                    "Error",
                    "Balance cannot be negative"
                )
                return

            self.controller.update_account(
                self.selected_account,
                account_no,
                name,
                balance,
                account_type
            )

            messagebox.showinfo(
                "Success",
                "Account updated successfully"
            )

            self.clear_fields()
            self.display_accounts()

        except ValueError:
            messagebox.showerror("Error", "Invalid balance")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Delete Account
    def delete_account(self):

        if not self.selected_account:
            messagebox.showwarning(
                "Warning",
                "Please select an account first"
            )
            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this account?"
        )

        if confirm:

            try:
                self.controller.delete_account(
                    self.selected_account
                )

                messagebox.showinfo(
                    "Success",
                    "Account deleted successfully"
                )

                self.clear_fields()
                self.display_accounts()

            except Exception as e:
                messagebox.showerror("Error", str(e))

    # Clear Fields
    def clear_fields(self):

        self.account_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.balance_entry.delete(0, END)

        self.type_combo.set("")
        self.search_entry.delete(0, END)

        self.selected_account = None

        for item in self.account_table.selection():
            self.account_table.selection_remove(item)
