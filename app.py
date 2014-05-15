# app.py by jared musil
# various tools for use within the iowa water science center
# tested with Python 3.3 and Tkinter 8.5

__version__ = '0.6'

import os
import shutil
import subprocess
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename


class Application:
    def __init__(self, root):
        self.root = root
        self.root.title('Data Toolbox')
        self.root.iconbitmap(os.path.dirname(os.path.abspath(__file__)) + '\\logo.ico')

        # variables
        self.appRoot = os.path.dirname(os.path.abspath(__file__))
        self.widthProcessBtn  = 130
        self.widthProcessIcon = 27
        # images
        self.imgAdd     = tk.PhotoImage(data='R0lGODlhEAAQALMKAABy/5bG4ZDG5pLI247E9JXH2ZbF4ZDH5o7B/5LI3P///wAAAAAAAAAAAAAAAAAAACH5BAEAAAoALAAAAAAQABAAAAQ0UMlJq71Ygg3yBEHQeQookmWAjBa3EYTLpkJtH+FsDjyf5BRZoSDDAAwnkmlmBCo5qGg0AgA7')
        self.imgRun     = tk.PhotoImage(data='R0lGODlhEAAQAMZSADNIYzNIZDRJYzVKZTdMZjhNZzlNaDlOaDxQazxRaz5SbD5SbUJWb0RYcipbvUdadEpdd0teeExeeE5helBifFFkfVRmf1RngFlrhFtuhlxuh2BxiWFzi2R1jWV3jmZ4kGd5kEN+9Gt9k21/lm+Al1GD5XOEmneHnn+PpF6T/NTe9dXf9tbh9tji99rj9tzk99zl993m997n99/n+OHn+OLp+OPp+ePr+eXr+eXr+ubs+ebs+ubt+uju+eju+urv+uvv+uvw+uzx++3y++7y++7z++/z+/Dz/PD0/PH1/PL2/PP2/fT3/fX3/fX4/ff5/fn7/vv8/v///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////yH5BAEKAH8ALAAAAAAQABAAAAeXgH+Cg4SFhCWHiYaLi4iDjoKQkYqTkSkpIQ4ll5mbmA6RmaGgfyWig6SCqX+pJyYkIiAdGxoYFxUTEA8NfyNSv8DBv0wKfx5RKFAfTxRNCUoARwBDBX8ZTkxLSUhGREJAPz48OQF/FkUcQRE9BjoANgAzADAAfxI7ODc1NDIxLy4tWKxQUa8BgwUIDhAYIACAw4f1GC0KBAA7')
        self.imgOpen    = tk.PhotoImage(data='R0lGODlhEAAQAOMJAICAAJ+fP///n19fP5+ff9+/P7+fP//fn19fX////////////////////////////yH5BAEKAA8ALAAAAAAQABAAAARE8MlJq70WaIAnOsJxIB0AnsemBRMQvudLSiZspy087Hw/1IdBYUgcGkiuYLF4pCmXxtkDMDBYr1fpg4Doer+dsHgsjgAAOw==')
        self.imgOkay    = tk.PhotoImage(data='R0lGODlhEAAQAIABAB4eHQAAACH5BAEAAAEALAAAAAAQABAAAAIjjI+pG8AK3DtRzmotwlk3TkUhtlUfWXJmoq6QeqGx99DTVAAAOw==')
        self.imgIAWSC   = tk.PhotoImage(data='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')
        self.imgReset   = tk.PhotoImage(data='R0lGODlhEAAQAOMJAAAAALAwF39ZBo1jBpVyHdGUDNusN+K7Uu7WgP///////////////////////////yH5BAEKAA8ALAAAAAAQABAAAARF8ElAq6XyAYK6/wIwIUZhnmYpakgRXEDQrsCcZXVB2zerj79ebhe8DSszDM5WaxWBxJWRp5FaZM+p55DFoQoDqRDWK5cjADs=')
        self.imgDelete  = tk.PhotoImage(data='R0lGODlhEAAQAOcAAP///8opAJMAAPb4+v/M/4SQnfr7/Pj5+/z9/f7+/vT2+Ss2QvH1+P9MDP8zAP8pAOnu9O3y9uXs8u/z9+vw9f+DIJSfq/9sFHJ+ivr7/ff5+4+PyGBpc/n7/GNsd1dfaIGOmkpUX3aBjX6KlvP2+e7y9/n6+3B7h2Zveuzx9oSRnfH09v3+/2hyfVBZYW14hJKRy/7///j6/I6Ox//+/mBoc52evoSRnrjBx2t1gHuHk3mEkOXr8dPY3oiUn4mVoerv9Ss3QlRcZoCKlvD1+Kissejt84iUof///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////yH5BAEKAH8ALAAAAAAQABAAAAjRAH/cKECwoAofFv4oVAgCgMOHDmEASLhwBIAEGDMCmOGQ4h8dABCIHAlgw0OKOwAYWMkyhg0XQj4MUSgCwIGbOE2wWNEDxxGFGAAMGEp0qAYZADAoPAGAhIKnTzM4lApA4QsARBhoZdCBRoAADr/+yQGgxISzEwAEIEDgK9sALQCkiEA3AgABFSqwzSsABQAgFAJT0HD3guELAv54AGAEgmMIA9Q2mNwgwB8OAHhI2CxBLYEHDhw8aFsD4kMBoAUIEC0gRJAFsGEXuSvAoeo/AQEAOw==')
        self.imgOutput  = tk.PhotoImage(data='R0lGODlhEAAQAKUqAABCZQFGagBHbgBLcwBMcwFMdAFQeT9DRgBSewJSeAJXgQBZhANagklNTwJdiQBfiwNijwNmlAVsmwdwoV5hZAl0pmlsb25xc06LrVOOsGCdvKnV+KfY+rPa+Krf+b3f98Lh+crl+dHo+tfq+9zs++Hw/OXy/Ofz/e32/fD4/f///////////////////////////////////////////////////////////////////////////////////////yH5BAEKAD8ALAAAAAAQABAAAAaNwJ/wV6kMf5ekcjhJTY7QoQQlklivP4vW8oucQKCTWByBPkqdtDr9+FHelN9iQ6/TF9EfgsNB+P8/DYINQwQeBHl5AgJHB46PQhGSDJKVlJM/EBomJhoQJhCfn5wQPw4kDqcOI6msqw4JPwohCrO2t7RCARghIRgBGb0ZAQYfBkMAAwMAPwAFy83QiYlBADs=')
        self.imgRecover = tk.PhotoImage(data='R0lGODlhEAAQALMAAP9jAP8AAM4AAL0AAP///87OznNzcwAAAP///wAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAAgALAAAAAAQABAAAARaEEl5qp0YVQI6IFV2EGRgBmRxTGMqDC9JGKuW0pas2kRBYy1fBRAQ1IBE44E4OLKYw6KTkow2Mxpoi+QM/ragXKp2KMg8n96PYigUTgH3mnUwwGA4LMUSwkQAADs=')
        # colors
        self.ncsRed    = '#C40233'
        self.ncsBlue   = '#0087BD'
        self.ncsGreen  = '#009F6B'
        self.ncsYellow = '#FFD300'
        # styles
        style = ttk.Style()
        style.configure('bgRed.TLabel', background=self.ncsRed)
        style.configure('bgGreen.TLabel', background=self.ncsGreen)
        style.configure('bgYellow.TLabel', background=self.ncsYellow)

        # construct gui
        self.init_widgets()

    def init_widgets(self):
        # root window resizing
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # add tabs
        self.nb = ttk.Notebook(root)
        self.nb.grid(row=0, column=0, sticky=tk.NSEW)
        self.tab_help()
        self.tab_efc()
        self.tab_gwflow()
        self.tab_makeplot()
        self.tab_about()

    def tab_help(self):
        self.tab_help = tk.Frame()
        tab = self.tab_help
        self.nb.add(tab, text='Help')

        # tab window resizing
        # - The process frame can only resize vertically
        # - The help frame can resize in both directions
        tab.grid_rowconfigure(0, weight=1)
        tab.grid_columnconfigure(0, weight=1)

        # frames
        tab.help = ttk.Frame(tab)
        tab.help.grid( row=0, column=0, sticky=tk.NSEW, padx=5, pady=5)

        # frame widgets
        tab.help.text = tk.Text(tab.help, padx=5, pady=5, relief=tk.FLAT)
        tab.help.sb   = ttk.Scrollbar(tab.help, command=tab.help.text.yview, orient='vertical')

        # frame widget placement
        tab.help.text.grid( row=0, column=0, sticky=tk.NSEW)
        tab.help.sb.grid(   row=0, column=1, sticky=tk.NS)

        # frame widget window resizing
        # - the text widget will fill its containter in both directions
        tab.help.grid_columnconfigure(0, weight=1)
        tab.help.grid_rowconfigure(0, weight=1)

        efc = (
        'EFC Tab\n'
        'Environmental Flow Components tab will create a set of flow '
        'observation related files for the purpose of calibration within the '
        'LUCA calibration tool. The file most commonly used from this tab '
        'will be the HIGH6.LOW7 file. LUCA will use this file to examine only '
        'observed and simulated flow values at either the HIGH or LOW flow '
        'regime, and calibrate related HIGH or LOW flow parameters to those '
        'flow regimes.\n\n')
        
        gwflow = (
        'Gwflow Tab\n'
        'The gwflow tab will create PRMS groundwater flow parameters for '
        'gwflow_coef and gwstor_init. A mean, min, and max value for '
        'gwflow_coef, and gwstor_init will be created for each streamflow '
        'gage. The mean values can be used as starting values for HRUs '
        'upstream of the runoff(streamflow gage) site, and the min/max can be '
        'used for calibration bounds in LUCA.\n\n')
        
        makeplot = (
        'MakePlot Tab\n'
        'Makeplot is used to plot the latest PRMS model simulations and '
        'examine observed and simulated data and how well they are matching. '
        'The plot has six graphics, 1.solar, 2.PET, Streamflow, simulate '
        'versus observed (3.Monthly, 4.Annual), and Nash-Sutcliffe statistics '
        'for fit (5.annually, and 6.all years). This plot is a simple way to '
        'examine how well PRMS is fitting Solar, PET and water budgets to '
        'observed data.')
        

        # frame widget initial data population
        tab.help.text['yscrollcommand'] = tab.help.sb.set
        tab.help.text.insert(tk.INSERT, efc)
        tab.help.text.insert(tk.INSERT, gwflow)
        tab.help.text.insert(tk.INSERT, makeplot)

    def tab_efc(self):
        self.tab_efc = tk.Frame()
        tab = self.tab_efc
        self.nb.add(tab, text='Efc')

        # tab variables
        tab.filename = tk.StringVar()
        tab.filepath = tk.StringVar()
        instructions = ("Before starting, please check that the data file:\n"
        " 1. Is a downsizer file with ONLY runoff(streamflow gages) values.\n"
        " 2. Has had a global search and replace of all TABS replaced with SPACES.")

        # tab window resizing
        # - The process frame can only resize vertically
        # - The log frame can resize in both directions
        tab.grid_rowconfigure(1, weight=1)
        tab.grid_columnconfigure(0, weight=0, minsize=162)
        tab.grid_columnconfigure(1, weight=1)

        # frames
        tab.info    = ttk.LabelFrame(tab, text='Instructions')
        tab.process = ttk.Frame(tab)
        tab.log     = ttk.Frame(tab)
        tab.info.grid(    row=0, column=0, columnspan=2, sticky=tk.NSEW, padx=5, pady=5)
        tab.process.grid( row=1, column=0, sticky=tk.NSEW, padx=5, pady=5)
        tab.log.grid(     row=1, column=1, sticky=tk.NSEW, padx=(0,5), pady=5)

        # frame widgets
        tab.info.txt             = ttk.Label(tab.info, text=instructions)
        tab.process.loadFileBtn  = ttk.Button(tab.process, command=lambda:self.load_file(tab), text='Load Data')
        tab.process.loadFileIcon = ttk.Label(tab.process, image=self.imgOpen, anchor=tk.CENTER)
        tab.process.saveBtn      = ttk.Button(tab.process, command=lambda:self.run_efc(tab), text='Process & Save')
        tab.process.saveIcon     = ttk.Label(tab.process, image=self.imgRun, anchor=tk.CENTER)
        tab.process.spacerLabel  = ttk.Label(tab.process, text=' ')
        tab.process.resetBtn     = ttk.Button(tab.process, command=lambda:self.open_directory(tab, 'efc'), text='Open Output Folder')
        tab.process.resetIcon    = ttk.Label(tab.process, image=self.imgOutput, anchor=tk.CENTER)
        tab.log.text             = tk.Text(tab.log, width=60, height=15, padx=5, pady=5, relief=tk.FLAT)
        tab.log.sb               = ttk.Scrollbar(tab.log, command=tab.log.text.yview, orient='vertical')

        # frame widget placement
        tab.info.txt.grid( row=0, column=0, sticky=tk.NSEW)
        tab.process.loadFileBtn.grid(  row=0, column=0, sticky=tk.EW)
        tab.process.loadFileIcon.grid( row=0, column=1, sticky=tk.NSEW)
        tab.process.saveBtn.grid(      row=1, column=0, sticky=tk.EW)
        tab.process.saveIcon.grid(     row=1, column=1, sticky=tk.NSEW)
        tab.process.spacerLabel.grid(  row=2, column=0, sticky=tk.EW)
        tab.process.resetBtn.grid(     row=3, column=0, sticky=tk.EW)
        tab.process.resetIcon.grid(    row=3, column=1, sticky=tk.NSEW)
        tab.log.text.grid( row=0, column=0, sticky=tk.NSEW)
        tab.log.sb.grid(   row=0, column=1, sticky=tk.NS)

        # frame widget window resizing
        # - the text widget will fill its containter in both directions
        tab.log.grid_columnconfigure(0, weight=1)
        tab.log.grid_rowconfigure(0, weight=1)
        # - push 'recover input' button to bottom of process frame using spacer
        tab.process.grid_rowconfigure(2, weight=1)
        # - strech process frame columns to be the same width as other tabs
        tab.process.grid_columnconfigure(0, weight=0, minsize=self.widthProcessBtn)
        tab.process.grid_columnconfigure(1, weight=0, minsize=self.widthProcessIcon)


        # frame widget initial data population
        tab.log.text['yscrollcommand'] = tab.log.sb.set
        tab.log.text.insert(tk.INSERT, '\u2190 Start here\n\n')

    def tab_gwflow(self):
        self.tab_gwflow = tk.Frame()
        tab = self.tab_gwflow
        self.nb.add(tab, text='Gwflow')

        # tab window resizing
        # - the process frame can only resize vertically
        # - the log frame can resize in both directions
        tab.grid_rowconfigure(1, weight=1)
        tab.grid_columnconfigure(0, weight=0)
        tab.grid_columnconfigure(1, weight=1)

        # tab variables
        tab.filename  = tk.StringVar()
        tab.filepath  = tk.StringVar()
        tab.runoffNum = tk.IntVar()
        tab.runoffNum.set('#')
        instructions = ("Before starting, please check that the data file:\n"
        " 1. Is a downsizer file with ONLY runoff(streamflow gages) values.\n"
        " 2. Has had a global search and replace of all TABS replaced with SPACES.")

        # frames
        tab.info    = ttk.LabelFrame(tab, text='Instructions')
        tab.process = ttk.Frame(tab)
        tab.log     = ttk.Frame(tab)
        tab.info.grid(    row=0, column=0, columnspan=2, sticky=tk.NSEW, padx=5, pady=5)
        tab.process.grid( row=1, column=0, sticky=tk.NSEW, padx=5, pady=5)
        tab.log.grid(     row=1, column=1, sticky=tk.NSEW, padx=(0,5), pady=5)

        # frame widgets
        tab.info.txt = ttk.Label(tab.info, text=instructions)
        tab.process.loadFileBtn  = ttk.Button(tab.process, command=lambda:self.load_file(tab), text='Load Data')
        tab.process.loadFileIcon = ttk.Label(tab.process, image=self.imgOpen, anchor=tk.CENTER)
        tab.process.runoffLabel  = ttk.Label(tab.process, text='How many runoff sites?')
        tab.process.runoffEntry  = ttk.Entry(tab.process, textvariable=tab.runoffNum)
        tab.process.runoffBtn    = ttk.Button(tab.process, command=lambda:self.add_runoff(tab), image=self.imgAdd)
        tab.process.drainage     = ttk.Frame(tab.process)
        tab.process.saveBtn      = ttk.Button(tab.process, command=lambda:self.run_gwflow(tab), text='Process & Save')
        tab.process.saveIcon     = ttk.Label(tab.process, image=self.imgRun, anchor=tk.CENTER)
        tab.process.spacerLabel  = ttk.Label(tab.process, text=' ')
        tab.process.resetBtn     = ttk.Button(tab.process, command=lambda:self.open_directory(tab, 'gwflow'), text='Open Output Folder')
        tab.process.resetIcon    = ttk.Label(tab.process, image=self.imgOutput, anchor=tk.CENTER)
        tab.log.text             = tk.Text(tab.log, width=60, height=15, padx=5, pady=5, relief=tk.FLAT)
        tab.log.sb               = ttk.Scrollbar(tab.log, command=tab.log.text.yview, orient='vertical')

        # frame widget placement
        tab.info.txt.grid(             row=0, column=0, sticky=tk.NSEW)
        tab.process.loadFileBtn.grid(  row=0, column=0, sticky=tk.EW)
        tab.process.loadFileIcon.grid( row=0, column=1, sticky=tk.NSEW)
        tab.process.runoffLabel.grid(  row=1, column=0, columnspan=2, sticky=tk.EW)
        tab.process.runoffEntry.grid(  row=2, column=0, sticky=tk.EW, ipady=1)
        tab.process.runoffBtn.grid(    row=2, column=1, sticky=tk.EW)
        tab.process.drainage.grid(     row=3, column=0, columnspan=2, sticky=tk.EW)
        tab.process.saveBtn.grid(      row=4, column=0, sticky=tk.EW)
        tab.process.saveIcon.grid(     row=4, column=1, sticky=tk.NSEW)
        tab.process.spacerLabel.grid(  row=5, column=0, sticky=tk.EW)
        tab.process.resetBtn.grid(   row=6, column=0, sticky=tk.EW)
        tab.process.resetIcon.grid(  row=6, column=1, sticky=tk.NSEW)
        tab.log.text.grid(             row=0, column=0, sticky=tk.NSEW)
        tab.log.sb.grid(               row=0, column=1, sticky=tk.NSEW)

        #frame widget event binding
        #tab.process.runoffBtn.bind("<Return>",self.add_runoff(tab))

        # frame widget window resizing
        # - the text widget will fill its containter in both directions
        tab.log.grid_columnconfigure(0, weight=1)
        tab.log.grid_rowconfigure(0, weight=1)
        # - push 'recover input' button to bottom of process frame using spacer
        tab.process.grid_rowconfigure(5, weight=1)
        # - strech process frame columns to be the same width as other tabs
        tab.process.grid_columnconfigure(0, weight=0, minsize=self.widthProcessBtn)
        tab.process.grid_columnconfigure(1, weight=0, minsize=self.widthProcessIcon)

        # frame widget initial data population
        tab.log.text['yscrollcommand'] = tab.log.sb.set
        tab.log.text.insert(tk.INSERT, '\u2190 Start here\n\n')

    def tab_makeplot(self):
        self.tab_plot = tk.Frame()
        tab = self.tab_plot
        self.nb.add(tab, text='MakePlot')

        # tab variables
        tab.filename   = tk.StringVar()
        tab.filenameSr = tk.StringVar()
        tab.filenamePe = tk.StringVar()
        tab.filepath   = tk.StringVar()
        tab.filepathSr = tk.StringVar()
        tab.filepathPe = tk.StringVar()
        tab.simSr      = tk.StringVar()
        tab.simPet     = tk.StringVar()
        tab.obsRunoff  = tk.StringVar()
        tab.simRunoff  = tk.StringVar()
        tab.startYear  = tk.StringVar()
        tab.endYear    = tk.StringVar()
        tab.simSr.set('#')
        tab.simPet.set('#')
        tab.obsRunoff.set('#')
        tab.simRunoff.set('#')
        tab.startYear.set('####')
        tab.endYear.set('####')
        instructions = ("Makeplots requires three input files. A statvar file from PRMS, and PE and SR monthly observed data files (user created see the example files).\n"
        "The SR and PE file should be placed in the input sub folder. The statvar file needs to contain at least the simulated SR, PE, observed flow,\n"
        "and simulated flow. You will need to enter the proper location of each of these output variables so that makeplot can run properly.\n"
        "All plots are by water year, your statvar must have data that covers the water years you would like plotted.")

        # tab window resizing
        # - The process frame can only resize vertically
        # - The log frame can resize in both directions
        tab.grid_rowconfigure(1, weight=1)
        tab.grid_columnconfigure(0, weight=0, minsize=162)
        tab.grid_columnconfigure(1, weight=1)

        # frames
        tab.info    = ttk.LabelFrame(tab, text='Instructions')
        tab.process = ttk.Frame(tab)
        tab.log     = ttk.Frame(tab)
        tab.info.grid(    row=0, column=0, columnspan=2, sticky=tk.NSEW, padx=5, pady=5)
        tab.process.grid( row=1, column=0, sticky=tk.NSEW, padx=5, pady=5)
        tab.log.grid(     row=1, column=1, sticky=tk.NSEW, padx=(0,5), pady=5)

        # frame widgets
        tab.info.txt               = ttk.Label(tab.info, text=instructions)
        tab.process.loadFileBtn    = ttk.Button(tab.process, command=lambda:self.load_statvar(tab), text='Load StatVar')
        tab.process.loadFileIcon   = ttk.Label(tab.process, image=self.imgOpen, anchor=tk.CENTER)
        tab.process.loadSrBtn      = ttk.Button(tab.process, command=lambda:self.load_sr(tab), text='Load SR')
        tab.process.loadSrIcon     = ttk.Label(tab.process, image=self.imgOpen, anchor=tk.CENTER)
        tab.process.loadPeBtn      = ttk.Button(tab.process, command=lambda:self.load_pe(tab), text='Load PE')
        tab.process.loadPeIcon     = ttk.Label(tab.process, image=self.imgOpen, anchor=tk.CENTER)
        tab.process.simSrLabel     = ttk.Label(tab.process, text='Simulated SR')
        tab.process.simSrEntry     = ttk.Entry(tab.process, textvariable=tab.simSr)
        tab.process.simPetLabel    = ttk.Label(tab.process, text='Simulated PET')
        tab.process.simPetEntry    = ttk.Entry(tab.process, textvariable=tab.simPet)
        tab.process.obsRunoffLabel = ttk.Label(tab.process, text='Observed Runoff')
        tab.process.obsRunoffEntry = ttk.Entry(tab.process, textvariable=tab.obsRunoff)
        tab.process.simRunoffLabel = ttk.Label(tab.process, text='Simulated Runoff')
        tab.process.simRunoffEntry = ttk.Entry(tab.process, textvariable=tab.simRunoff)
        tab.process.startYearLabel = ttk.Label(tab.process, text='Start Water Year')
        tab.process.startYearEntry = ttk.Entry(tab.process, textvariable=tab.startYear)
        tab.process.endYearLabel   = ttk.Label(tab.process, text='End Water Year')
        tab.process.endYearEntry   = ttk.Entry(tab.process, textvariable=tab.endYear)
        tab.process.makeplotBtn    = ttk.Button(tab.process, command=lambda:self.run_makeplot(tab), text='Run makeplot.exe')
        tab.process.makeplotIcon   = ttk.Label(tab.process, image=self.imgRun, anchor=tk.CENTER)
        tab.process.spacerLabel    = ttk.Label(tab.process, text=' ')
        tab.process.resetBtn       = ttk.Button(tab.process, command=lambda:self.open_directory(tab, 'makeplot'), text='Open Output Folder')
        tab.process.resetIcon      = ttk.Label(tab.process, image=self.imgOutput, anchor=tk.CENTER)
        tab.log.text               = tk.Text(tab.log, width=60, height=15, padx=5, pady=5, relief=tk.FLAT)
        tab.log.sb                 = ttk.Scrollbar(tab.log, command=tab.log.text.yview, orient='vertical')

        # frame widget placement
        tab.info.txt.grid(               row=0, column=0, sticky=tk.NSEW)
        tab.process.loadFileBtn.grid(    row=0, column=0, sticky=tk.EW)
        tab.process.loadFileIcon.grid(   row=0, column=1, sticky=tk.NSEW)
        tab.process.loadSrBtn.grid(      row=1, column=0, sticky=tk.EW)
        tab.process.loadSrIcon.grid(     row=1, column=1, sticky=tk.NSEW)
        tab.process.loadPeBtn.grid(      row=2, column=0, sticky=tk.EW)
        tab.process.loadPeIcon.grid(     row=2, column=1, sticky=tk.NSEW)
        tab.process.simSrLabel.grid(     row=3, column=0, sticky=tk.EW)
        tab.process.simSrEntry.grid(     row=4, column=0, sticky=tk.EW)
        tab.process.simPetLabel.grid(    row=5, column=0, sticky=tk.EW)
        tab.process.simPetEntry.grid(    row=6, column=0, sticky=tk.EW)
        tab.process.obsRunoffLabel.grid( row=7, column=0, sticky=tk.EW)
        tab.process.obsRunoffEntry.grid( row=8, column=0, sticky=tk.EW)
        tab.process.simRunoffLabel.grid( row=9, column=0, sticky=tk.EW)
        tab.process.simRunoffEntry.grid( row=10, column=0, sticky=tk.EW)
        tab.process.startYearLabel.grid( row=11, column=0, sticky=tk.EW)
        tab.process.startYearEntry.grid( row=12, column=0, sticky=tk.EW)
        tab.process.endYearLabel.grid(   row=13, column=0, sticky=tk.EW)
        tab.process.endYearEntry.grid(   row=14, column=0, sticky=tk.EW)
        tab.process.makeplotBtn.grid(    row=15, column=0, sticky=tk.EW)
        tab.process.makeplotIcon.grid(   row=15, column=1, sticky=tk.NSEW)
        tab.process.spacerLabel.grid(    row=16, column=0, sticky=tk.EW)
        tab.process.resetBtn.grid(     row=17, column=0, sticky=tk.EW)
        tab.process.resetIcon.grid(    row=17, column=1, sticky=tk.NSEW)
        tab.log.text.grid(               row=0, column=0, sticky=tk.NSEW)
        tab.log.sb.grid(                 row=0, column=1, sticky=tk.NS)

        # frame widget window resizing
        # - the text widget will fill its containter in both directions
        tab.log.grid_columnconfigure(0, weight=1)
        tab.log.grid_rowconfigure(0, weight=1)
        # - push 'recover input' button to bottom of process frame using spacer
        tab.process.grid_rowconfigure(16, weight=1)
        # - strech process buttons out to the same width as other tabs
        # - strech process frame columns to be the same width as other tabs
        tab.process.grid_columnconfigure(0, weight=0, minsize=self.widthProcessBtn)
        tab.process.grid_columnconfigure(1, weight=0, minsize=self.widthProcessIcon)

        # frame widget initial data population
        tab.log.text['yscrollcommand'] = tab.log.sb.set
        tab.log.text.insert(tk.INSERT, '\u2190 Start here\n\n')

    def tab_about(self):
        self.tab_about = tk.Frame()
        tab = self.tab_about
        self.nb.add(tab, text='...')
        
        # tab window resizing
        # - center the image of iowa
        tab.grid_rowconfigure(0, weight=1)
        tab.grid_columnconfigure(0, weight=1)
        tab.grid_columnconfigure(1, weight=0)
        tab.grid_columnconfigure(2, weight=1)

        # "about" tab info
        tab.about = ttk.Label(tab, text='Data Toolbox\nVersion ' + __version__ + '\n\nFound a bug?\nContact jaredmusil@gmail.com', image=self.imgIAWSC, compound='top', justify=tk.CENTER)
        tab.about.grid(row=0, column=1, sticky=tk.NSEW)
