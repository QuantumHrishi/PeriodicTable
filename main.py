import tkinter as tk
from elements import Elements

length = 117

window = tk.Tk()
window.title('The Periodic Database')

label = tk.Label(text="What Element do you want to search?")
label.grid(row='1', column='9')
Elementneeded = tk.Entry(width=50)
Elementneeded.grid(row='3', column='9')
Text_box = tk.Text(height='100', width='120', wrap='word')
Text_box.grid(row='8', column='9', columnspan='1')


def Clearbox():
    Text_box.delete('1.0', 'end')
    Elementneeded.delete(0, 'end')
    Stringvar.set('None')


Num = 0


def Next(self):
    global Num
    global Stringvar
    try:

        Num = list(Elements).index(Elementneeded.get().lower())
        if Num == length:
            Num = 0
            Index = list(Elements.keys())[Num]
            Elementneeded.delete(0, 'end')
            Elementneeded.insert(0, Index)
            Newindex = Elements[Index]
            Text_box.delete('1.0', 'end')
            Text_box.insert('1.0', Newindex)
            Stringvar.set(Elementneeded.get().lower())

        else:
            Num = Num + 1
            Index = list(Elements.keys())[Num]
            Elementneeded.delete(0, 'end')
            Elementneeded.insert(0, Index)
            Newindex = Elements[Index]
            Text_box.delete('1.0', 'end')
            Text_box.insert('1.0', Newindex)
            Stringvar.set(Elementneeded.get().lower())
    except:
        Text_box.delete('1.0', 'end')
        Text_box.insert(
            '1.0',
            'You can not move through elements if no valid element is selected'
        )


def Back(self):
    global Stringvar
    global Num
    try:

        Num = list(Elements).index(Elementneeded.get().lower())
        if Num == 0:
            Num = length
            Index = list(Elements.keys())[Num]
            Elementneeded.delete(0, 'end')
            Elementneeded.insert(0, Index)
            Newindex = Elements[Index]
            Text_box.delete('1.0', 'end')
            Text_box.insert('1.0', Newindex)
            Stringvar.set(Elementneeded.get().lower())
        else:
            Num = Num - 1
            Index = list(Elements.keys())[Num]
            Elementneeded.delete(0, 'end')
            Elementneeded.insert(0, Index)
            Newindex = Elements[Index]
            Text_box.delete('1.0', 'end')
            Text_box.insert('1.0', Newindex)
            Stringvar.set(Elementneeded.get().lower())
    except:
        Text_box.delete('1.0', 'end')
        Text_box.insert(
            '1.0',
            'You can not move through elements if no valid element is selected'
        )


lis = []
for x in range(0, length):
    i = list(Elements.keys())[x]
    lis.append(i)


def callback(selection):
    Text_box.delete('1.0', 'end')
    Text_box.insert('1.0', Elements[selection])
    Elementneeded.delete(0, 'end')
    Elementneeded.insert(0, selection)


def Search(self):
    global Stringvar
    Text_box.delete('1.0', 'end')
    try:
        Text_box.insert('1.0', Elements[Elementneeded.get().lower()])
        Stringvar.set(Elementneeded.get().lower())
    except:
        Text_box.insert('1.0', 'That is not an element')


Stringvar = tk.StringVar(window, 'None')
Dropdown = tk.OptionMenu(window, Stringvar, *lis, command=callback)
Dropdown.grid(row='2', column='300', columnspan='2')
Clear = tk.Button(text="Clear", command=Clearbox)
Clear.grid(row='3', padx='500', column='300')
window.bind('<Return>', Search)
window.bind('<Right>', Next)
window.bind('<Left>', Back)
window.mainloop()
