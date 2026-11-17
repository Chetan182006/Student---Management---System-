
from tkinter import Tk
from view import BankView

def main():

    root = Tk()
    app = BankView(root)

    root.mainloop()


if __name__ == "__main__":
    main()
