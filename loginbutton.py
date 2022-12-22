import tkinter as tk

def on_login_button_clicked():
    # This function is called when the login button is clicked
    username = username_entry.get()  # Get the username from the entry widget
    password = password_entry.get()  # Get the password from the entry widget
    # Perform the login process (e.g. check the username and password against a database)

# Create the main window
window = tk.Tk()
window.title("Log In")

# Create a label for the username
username_label = tk.Label(text="Username:")
username_label.pack()

# Create an entry widget for the username
username_entry = tk.Entry()
username_entry.pack()

# Create a label for the password
password_label = tk.Label(text="Password:")
password_label.pack()

# Create an entry widget for the password
password_entry = tk.Entry(show="*")  # Show asterisks instead of the actual password
password_entry.pack()

# Create a login button
login_button = tk.Button(text="Log In", command=on_login_button_clicked)
login_button.pack()

# Run the main loop
window.mainloop()