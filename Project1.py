#Author- Samiya Bhogal
#Description- Choosing a beam or channel and then drawing sketch according to specifications

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        


    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
