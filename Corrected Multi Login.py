from tkinter import *  # noqa: F403
from tkinter import messagebox

class MultiLoginPage:
    def __init__(self, root):
        # Initialize the main window 
        self.root = root 
        self.root.title("Login Page")
        self.root.geometry("400x350")
        
        self.create_login_page()  # Call to create the login page at initialization

    def create_login_page(self):
        # Creating frames for labels and button
        self.username_frame = Frame(self.root, bg="#ccffff")
        self.username_frame.pack(pady=20)
        self.password_frame = Frame(self.root, bg="#ccffff")
        self.password_frame.pack(pady=20)
        self.login_button_frame = Frame(self.root, bg="#ccffff")
        self.login_button_frame.pack(pady=10)

        # Creating username label and entry field
        self.username_label = Label(self.username_frame, text="Username:", font=("Arial", 12))
        self.username_label.pack(pady=5)
        self.username_entry = Entry(self.username_frame)
        self.username_entry.pack(pady=5)

        # Creating password label and entry field
        self.password_label = Label(self.password_frame, text="Password:", font=("Arial", 12))
        self.password_label.pack(pady=5)
        self.password_entry = Entry(self.password_frame, show="*")
        self.password_entry.pack(pady=5)

        # Creating login button
        self.login_button = Button(self.login_button_frame, text="Login", command=self.check_login)
        self.login_button.pack(pady=10)

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check login credentials
        if username == "admin" and password == "admin":
            self.create_home_page("Admin Home Page")
        elif username == "user" and password == "user":
            self.create_home_page("User Home Page")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def create_home_page(self, title):
        # Clear previous widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Creating home page label
        self.home_page_label = Label(self.root, text=title, font=("Arial", 16, "bold"))
        self.home_page_label.pack(pady=20)

        # Creating logout button
        self.logout_button = Button(self.root, text="Logout", command=self.create_login_page)
        self.logout_button.pack(pady=10)

# Running the login page
if __name__ == "__main__":
    root = Tk()
    app = MultiLoginPage(root)  # Create an instance of the MultiLoginPage class
    root.mainloop()