import PySimpleGUI as sg




# bereken aantal mewters, voor aanta; vdps, wikkel

def main():
    layout = [
        # [sg.Text("VDP"), sg.Checkbox('nummers', default=True), sg.Checkbox('beelden')],

        [sg.Text('ordergegevens voor verwerken VDP', text_color="Yellow")],
        [sg.Text('Ordernummer', size=(15, 1)), sg.InputText(key="order_number")],

        [sg.Text("VDP map voor csv's")],
        [sg.In(key='folder_voor_vdp_map')], [sg.FolderBrowse(target="folder_voor_vdp_map")],
        # [sg.Text("Choose a file: "), sg.FileBrowse()],
        # [sg.Text()],
        # [sg.CalendarButton("Datum")],
        # [sg.Text()],

        [sg.Text('Totaal aantal', size=(15, 1)), sg.Input(key="totaal_aantal")],
        [sg.Text('Aantal_per_rol', size=(15, 1)), sg.InputText(key='aantal_per_rol')],
        [sg.Text('Kern', size=(15, 1)), sg.InputText(76,key='aantal_per_rol')],
        # [sg.Text('Beginnummer', size=(15, 1)), sg.InputText(key="begin_nummer")],
        # [sg.Text('posities', size=(15, 1)), sg.InputText(key="posities")],
        [sg.Text('aantal VDP,s', size=(15, 1)), sg.InputText(1,key="posities",)],
        # [sg.Listbox(values=['Listbox 1', 'Listbox 2', 'Listbox 3'], size=(30, 6))],
        # [sg.Text('voorloop getal', size=(15, 1)), sg.InputText(key="vlg0")],
        # [sg.Text('Kern')],[sg.Listbox(key="kern",values=[76,40,25], size=(10, 3))],
        # [sg.Text('Kern')],[sg.Combo(key="kern",values=[76,40,25], size=(10, 3))],



        [sg.Text('x', size=(15, 1)), sg.InputText(key='mes')],
        [sg.Text('y', size=(15, 1)), sg.InputText(3,key='y')],
        [sg.Text('X_Waarde', size=(15, 1)), sg.InputText(3,key='x_waarde')],
        [sg.Text('Y_waarde', size=(15, 1)), sg.InputText(3,key="y_waarde")],
        [sg.Text('breedte etiket', size=(15, 1)), sg.InputText(1,key="breedte")],
        [sg.Text('hoogte etiket', size=(15, 1)), sg.InputText(1,key="hoogte")],

        # [sg.Text('Wikkel', size=(15, 1)), sg.InputText(key="wikkel")],# formule

        # [sg.Text('prefix', size=(15, 1)), sg.InputText(key="prefix")],
        # [sg.Text('postfix', size=(15, 1)), sg.InputText(key="postfix")],


        [sg.Button("Ok"), sg.Cancel()],
    ]

    window = sg.Window('Demo window..', layout)
    i = 0
    while True:
        event, values = window.read(timeout=1)
        if event != sg.TIMEOUT_KEY:
            print(event, values)
        if event is None:
            break
        i += 1
    window.close()

main()
print('Program terminating normally')