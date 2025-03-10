from nicegui import ui

with ui.grid(columns=2):
    ui.label('Name: Sandi')
    ui.label('Name: Maureen')

    ui.label('Age: 30')
    ui.label('Age: 27')

    ui.label('Height: 1.97 Cm')
    ui.label('Height: 1.65 Cm')

    ui.label('Weight: 100 Kg')
    ui.label('Weight: 60 Kg')

ui.run()