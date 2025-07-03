import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter.scrolledtext import ScrolledText

contacts = []
def add_contact():
    name = simpledialog.askstring("Add Contact", "Enter Name:")
    if not name: return

    phone = simpledialog.askstring("Add Contact", "Enter Phone Number:")
    email = simpledialog.askstring("Add Contact", "Enter Email:")
    address = simpledialog.askstring("Add Contact", "Enter Address:")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    messagebox.showinfo(" Success", "Contact added successfully!")

def view_contacts():
    output.delete("1.0", tk.END)
    if not contacts:
        output.insert(tk.END, " No contacts found.\n")
    else:
        for i, c in enumerate(contacts, start=1):
            output.insert(tk.END, f"\n Contact {i}\n")
            output.insert(tk.END, f" Name   : {c['name']}\n")
            output.insert(tk.END, f" Phone  : {c['phone']}\n")
            output.insert(tk.END, f" Email  : {c['email']}\n")
            output.insert(tk.END, f" Address: {c['address']}\n")

def search_contact():
    keyword = simpledialog.askstring("Search", "Enter name or phone number:")
    if not keyword: return
    output.delete("1.0", tk.END)
    found = False
    for c in contacts:
        if keyword.lower() in c["name"].lower() or keyword in c["phone"]:
            output.insert(tk.END, f"\nFound Contact\n")
            output.insert(tk.END, f" Name   : {c['name']}\n")
            output.insert(tk.END, f" Phone  : {c['phone']}\n")
            output.insert(tk.END, f" Email  : {c['email']}\n")
            output.insert(tk.END, f" Address: {c['address']}\n")
            found = True
    if not found:
        output.insert(tk.END, " No matching contact found.\n")

def update_contact():
    name = simpledialog.askstring("Update", "Enter the name of the contact to update:")
    for c in contacts:
        if c["name"].lower() == name.lower():
            new_name = simpledialog.askstring("Update", f"New Name ({c['name']}):") or c["name"]
            new_phone = simpledialog.askstring("Update", f"New Phone ({c['phone']}):") or c["phone"]
            new_email = simpledialog.askstring("Update", f"New Email ({c['email']}):") or c["email"]
            new_address = simpledialog.askstring("Update", f"New Address ({c['address']}):") or c["address"]

            c["name"] = new_name
            c["phone"] = new_phone
            c["email"] = new_email
            c["address"] = new_address

            messagebox.showinfo("Success", "Contact updated successfully!")
            return
    messagebox.showerror("Error", "Contact not found.")

def delete_contact():
    name = simpledialog.askstring("Delete", "Enter the name of the contact to delete:")
    for i, c in enumerate(contacts):
        if c["name"].lower() == name.lower():
            del contacts[i]
            messagebox.showinfo(" Deleted", "Contact deleted successfully!")
            return
    messagebox.showerror(" Error", "Contact not found.")

root = tk.Tk()
root.title("📘 Contact Book")
root.configure(bg="#970DE1")
root.geometry("600x500")
root.resizable(False, False)

header = tk.Label(root, text=" Contact Book", bg="#CF3838", fg="white",
                  font=("Arial Rounded MT Bold", 18), pady=10, padx=10)
header.pack(fill=tk.X)

btn_frame = tk.Frame(root, bg="#D0109D")
btn_frame.pack(pady=15)

button_style = {
    "width": 18,
    "font": ("Verdana", 10, "bold"),
    "bg": "#3D794E",
    "fg": "black",
    "activebackground": "#51A461",
    "relief": "raised",
    "bd": 2,
    "padx": 5,
    "pady": 5
}

tk.Button(btn_frame, text="Add Contact", command=add_contact, **button_style).grid(row=0, column=0, padx=10, pady=8)
tk.Button(btn_frame, text="View Contacts List", command=view_contacts, **button_style).grid(row=0, column=1, padx=10, pady=8)
tk.Button(btn_frame, text="Search Contact", command=search_contact, **button_style).grid(row=1, column=0, padx=10, pady=8)
tk.Button(btn_frame, text="Update Contact", command=update_contact, **button_style).grid(row=1, column=1, padx=10, pady=8)
tk.Button(btn_frame, text="Delete Contact", command=delete_contact, **button_style).grid(row=2, column=0, columnspan=2, pady=10)

output_label = tk.Label(root, text=" Output:", bg="#c78005", font=("Arial", 15, "bold"))
output_label.pack(anchor="w", padx=20)

output = ScrolledText(root, width=70, height=15, font=("Consolas", 11), wrap=tk.WORD, bd=2, relief="sunken")
output.pack(padx=20, pady=5)
root.mainloop()