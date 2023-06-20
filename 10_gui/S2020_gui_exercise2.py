""" Opgave "GUI step 2":

Som altid skal du læse hele øpgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2020.png

Genbrug din kode fra "GUI step 1".

GUI-strukturen bør være som følger:
    main window
        labelframe
            frame
                labels and entries
            frame
                buttons

Funktionalitet:
    Klik på knappen "clear entry boxes" sletter teksten i alle indtastningsfelter (entries).

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

import tkinter as tk


def create_entry():
    print("Create was pressed")
    # entry_1.delete(0, tk.END)


def update_entry():
    print("Update was pressed")
    # entry_1.delete(0, tk.END)


def empty_entry():
    print("Delete was pressed")
    # entry_1.delete(0, tk.END)


def empty_entries():
    print("Clear Entry Boxes was pressed")
    Id_entry_1.delete(0, tk.END)
    weight_entry_1.delete(0, tk.END)
    Destination_entry_1.delete(0, tk.END)
    Weather_entry_1.delete(0, tk.END)


main_window = tk.Tk()
main_window.title('my first GUI')
main_window.geometry("700x400")

padx = 5
pady = 10

frame_1 = tk.LabelFrame(main_window, text="Container")
frame_1.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)

frame_2 = tk.Frame(frame_1)
frame_2.grid(row=1, column=0, padx=padx, pady=pady, sticky=tk.N)

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
frame_3.grid(row=2, column=0, padx=padx, pady=pady, sticky=tk.N)

Create_button_1 = tk.Button(frame_3, text="Create", command=create_entry)
Create_button_1.grid(row=0, column=0, padx=padx, pady=pady)
Update_button_1 = tk.Button(frame_3, text="Update", command=update_entry)
Update_button_1.grid(row=0, column=1, padx=padx, pady=pady)
Delete_button_1 = tk.Button(frame_3, text="Delete", command=empty_entry)
Delete_button_1.grid(row=0, column=2, padx=padx, pady=pady)
Clear_All_button_1 = tk.Button(
    frame_3, text="Clear Entry Boxes", command=empty_entries)
Clear_All_button_1.grid(row=0, column=3, padx=padx, pady=pady)

if __name__ == "__main__":
    main_window.mainloop()
