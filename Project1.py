#Author- Samiya Bhogal
#Description- Giving a beam or channel number and then drawing sketch in fusion according to specifications

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        


    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
