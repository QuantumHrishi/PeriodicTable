import tkinter as tk

length = 92


def form(Number, abrev, mass, group, melt, boil, dence, color, radius):
    Atomicnumber = float(Number)

    if Atomicnumber > 96:
        State = 'Solid'
        if Atomicnumber > 103:
            State = 'Unknown'

    else:

        Meltcalc = float(melt)
        Boilcalc = float(boil)
        if Meltcalc > 22.22:
            State = 'Solid'
        if Meltcalc < 22.22 and Boilcalc > 22.22:
            State = 'Liquid'
        if Boilcalc < 22.22:
            State = 'Gas'
    if group == 'Noble Gases':
        Inert = 'Yes'
    else:
        Inert = 'No'
    New_Number = int(Number)
    New_mass = float(mass)
    NeutronsCalc = New_mass - New_Number
    Neutrons = round(NeutronsCalc, 0)

    result = "Atomic Number:{} \n Abbreviation:{} \n Atomic Mass:{} u \n Group:{} \n Protons:{} \n Neutrons:{} \n Electrons: {} \n Melting Point: {} °C \n Boiling Point:{} °C \n Inert:{} \n State of matter at room temperature:{} \n Density:{}kg/Meters Cubed \n  Color:{} \n Atomic Radius:{} Pm".format(
        Number, abrev, mass, group, Number, Neutrons, Number, melt, boil, Inert, State, dence, color, radius)
    return result


