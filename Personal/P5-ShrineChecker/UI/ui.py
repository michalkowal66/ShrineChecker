import csv
from csv import reader
import io
import os
from sc_ui import *

#To do list:
#Make the animation showing that desired perk is available
#Merge main.py and ui.py
#Prepare the proper bg and css
#Make reload button work

class SC_Ui(Ui_MainWindow):
    def __init__(self):
        self.current_shrine = []
        self.desired_perks = []
        self.perks = []
        self.perks_csv = 'perks.csv'
        self.shrine_csv = 'shrine.csv'
        self.desired_perks_csv = 'desired_perks.csv'
        self.local_dir = os.path.expanduser('~') + '\Documents\ShrineChecker'
        self.local_data = self.local_dir + '\local'
        self.local_img = self.local_data + '\img'
        self.load_local_data()

    def setupUi(self, MainWindow):
        super(SC_Ui, self).setupUi(MainWindow)
        self.load_content()
        self.add_btn.clicked.connect(self.add_perk)
        self.remove_btn.clicked.connect(self.remove_perk)

        self.date_lbl.setText(self.current_shrine[0])

        self.img1.setPixmap(QtGui.QPixmap(self.local_img+f'\{self.current_shrine[1]}.png'))
        self.img1.setScaledContents(True)
        self.perk1_lbl.setText(self.current_shrine[1])

        self.img2.setPixmap(QtGui.QPixmap(self.local_img+f'\{self.current_shrine[2]}.png'))
        self.img2.setScaledContents(True)
        self.perk2_lbl.setText(self.current_shrine[2])

        self.img3.setPixmap(QtGui.QPixmap(self.local_img+f'\{self.current_shrine[3]}.png'))
        self.img3.setScaledContents(True)
        self.perk3_lbl.setText(self.current_shrine[3])

        self.img4.setPixmap(QtGui.QPixmap(self.local_img+f'\{self.current_shrine[4]}.png'))
        self.img4.setScaledContents(True)
        self.perk4_lbl.setText(self.current_shrine[4])

    def load_local_data(self): 
        with open(f'{self.local_data}/{self.desired_perks_csv}', newline='') as f:
            reader = csv.reader(f)
            for line in reader:
                self.desired_perks.append(line[0])
            
        with open(f'{self.local_data}/{self.perks_csv}', newline='') as f:
            reader = csv.reader(f)
            for line in reader:
                self.perks.append(line[0])

        with open(f'{self.local_data}/{self.shrine_csv}', newline='') as f:
            reader = csv.reader(f)
            for line in reader:
                self.current_shrine.append(line[0])

    def load_content(self):
        for perk in self.perks:
            self.perks_combo.addItem(perk)

        if len(self.desired_perks) > 0:
            for perk in self.desired_perks:
                self.perks_list.addItem(perk)

    def add_perk(self):
        perk = self.perks_combo.currentText()
        items = self.perks_list.findItems(perk, QtCore.Qt.MatchExactly)
        if len(items) > 0:
            return
        else:
            self.perks_list.addItem(perk)
            self.desired_perks.append(perk)
            with io.open(f'{self.local_data}/{self.desired_perks_csv}', 'a', encoding='utf-8') as output:
                    writer = csv.writer(output, lineterminator='\n')
                    writer.writerow([perk])
    
    def remove_perk(self):
        sel_perk_txt = self.perks_list.currentItem().text()
        sel_perks = self.perks_list.selectedItems()
        for perk in sel_perks:
            self.perks_list.takeItem(self.perks_list.row(perk))
            self.desired_perks.remove(sel_perk_txt)
            with io.open(f'{self.local_data}/{self.desired_perks_csv}', 'w', encoding='utf-8') as output:
                    writer = csv.writer(output, lineterminator='\n')
                    for val in self.desired_perks:
                        writer.writerow([val])
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = SC_Ui()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
