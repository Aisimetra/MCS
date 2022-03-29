import PySimpleGUI as sg #da installare se mancante

def interface_def():
    sg.theme('LightGrey1')   # Add a touch of color
    # All the stuff inside your window.
    layout =    [[sg.Text('Selezionare un\'immagine Bitmap',font=('Any')), sg.In(key='-L-',font=('Any')), sg.FileBrowse('FileBrowse',font=('Any'))],
                # un intero F che sar`a l’ampiezza della finestra in cui si effettuera` la DCT2
                [sg.Text('Selezionare l\'ampiezza della finestra (F)',font=('Any')), sg.In(key='-F-',font=('Any'))],  
                # un intero d compreso tra 0 e (2F −2) che sara` la soglia di taglio delle frequenze
                [sg.Text('Selezionare la soglia di taglio delle frequenze (d)',font=('Any')), sg.In(key='-d-',font=('Any'))],     
                [sg.Text('(tra 0 e 2F-2)',font=('Any'))] ,               
                [sg.Submit(font=('Any')), sg.Cancel(font=('Any'))],
    ]


    window = sg.Window('Window Title', layout)    


    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break    
        if((values['-F-']).lstrip('-+').isdigit() == False):
            sg.popup('F deve essere un numero',font=('Any'))
        elif( int(values['-F-']) <= 0):
            sg.popup('F deve essere un intero positivo',font=('Any'))    
        elif((values['-d-']).lstrip('-+').isdigit() == False):
            sg.popup('d deve essere un numero',font=('Any'))       
        else:
            F_input = int(values['-F-'])
            d_input = int(values['-d-'])

            if (d_input< 0 or d_input > (2*F_input -2)):
                sg.popup('Il valore di d deve essere compreso tra 0 e 2F-2',font=('Any'))
            else:
                break

        
    returns = [F_input, d_input,values['-L-']];            
    window.close()
    return(returns)

# è necessario inserire il resize della finestra successiva quando F viene passato
# bisogna anche inserire la seconda schermata con la soluzione