Elements = {"Hydrogen": form('1', 'H', '1.008', 'Reactive Nonmetals,', '-259.1', '-252.9', '0.0899', 'None', '53'),
            "Helium": form('2', 'HE', '4.0026', 'Noble Gases', '-272.2', '-269', '0.1785', 'None', '31'),
            "Lithium": form('3', 'LI', '6.94', 'Alkali Metals', '180.54', '1342', '535', 'Silver', '167'),
            'Beryllium': form('4', 'BE', '9.0122', 'Alkaline Earth Metals', '1287', '2470', '1848', 'SlateGray', '112'),
            "Boron": form('5', 'B', '10.81', 'Metalloids', '2075', '4000', '2460', 'Black', '87'),
            "Carbon": form('6', 'C', '12.011', 'Reactive Nonmetals', '3642', '3642', '2260', 'Black', '67'),
            "Nitrogen": form('7', 'N', '14.007', 'Reactive Nonmetals', '-210.1', '-195.8', '1.251', 'None', '56'),
            "Oxygen": form('8', "O", '15.999', 'Reactive Nonmetals', '-218', '-183', '1.429', 'None', '48'),
            "Fluorine": form('9', "F", '18.998', 'Reactive Nonmetals', '-220', '-188.1', '1', 'None', '42'),
            "Neon": form('10', 'Ne', '20.180', 'Noble Gases', '-248.6', '-246.1', '0.9', 'None', '38'),
            "Sodium": form('11', "NA", '22.990', 'Alkali Metals', '97.72', '882.9', '968', 'Silver', '190'),
            'Magnesium': form('12', "MG", '24.305', 'Alkaline Earth Metals', '650', '1090', '1738', 'Silver', '145'),
            "Aluminum": form('13', 'AL', '26.982', 'Post Transiton Metals', '660.32', '2519', '2700', 'Silver', '118'),
            "Silicon": form('14', "Si", '28.085', 'Metalloids', '1414', '2900', '2330', 'Gray', '111'),
            "Phosphorus": form('15', 'P', '30.974', 'Reactive Nonmetals', '44.15', '280.5', '1823', 'None', '98'),
            "Sulfer": form('16', 'S', '32.06', 'Reactive Nonmetals', '115.21', '444.72', '1960', 'Yellow', '88'),
            "Chlorine": form('17', "CL", '35.45', 'Reactive Nonmetal', '-101.5', '-34.040', '3.214', 'Yellow', '79'),
            "Argon": form('18', "AR", '39.948', 'Noble Gases', '-189', '-186', '1.784', 'None', '71'),
            "Potassium": form('19', "K", '39.098', 'Alkali Metals', '63.38', '758.9', '856', 'Silver', '243'),
            "Calcium": form('20', 'CA', '40.078', 'Alkaline Earth Metals', '841.9', '1484', '1550', 'Silver', '194'),
            "Scandium": form('21', 'SC', '44.956', 'Transition Metals', '1541', '2830', '2985', 'Silver', '184'),
            "Titanium": form('22', "TI", '47.867', 'Transition Metals', '1668', '3287', '4507', 'Silver', '176'),
            "Vanadium": form('23', "V", '50.942', 'Transition Metals', '1910', '3407', '6110', 'Silver', '171'),
            "Chromium": form('24', 'CR', '51.996', 'Transition Metals', '1907', '2671', '7190', 'Silver', '166'),
            "Manganese": form('25', "MN", '54.938', 'Transition Metals', '1246', '2061', '7470', 'Silver', '161'),
            "Iron": form('26', "FE", '55.845', 'Transition Metals', '1538', '2861', '7874', 'Gray', '156'),
            "Cobalt": form('27', 'Co', '58.933', "Transition Metals", '1495', '2900', '8900', 'Gray', '152'),
            "Nickel": form('28', 'NI', '58.693', 'Transition Metals', '1455', '2913', '8908', 'Gray', '149'),
            'Copper': form('29', 'Cu', '63.546', 'Transition Metals', '1084.62', '2562', '8960', 'Copper', '145'),
            'Zinc': form('30', 'Zn', '65.38', 'Transition Metals', '419.53', '906.9', '7140', 'SlateGray', '142'),
            'Gallium': form('31', 'Ga', '69.723', 'Post-Transition Metals', '29.760', '2204', '5904', 'Silver', '136'),
            'Germanium': form('32', 'Ge', '72.630', 'Metalloids', '938.25', '2820', '5323', 'Gray', '125'),
            'Arsenic': form('33', 'As', '74.922', 'Metalloids', '816.9', '614', '5727', 'Silver', '114'),
            'Selenium': form('34', 'Se', '78.971', 'Reactive Nonmetals', '221', '685', '4819', 'Gray', '103'),
            'Bromine': form('35', 'Br', '79.904', 'Reactive Nonmetals', '-7.350', '58.9', '3120', 'Red', '94'),
            'Krypton': form('36', 'Kr', '83.798', 'Noble Gases', '-157.36', '-153.22', '3.75', 'None', '88'),
            'Rubidium': form('37', 'Rb', '85.468', 'Alkali Metals', '39.310', '688', '1532', 'Silver', '265'),
            'Strontium': form('38', 'Sr', '87.62', 'Alkaline Earth Metals', '776.9', '1382', '2630', 'Silver', '219'),
            'Yttrium': form('39', 'Y', '88.906', 'Transition Metals', '1526', '3345', '4472', 'Silver', '212'),
            'Zirconium': form('40', 'Zr', '91.224', 'Transition Metals', '1855', '4409', '6511', 'Silver', '206'),
            'Niobium': form('41', 'Nb', '92.906', 'Transition Metals', '2477', '4744', '8570', 'Gray', '198'),
            'Molubdenum': form('42', 'Mo', '95.95', 'Transition Metals', '2623', '4693', '10280', 'Gray', '190'),
            'Technetium': form('43', 'Tc', '98', 'Transition Metals', '2157', '4265', '11500', 'Silver', '183'),
            'Ruthenium': form('44', 'Ru', '101.07', 'Transition Metals', '2334', '4150', '12370', 'Silver', '178'),
            'Rhodium': form('45', 'Rh', '102.91', 'Transition Metals', '1964', '3695', '12450', 'Silver', '173'),
            'Palladium': form('46', 'Pd', '106.42', 'Transition Metals', '1554.90', '2963', '12023', 'Silver', '169'),
            'Silver': form('47', 'Ag', '107.87', 'Transition Metals', '961.78', '2162', '10490', 'Silver', '165'),
            'Cadmium': form('48', 'Cd', '112.41', 'Transition Metals', '321.07', '766.9', '8650', 'Silver', '161'),
            'Indium': form('49', 'In', '114.82', 'Post Transition Metals', '156.60', '2072', '7310', 'Silver', '156'),
            'Tin': form('50', 'Sn', '118.71', 'Post Transition Metals', '231.93', '2602', '7310', 'Silver', '145'),
            'Antimony': form('51', 'Sb', '121.76', 'Metalloids', '630.63', '1587', '6697', 'Silver', '133'),
            'Tellurium': form('52', 'Te', '127.60', 'Metalloids', '449.51', '987.9', '6240', 'Silver', '123'),
            'Iodine': form('53', 'I', '126.90', 'Reactive Nonmetals', '113.7', '184.3', '4940', 'SlateGray', '115'),
            'Xenon': form('54', 'Xe', '131.29', 'Noble Gases', '-111.8', '-108', '5.9', 'None', '108'),
            'Cesium': form('55', 'Cs', '132.91', 'Alkali Metals', '28.44', '671', '1879', 'Silver', '298'),
            'Caesium': form('55', 'Cs', '132.91', 'Alkali Metals', '28.44', '671', '1879', 'Silver', '298'),
            'Barium': form('56', 'Ba', '137.33', 'Alkaline Earth Metals', '730', '1870', '3510', 'Silver', '253'),
            'Lanthanum': form('57', 'La', '138.91', 'Lanthanoids', '919.9', '3464', '6146', 'Silver', None, ),
            'Cerium': form('58', 'Ce', '140.12', 'Lanthanoids', '797.9', '3360', '6689', 'Silver', None),
            'Praseodymium': form('59', 'Pr', '140.91', 'Lanthanoids', '930.9', '3290', '6640', 'Silver', '247'),
            'Neodymium': form('60', 'Nd', '144.24', 'Lanthanoids', '1021', '3100', '7010', 'Silver', '206'),
            'Promethium': form('61', 'Pm', '145', 'Lanthanoids', '1100', '3000', '7264', 'Silver', '205'),
            'Samarium': form('62', 'Sm', '150.36', 'Lanthanoids', '1072', '1803', '7353', 'Silver', '238'),
            'Europium': form('63', 'Eu', '151.96', 'Lanthanoids', '821.9', '1500', '5244', 'Silver', '231'),
            'Gadolinium': form('64', 'Gd', '157.25', 'Lanthanoids', '1313', '3250', '7901', 'Silver', '233'),
            'Terbium': form('65', 'Tb', '158.93', 'Lanthanoids', '1356', '3230', '8219', 'Silver', '225'),
            'Dysprosium': form('66', 'Dy', '162.5', 'Lanthanoids', '1412', '2567', '8551', 'Silver', '228'),
            'Holmium': form('67', 'Ho', '164.93', 'Lanthanoids', '1474', '2700', '8795', 'Silver', '226'),
            'Erbium': form('68', 'Er', '167.26', 'Lanthanoids', '1497', '2868', '9066', 'Silver', '226'),
            'Thulium': form('69', 'Tm', '168.93', 'Lanthanoids', '1545', '1950', '9320', 'Silver', '222'),
            'Ytterbium': form('70', 'Yb', '173.05', 'Lanthanoids', '818.9', '1196', '6570', 'Silver', '222'),
            'Lutetium': form('71', 'Lu', '174.97', 'Lanthanoids', '1663', '3402', '9841', 'Silver', '217'),
            'Hafnium': form('72  ', 'Hf', '178.49', 'Transition Metals', '2233', '4603', '13310', 'Gray', '208'),
            'Tantalum': form('73', 'Ta', '180.95', 'Transition Metals', '3017', '5458', '16650', 'Gray', '200'),
            'Tungsten': form('74', 'W', '183.84', 'Transition Metals', '3422', '5555', '19250', 'Gray', '193'),
            'Rhenium': form('75', 'Re', '186.21', 'Transition Metals', '3186', '5596', '21020', 'Gray', '188'),
            'Osmium': form('76', 'Os', '190.23', 'Transition Metals', '3033', '5012', '22590', 'Bluish-White', '185'),
            'Iridium': form('77', 'Ir', '192.217', 'Transition Metals', '2466', '4428', '22560', 'Silvery-White',
                            '180'),
            'Platium': form('78', 'Pt', '195.084', 'Transition Metals', '1768.3', '3825', '21450', 'Silverish-White',
                            '177'),
            'Gold': form('79', 'Au', '196.977', 'Transition Metals', '1064.18', '2856', '19300', 'Yellow', '174'),
            'Mercury': form('80', 'Hg', '200.59', 'Transition Metals', '-38.83', '356.73', '13534', 'Silver', '171'),
            'Thallium': form('81', 'TI', '204.38', 'Post Transition Metals', '304', '1473', '11850', 'Gray', '156'),
            'Lead': form('82', 'Pb', '207.2', 'Post Transition Metals', '327.46', '1749', '11340',
                         'Silver-Hint of Blue', '154'),
            'Bismuth': form('83', 'Bi', '208.980', 'Post Transition Metals', '271.3', '1564', '9780', 'Silvery-White',
                            '143'),
            'Polonium': form('84', 'Po', '209', 'Post Transition Metals', '255', '961.9', '9196', 'Silver', '135'),
            'Astatine': form('85', 'At', '210', 'Metalloids', '302', '350', 'None', 'Silver', '127'),
            'Radon': form('86', 'Rn', '222', 'Noble Gases', '-71.1', '-68.85', '9.73', 'Colorless ', '120'),
            'Francium': form('87', 'Fr', '223', ' Alkali Metals', '20.9', '650', 'None', 'Silver-Gray-Metallic',
                             'None'),
            'Radium': form('88', 'Ra', '226', ' Alkaline Earth Metal', '700', '1737', '5000', 'Silver-WHite', 'None'),
            'Actinium': form('89', 'Ac', '227', 'Actinoids', '1050', '3200', '10070', 'Silver-White', 'None'),
            'Thorium': form('90', 'Th', '232.038', 'Actinoids', '1750', '4820', '11724', 'Silver', 'None'),
            'Protactinium': form('91', 'Pa', '231.036', 'Actinoids', '1572', '4000', '15370', 'Silver-Gray', 'None'),
            'Uranium': form('92', 'U', '238.029', 'Actinoids', '1135', '3900', '19050', 'Silver-Gray', 'None'),
            }