# -----------------------------------------------------------------------------

    def load_file(self, tab):
        # open chose-file dialogue box
        filepath = askopenfilename()

        # only remember the filename itself.
        # split the string by "/" characters & remember the last part/filename
        filename = filepath.split('/')[-1]

        # save location to a tab variable
        tab.filepath.set(filepath)
        tab.filename.set(filename)
            
        # askopenfilename() returns an empty string on cancel
        if filepath != '':     
            
            # change icon from folder to checkmark
            tab.process.loadFileIcon.configure(image=self.imgOkay)

            # visually notify user
            tab.log.text.insert(tk.INSERT, 'File loaded:\n ' + filename + '\n\n')

    def load_sr(self, tab):
        # open chose-file dialogue box
        filepath = askopenfilename()

        # only remember the filename itself.
        # split the string by "/" characters & remember the last part/filename
        filename = filepath.split('/')[-1]

        # save location to a tab variable
        tab.filepathSr.set(filepath)
        tab.filenameSr.set(filename)

        # askopenfilename() returns an empty string on cancel
        if filepath != '':     
            
            # change icon from folder to checkmark
            tab.process.loadSrIcon.configure(image=self.imgOkay)

            # visually notify user
            tab.log.text.insert(tk.INSERT, 'SR File loaded:\n ' + filename + '\n\n')

    def load_pe(self, tab):
        # open chose-file dialogue box
        filepath = askopenfilename()

        # only remember the filename itself.
        # split the string by "/" characters & remember the last part/filename
        filename = filepath.split('/')[-1]

        # save location to a tab variable
        tab.filepathPe.set(filepath)
        tab.filenamePe.set(filename)
            
        # askopenfilename() returns an empty string on cancel
        if filepath != '':     
            
            # change icon from folder to checkmark
            tab.process.loadPeIcon.configure(image=self.imgOkay)

            # visually notify user
            tab.log.text.insert(tk.INSERT, 'PE File loaded:\n ' + filename + '\n\n')

    def load_statvar(self, tab):
        # ask user to find file 
        self.load_file(tab)

        # locate file
        file = tab.filepath.get()

        # load file
        f = open(file, 'r')

        # print header information needed for makeplot configuration
        headers = []
        index = 0
        line = f.readline()
        while file:
            header = line.split()
            # headers at most have a name and value            
            if len(header) > 2:
                break
            else:
                # advance forward
                headers.append(str(index) + ' ' + line)
                line = f.readline()
                index += 1

        # display header information in user log
        tab.log.text.insert(tk.INSERT, '# Statvar_Header:\n')
        tab.log.text.insert(tk.INSERT, '--------------------\n')
        for iHeader in headers:
            tab.log.text.insert(tk.INSERT, iHeader)
        tab.log.text.insert(tk.INSERT, '--------------------\n\n')

    def add_runoff(self, tab):
        num = tab.process.runoffEntry.get()
        if(num.isnumeric()):
            # add drainage label
            tab.process.drainage.label = ttk.Label(tab.process.drainage, text='Drainage area in sq/km?')
            tab.process.drainage.label.grid(row=0, column=0, columnspan=2, sticky=tk.EW)

            # add new data entry inputs
            tab.drainage = []
            for iRow in range(int(num)):
                tab.drainage.append(tk.StringVar())
                entry = ttk.Entry(tab.process.drainage, textvariable=tab.drainage[iRow])
                label = ttk.Label(tab.process.drainage, text=iRow+1, anchor=tk.CENTER)
                # offset the grid by 1 because of the label                
                entry.grid(row=iRow+1, column=0, sticky=tk.EW)
                label.grid(row=iRow+1, column=1, sticky=tk.EW)

            # notify user
            tab.log.text.insert(tk.INSERT, str(num) + ' runoff sites added\n Next please enter drainage area in sq/km\n\n')
        else:
            # complain about non numeric input
            tab.runoffNum.set('#')
            tab.log.text.insert(tk.INSERT, 'Runoff site numbers can only be positive whole numbers.\n')
            tab.log.text.insert(tk.INSERT, 'Computers are rather picky about this.\n\n')

    def open_directory(self, tab, tabname):
        os.chdir(self.appRoot + '\\output\\' + tabname)
        subprocess.Popen(r'explorer .')
        os.chdir(self.appRoot)

    def run_efc(self, tab):
        # copy input file to the same directory as the exe
        iSource = tab.filepath.get()
        iDestination = self.appRoot + '\\exe\\efc\\' + tab.filename.get()
        shutil.copyfile(iSource, iDestination)

        # navigate python to the executable
        os.chdir('exe\\efc')

        # run the executable
        exeInput = tab.filename.get() + '\n'       
        process = subprocess.Popen(['efc.exe'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        out, err = process.communicate(input=bytes(exeInput, "UTF-8"))
        process.terminate()

        # display efc.exe cmd text
        tab.log.text.insert(tk.INSERT, 'efc.exe input:\n ')
        tab.log.text.insert(tk.INSERT, exeInput)
        tab.log.text.insert(tk.INSERT, '\nefc.exe output:\n')
        tab.log.text.insert(tk.INSERT, out)
        tab.log.text.insert(tk.INSERT, '\n')
        # only show errors if they actually happen        
        if err != b'':
            tab.log.text.insert(tk.INSERT, 'efc.exe errors:\n ')
            tab.log.text.insert(tk.INSERT, err)
            tab.log.text.insert(tk.INSERT, '\n')

        # delete input file copied into "efc" folder
        iSource = self.appRoot + '\\exe\\efc\\' + tab.filename.get()
        os.remove(iSource)

        # navigate python to where the executable outputs the files
        os.chdir('efcs')

        # permanently move the executable output files
        tab.log.text.insert(tk.INSERT, 'Files created:\n')
        exeFiles = os.listdir()
        for iFile in exeFiles:
            iFileSource = self.appRoot + '\\exe\\efc\\efcs\\' + iFile
            iFileDestination = self.appRoot + '\\output\\efc\\' + iFile
            # desination file exists - delete old existing file, move new one
            if os.path.isfile(iFileDestination):
                os.remove(iFileDestination)
                os.rename(iFileSource, iFileDestination)
            # desination file does NOT exist - move to "output" folder
            else:
                os.rename(iFileSource, iFileDestination)
            # inform user of generated file(s) location
            tab.log.text.insert(tk.INSERT, ' ' + iFileDestination + '\n')
        tab.log.text.insert(tk.INSERT, '\n--------------------\n\n')

        # navigate python back to the app root
        os.chdir('../../..')

    def run_gwflow(self, tab):
        # copy input file to the same directory as the exe
        iSource = tab.filepath.get()
        iDestination = self.appRoot + '\\exe\\gwflow\\' + tab.filename.get()
        shutil.copyfile(iSource, iDestination)

        # navigate python to the executable
        os.chdir('exe\\gwflow')

        # subprocess can only accept input one time
        # therefore all of the input text and 'enters' need to be in one variable
        file     = tab.filename.get()
        tmax     = '0'
        tmin     = '0'
        precip   = '0'
        solrad   = '0'
        panEvap  = '0'
        runoff   = tab.runoffNum.get()

        # combine all responses to the exe input prompts
        cmds = [file, tmax, tmin, precip, solrad, panEvap, str(runoff)]

        # double check that the user has entered in all drainage values
        for i in range(runoff):
            cmds.append(tab.drainage[i].get())

        # add the 'enter' key press after each response
        exeInput = '\n'.join(cmds)
        exeInput += '\n'
        # construct a pretty log file version
        logInput = [' {0}'.format(elem) for elem in cmds]
        logInput = '\n'.join(logInput)
        logInput += '\n'

        # run the pre-formatted input through the gwflow.exe fortran executable
        process = subprocess.Popen('gwflow.exe', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        out, err = process.communicate(input=bytes(exeInput, "UTF-8"))
        process.terminate()

        # display gwflow.exe cmd text
        tab.log.text.insert(tk.INSERT, 'gwflow.exe input:\n')
        # add a space before each input just for ease of reading in log
        tab.log.text.insert(tk.INSERT, logInput)
        tab.log.text.insert(tk.INSERT, '\ngwflow.exe output:\n')
        tab.log.text.insert(tk.INSERT, out)
        tab.log.text.insert(tk.INSERT, '\n\n')
        # only show errors if they actually happen        
        if err != b'':
            tab.log.text.insert(tk.INSERT, 'gwflow.exe errors:\n ')
            tab.log.text.insert(tk.INSERT, err)
            tab.log.text.insert(tk.INSERT, '\n')

        # delete input file from "gwflow" folder
        iSource = self.appRoot + '\\exe\\gwflow\\' + tab.filename.get()
        os.remove(iSource)

        # permanently move the executable output files
        tab.log.text.insert(tk.INSERT, 'Files created:\n')
        exeFiles = os.listdir()
        for iFile in exeFiles:
            # skip the executable
            if iFile != 'gwflow.exe':
                iFileSource = self.appRoot + '\\exe\\gwflow\\' + iFile
                iFileDestination = self.appRoot + '\\output\\gwflow\\' + iFile
                # desination file exists - delete old existing file, move new one
                if os.path.isfile(iFileDestination):
                    os.remove(iFileDestination)
                    os.rename(iFileSource, iFileDestination)
                # desination file does NOT exist - move to "output" folder
                else:
                    os.rename(iFileSource, iFileDestination)
                # inform user of generated file(s) location
                tab.log.text.insert(tk.INSERT, ' ' + iFileDestination + '\n')
        tab.log.text.insert(tk.INSERT, '\n--------------------\n\n')

        # navigate python back to the app root
        os.chdir('../..')

    def run_makeplot(self, tab):
        # copy input file to the same directory as the exe
        iSource = tab.filepath.get()
        iDestination = self.appRoot + '\\exe\\makeplot\\' + tab.filename.get()
        shutil.copyfile(iSource, iDestination)
        
        # move sr file to the same directory as the exe
        iSource = tab.filepathSr.get()
        iDestination = self.appRoot + '\\exe\\makeplot\\' + tab.filenameSr.get()
        shutil.copyfile(iSource, iDestination)
        
        # move pe file to the same directory as the exe
        iSource = tab.filepathPe.get()
        iDestination = self.appRoot + '\\exe\\makeplot\\' + tab.filenamePe.get()
        shutil.copyfile(iSource, iDestination)

        # navigate python to the executable
        os.chdir('exe\\makeplot')

        # subprocess can only accept input one time
        # therefore all of the input text and 'enters' need to be in one variable
        file      = tab.filename.get()
        simSr     = tab.simSr.get()
        simPet    = tab.simPet.get()
        obsRunoff = tab.obsRunoff.get()
        simRunoff = tab.simRunoff.get()
        startYear = tab.startYear.get() + "1001" #october 1st
        endYear   = tab.endYear.get() + "0930" #september 30th
        
        # combine all responses to the exe input prompts
        cmds = [file, simSr, simPet, obsRunoff, simRunoff, obsRunoff, simRunoff, startYear, endYear]
        
        # add the 'enter' key press after each response
        exeInput = '\n'.join(cmds)
        exeInput += '\n'
        # construct a pretty log file version
        logInput = [' {0}'.format(elem) for elem in cmds]
        logInput = '\n'.join(logInput)
        logInput += '\n'

        # run the executable
        process = subprocess.Popen(['makeplot.exe'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        out, err = process.communicate(input=bytes(exeInput, "UTF-8"))
        process.terminate()

        # display makeplot.exe cmd text
        tab.log.text.insert(tk.INSERT, 'gwflow.exe input:\n')
        # add a space before each input just for ease of reading in log
        tab.log.text.insert(tk.INSERT, logInput)
        tab.log.text.insert(tk.INSERT, '\nmakeplot.exe output:\n')
        tab.log.text.insert(tk.INSERT, out)
        tab.log.text.insert(tk.INSERT, '\n\n')
        # only show errors if they actually happen        
        if err != b'':
            tab.log.text.insert(tk.INSERT, 'makeplot.exe errors:\n ')
            tab.log.text.insert(tk.INSERT, err)
            tab.log.text.insert(tk.INSERT, '\n')

        # run makeplot.r using makeplot.bat
        process = subprocess.Popen(['makeplot.bat'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        out, err = process.communicate(input=bytes('\n', "UTF-8"))
        process.terminate()

        # delete input file from "makeplot" folder
        iSource = self.appRoot + '\\exe\\makeplot\\' + tab.filename.get()
        os.remove(iSource)

        # delete pe file from "makeplot" folder
        iSource = self.appRoot + '\\exe\\makeplot\\' + tab.filenamePe.get()
        os.remove(iSource)

        # delete sr file from "makeplot" folder
        iSource = self.appRoot + '\\exe\\makeplot\\' + tab.filenameSr.get()
        os.remove(iSource)

        # permanently move the executable output files
        tab.log.text.insert(tk.INSERT, 'Files created:\n')
        exeFiles = os.listdir()
        for iFile in exeFiles:
            # skip the executable
            if iFile not in ['makeplot.exe', 'makeplot.r', 'makeplot.bat']:
                iFileSource = self.appRoot + '\\exe\\makeplot\\' + iFile
                iFileDestination = self.appRoot + '\\output\\makeplot\\' + iFile
                # desination file exists - delete old existing file, move new one
                if os.path.isfile(iFileDestination):
                    os.remove(iFileDestination)
                    os.rename(iFileSource, iFileDestination)
                # desination file does NOT exist - move to "output" folder
                else:
                    os.rename(iFileSource, iFileDestination)
                # inform user of generated file(s) location
                tab.log.text.insert(tk.INSERT, ' ' + iFileDestination + '\n')
        tab.log.text.insert(tk.INSERT, '\n--------------------\n\n')

        # navigate python back to the app root
        os.chdir('../..')

    def delete_input(self, file, folder):
        inputFile = self.appRoot + '\\exe\\' + folder + '\\' + file.get()        
        os.remove(inputFile)

# -----------------------------------------------------------------------------

if __name__ == '__main__':
    root = tk.Tk()
    Application(root)
    root.mainloop()