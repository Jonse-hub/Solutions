""" Opgave "GUI step 4":

Som altid skal du læse hele øpgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2040.png

Genbrug din kode fra "GUI step 3".

Fyld treeview'en med testdata.
Leg med farveværdierne. Find en farvekombination, som du kan lide.

Funktionalitet:
    Klik på knappen "clear entry boxes" sletter teksten i alle indtastningsfelter (entries).
    Hvis du klikker på en datarække i træoversigten, kopieres dataene i denne række til indtastningsfelterne.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

import tkinter as tk
from tkinter import ttk


def create_entry():
    print("Create was pressed")
    # entry_1.delete(0, tk.END)

    test_data_list.append((int(Id_entry_1.get()), int(
        weight_entry_1.get()), Destination_entry_1.get()))

    read_table(tree_1)

    Id_entry_1.delete(0, tk.END)
    weight_entry_1.delete(0, tk.END)
    Destination_entry_1.delete(0, tk.END)


def update_entry():
    print("Update was pressed")

    index_selected = tree_1.index(tree_1.focus())

    test_data_list.pop(int(index_selected))

    test_data_list.insert(int(index_selected), (int(Id_entry_1.get()), int(
        weight_entry_1.get()), Destination_entry_1.get()))

    # tree_1.update(index_selected, (int(Id_entry_1.get()), int(weight_entry_1.get()), Destination_entry_1.get()))

    # tree_1.item(index_selected, option=)

    # entry_1.delete(0, tk.END)
    # tree_1.update()
    read_table(tree_1)


def empty_entry():
    print("Delete was pressed")
    # entry_1.delete(0, tk.END)

    index_selected = tree_1.focus()  # Index of selected tuple
    test_data_list.pop(int(tree_1.index(index_selected)))
    tree_1.delete(index_selected)


def empty_entries():
    print("Clear Entry Boxes was pressed")
    Id_entry_1.delete(0, tk.END)
    weight_entry_1.delete(0, tk.END)
    Destination_entry_1.delete(0, tk.END)
    Weather_entry_1.delete(0, tk.END)


def read_table(tree):  # fill tree with test data
    # Use counter to keep track of odd and even rows, because these will be colored differently. (2)

    tree.delete(*tree.get_children())

    count = 0
    for record in test_data_list:
        if count % 2 == 0:  # even
            tree.insert(parent='', index='end', text='', values=record, tags=(
                'evenrow',))  # Insert one row into the data table
        else:  # odd
            tree.insert(parent='', index='end', text='', values=record, tags=(
                'oddrow',))  # Insert one row into the data table
        count += 1


# Copy data from selected row into entry box. Parameter event is mandatory but we don't use it. (1)
def edit_record(event, tree):
    index_selected = tree.focus()  # Index of selected tuple
    values = tree.item(index_selected, 'values')  # Values of selected tuple
    # Delete text in entry box, beginning with the first character (0) and ending with the last character (tk.END)
    Id_entry_1.delete(0, tk.END)
    Id_entry_1.insert(0, values[0])  # write data into entry box
    weight_entry_1.delete(0, tk.END)
    weight_entry_1.insert(0, values[1])
    Destination_entry_1.delete(0, tk.END)
    Destination_entry_1.insert(0, values[2])


padx = 5
pady = 10
rowheight = 24
treeview_background = "#eeeeee"
treeview_foreground = "black"
treeview_selected = "#773333"
oddrow = "#ddeedd"  # color of odd row in treeview (1)
evenrow = "#cce0cc"  # color of even row in treeview


main_window = tk.Tk()
main_window.title('my first GUI')
main_window.geometry("700x550")

frame_1 = tk.LabelFrame(main_window, text="Container")
frame_1.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)

treeview_frame = tk.Frame(frame_1)
treeview_frame.grid(row=1, column=0, padx=padx, pady=pady, sticky=tk.N)

style = ttk.Style()  # Configure treeview style and colors
style.theme_use('default')
style.configure("Treeview", background=treeview_background, foreground=treeview_foreground,
                rowheight=rowheight, fieldbackground=treeview_background)
style.map('Treeview', background=[('selected', treeview_selected)])

# create a scrollbar and a treeview
tree_1_scrollbar = tk.Scrollbar(treeview_frame)
tree_1_scrollbar.grid(row=5, column=6, padx=padx, pady=pady, sticky='ns')
tree_1 = ttk.Treeview(
    treeview_frame, yscrollcommand=tree_1_scrollbar.set, selectmode="browse")
tree_1.grid(row=5, column=5, padx=0, pady=pady)
tree_1_scrollbar.config(command=tree_1.yview)

tree_1['columns'] = ("col1", "col2", "col3")  # Define treeview columns
tree_1.column("#0", width=0, stretch=tk.NO)
tree_1.column("col1", anchor=tk.E, width=90)
tree_1.column("col2", anchor=tk.W, width=130)
tree_1.column("col3", anchor=tk.W, width=180)

tree_1.heading("#0", text="", anchor=tk.W)  # Create treeview column headings
tree_1.heading("col1", text="Id", anchor=tk.CENTER)
tree_1.heading("col2", text="Weight", anchor=tk.CENTER)
tree_1.heading("col3", text="Destination", anchor=tk.CENTER)

test_data_list = []
test_data_list.append(("1", 1000, "Olso"))
test_data_list.append(("2", 2000, "Chicago"))
test_data_list.append(("3", 3000, "Milano"))
test_data_list.append(("4", 4000, "Amsterdam"))

# Create tags for rows in 2 different colors (3)
tree_1.tag_configure('oddrow', background=oddrow)
tree_1.tag_configure('evenrow', background=evenrow)

# Define function to be called, when an item is selected. (2)
tree_1.bind("<ButtonRelease-1>", lambda event: edit_record(event, tree_1))


frame_2 = tk.Frame(frame_1)
frame_2.grid(row=2, column=0, padx=padx, pady=pady, sticky=tk.N)

label_1 = tk.Label(frame_2, text="Id")
label_1.grid(row=0, column=0, padx=padx, pady=pady)
Id_entry_1 = tk.Entry(frame_2, width=10, justify="right")
Id_entry_1.grid(row=1, column=0, padx=padx, pady=pady)

label_1 = tk.Label(frame_2, text="Weight")
label_1.grid(row=0, column=1, padx=padx, pady=pady)
weight_entry_1 = tk.Entry(frame_2, width=15, justify="right")
weight_entry_1.grid(row=1, column=1, padx=padx, pady=pady)

label_1 = tk.Label(frame_2, text="Destination")
label_1.grid(row=0, column=2, padx=padx, pady=pady)
Destination_entry_1 = tk.Entry(frame_2, width=25, justify="right")
Destination_entry_1.grid(row=1, column=2, padx=padx, pady=pady)

label_1 = tk.Label(frame_2, text="Weather")
label_1.grid(row=0, column=3, padx=padx, pady=pady)
Weather_entry_1 = tk.Entry(frame_2, width=20, justify="right")
Weather_entry_1.grid(row=1, column=3, padx=padx, pady=pady)

frame_3 = tk.Frame(frame_1)
frame_3.grid(row=3, column=0, padx=padx, pady=pady, sticky=tk.N)

Create_button_1 = tk.Button(frame_3, text="Create", command=create_entry)
Create_button_1.grid(row=0, column=0, padx=padx, pady=pady)
Update_button_1 = tk.Button(frame_3, text="Update", command=update_entry)
Update_button_1.grid(row=0, column=1, padx=padx, pady=pady)
Delete_button_1 = tk.Button(frame_3, text="Delete", command=empty_entry)
Delete_button_1.grid(row=0, column=2, padx=padx, pady=pady)
Clear_All_button_1 = tk.Button(
    frame_3, text="Clear Entry Boxes", command=empty_entries)
Clear_All_button_1.grid(row=0, column=3, padx=padx, pady=pady)

read_table(tree_1)  # read the test data into the treeview

if __name__ == "__main__":
    main_window.mainloop()