window = tk.Tk()
window.title('The Periodic Database')

label = tk.Label(text="What Element do you want to look at?")
label.pack()
Elementneeded = tk.Entry(width=50)
Elementneeded.pack()
Text_box = tk.Text()
Text_box.pack()


def Clearbox():
    Text_box.delete('1.0', 'end')
    Elementneeded.delete(0, 'end')
    Stringvar.set('None')


Clear = tk.Button(text="Clear", command=Clearbox)
Clear.pack()
Num = 0


def Next(self):
    global Num
    global Stringvar
    Num = list(Elements).index(Elementneeded.get())
    if Num == length:
        Num = 0
        Index = list(Elements.keys())[Num]
        Elementneeded.delete(0, 'end')
        Elementneeded.insert(0, Index)
        Newindex = Elements[Index]
        Text_box.delete('1.0', 'end')
        Text_box.insert('1.0', Newindex)
        Stringvar.set(Elementneeded.get())
    else:
        Num = Num + 1
        Index = list(Elements.keys())[Num]
        Elementneeded.delete(0, 'end')
        Elementneeded.insert(0, Index)
        Newindex = Elements[Index]
        Text_box.delete('1.0', 'end')
        Text_box.insert('1.0', Newindex)
        Stringvar.set(Elementneeded.get())


