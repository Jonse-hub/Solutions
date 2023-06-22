import tkinter as tk

main_window = tk.Tk()
main_window.title('my first GUI')
main_window.geometry("500x500")

padx = 10
pady = 10

frame_1 = tk.LabelFrame(main_window, text="Container")
frame_1.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)

frame_1.columnconfigure(0, weight=1)
frame_1.columnconfigure(1, weight=2)
frame_1.rowconfigure(0, weight=2)
frame_1.rowconfigure(1, weight=1)

label_1 = tk.Label(frame_1, text="Label 1")
label_1.grid(row=0, column=0)

button_1 = tk.Button(frame_1, text="Button 1")
button_1.grid(row=1, column=0)


if __name__ == "__main__":
    main_window.mainloop()
