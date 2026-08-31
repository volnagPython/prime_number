import tkinter as tk
from mainPrNumbers_g import ver_num


def master_win():

    master = tk.Tk()
    master.geometry("400x260")
    master.resizable(0, 0)
    master.title("ПРОСТІ ЧИСЛА")

    menu_bar = tk.Menu(master)
    master.config(menu=menu_bar)

    var_number = tk.StringVar(master)

    frame1 = tk.Frame(master, bg="deep sky blue", bd=5)
    frame1.place(
        relx=0.5,
        rely=0.2,
        relwidth=0.95,
        relheight=0.5,
        anchor='n'
    )

    label2 = tk.Label(
        master,
        bg='light yellow',
        text='Введіть у вікні своє число (1-999)',
        font=('Courier', 12)
    )
    label2.pack(side="top", padx=5, pady=10)

    entry_field = tk.Entry(
        frame1,
        font=('Courier', 74, 'bold'),
        bd=5,
        justify="center",
        textvariable = var_number
    )
    entry_field.place(
        relx=0.05,
        rely=0,
        relwidth=0.45,
        relheight=0.95
    )

    frame2 = tk.Frame(master, bg="green", bd=5)
    frame2.place(
        relx=0.5,
        rely=0.8,
        relwidth=0.85,
        relheight=0.15,
        anchor='n'
    )

    label1 = tk.Label(frame2, bg="yellow")
    label1.place(
        relx=0.05,
        rely=0.2,
        relwidth=0.9,
        relheight=0.65
    )

    def win_clear():
        var_number.set('')
        label1.config(text='')

    def out_print():
        my_number = var_number.get()
        num_pop = ver_num(my_number)
        label1.config(
            text=f"{num_pop}"
        )

        print("my_number =", my_number)

    button1 = tk.Button(
        frame1,
        text="Перевірити",
        bg="gray",
        fg="white",
        font=('Courier', 10, 'bold'),
        command = out_print
    )
    button1.place(
        relx=0.55,
        rely=0.12,
        relwidth=0.45,
        relheight=0.25
    )

    button2 = tk.Button(
        frame1,
        text="Очистити",
        bg="gray",
        fg="white",
        font=('Courier', 10, 'bold'),
        command = win_clear
    )
    button2.place(
        relx=0.6,
        rely=0.52,
        relwidth=0.35,
        relheight=0.25
    )

    menu_bar.add_command(label="Очистити", command = win_clear)
    menu_bar.add_command(label="Вийти", command = master.destroy)

    master.mainloop()


master_win()