def Back(self):
    global Stringvar
    global Num
    Num = list(Elements).index(Elementneeded.get())
    if Num == 0:
        Num = length
        Index = list(Elements.keys())[Num]
        Elementneeded.delete(0, 'end')
        Elementneeded.insert(0, Index)
        Newindex = Elements[Index]
        Text_box.delete('1.0', 'end')
        Text_box.insert('1.0', Newindex)
        Stringvar.set(Elementneeded.get())
    else:

        Num = Num - 1
        Index = list(Elements.keys())[Num]
        Elementneeded.delete(0, 'end')
        Elementneeded.insert(0, Index)
        Newindex = Elements[Index]
        Text_box.delete('1.0', 'end')
        Text_box.insert('1.0', Newindex)
        Stringvar.set(Elementneeded.get())
        
lis = []
for x in range(0, length):
    i = list(Elements.keys())[x]
    lis.append(i)


def callback(selection):
    Text_box.delete('1.0', 'end')
    Text_box.insert('1.0', Elements[selection])
    Elementneeded.delete(0, 'end')
    Elementneeded.insert(0, selection)


Stringvar = tk.StringVar(window, 'None')
Dropdown = tk.OptionMenu(window, Stringvar, *lis, command=callback)
Dropdown.pack()


def Search(self):
    global Stringvar
    text = Elementneeded.get()
    Text_box.delete('1.0', 'end')
    try:
        Text_box.insert('1.0', Elements[text])
        Stringvar.set(Elementneeded.get())def Next(self):
    global Num
    global Stringvar
    Num = list(Elements).index(Elementneeded.get())
    if Num == length:
        Num = 0
        Index = list(Elements.keys())[Num]
        Elementneeded.delete(0, 'end')
        Elementneeded.insert(0, Index)
        Newindex = Elements[Index]
        Text_box.delete('1.0', 'end')
        Text_box.insert('1.0', Newindex)
        Stringvar.set(Elementneeded.get())
    else:
        Num = Num + 1
        Index = list(Elements.keys())[Num]
        Elementneeded.delete(0, 'end')
        Elementneeded.insert(0, Index)
        Newindex = Elements[Index]
        Text_box.delete('1.0', 'end')
        Text_box.insert('1.0', Newindex)
        Stringvar.set(Elementneeded.get())


def Back(self):
    global Stringvar
    global Num
    Num = list(Elements).index(Elementneeded.get())
    if Num == 0:
        Num = length
        Index = list(Elements.keys())[Num]
        Elementneeded.delete(0, 'end')
        Elementneeded.insert(0, Index)
        Newindex = Elements[Index]
        Text_box.delete('1.0', 'end')
        Text_box.insert('1.0', Newindex)
        Stringvar.set(Elementneeded.get())
    else:

        Num = Num - 1
        Index = list(Elements.keys())[Num]
        Elementneeded.delete(0, 'end')
        Elementneeded.insert(0, Index)
        Newindex = Elements[Index]
        Text_box.delete('1.0', 'end')
        Text_box.insert('1.0', Newindex)
        Stringvar.set(Elementneeded.get())


lis = []
for x in range(0, length):
    i = list(Elements.keys())[x]
    lis.append(i)


def callback(selection):
    Text_box.delete('1.0', 'end')
    Text_box.insert('1.0', Elements[selection])
    Elementneeded.delete(0, 'end')
    Elementneeded.insert(0, selection)


Stringvar = tk.StringVar(window, 'None')
Dropdown = tk.OptionMenu(window, Stringvar, *lis, command=callback)
Dropdown.pack()


def Search(self):
    global Stringvar
    text = Elementneeded.get()
    Text_box.delete('1.0', 'end')
    try:
        Text_box.insert('1.0', Elements[text])
        Stringvar.set(Elementneeded.get())
    except:
        Text_box.insert('1.0', 'That is not an element')

    except:
        Text_box.insert('1.0', 'That is not an element')


# Binds
window.bind('<Right>', Next)
window.bind('<Left>', Back)
window.bind('<Return>', Search)

window.mainloop()
