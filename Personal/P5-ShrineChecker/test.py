
#     def __init__(self):
#             self.surv_perks = []
#             self.killer_perks = []
#             self.current_shrine = []
#             self.desired_perks = []
#             self.perks = []
#             self.surv_perks_csv = 'surv_perks.csv'
#             self.killer_perks_csv = 'killer_perks.csv'
#             self.perks_csv = 'perks.csv'
#             self.desired_perks_csv = 'desired_perks.csv'
#             self.local_dir = os.path.expanduser('~') + '\Documents\ShrineChecker'
#             self.local_data = self.local_dir + '\local'

#             self.load_local_data()

#     def setupUi(self, MainWindow):

#         self.load_content()

#         self.add_btn.clicked.connect(self.add_perk)
       
#         self.remove_btn.clicked.connect(self.remove_perk)

#     def load_local_data(self):
#         with open(f'{self.local_data}/{self.surv_perks_csv}', newline='') as f:
#                 reader = csv.reader(f)
#                 for line in reader:
#                     self.surv_perks.append(line[0])    
            
#         with open(f'{self.local_data}/{self.killer_perks_csv}', newline='') as f:
#             reader = csv.reader(f)
#             for line in reader:
#                 self.killer_perks.append(line[0])    

#         with open(f'{self.local_data}/{self.desired_perks_csv}', newline='') as f:
#             reader = csv.reader(f)
#             for line in reader:
#                 self.desired_perks.append(line[0])
            
#         with open(f'{self.local_data}/{self.perks_csv}', newline='') as f:
#             reader = csv.reader(f)
#             for line in reader:
#                 self.perks.append(line[0])

#     def load_content(self):
#         for perk in self.perks:
#             self.perks_combo.addItem(perk)

#     def add_perk(self):
#         perk = self.perks_combo.currentText()
#         items = self.perks_list.findItems(perk, QtCore.Qt.MatchExactly)
#         if len(items) > 0:
#             return
#         else:
#             self.perks_list.addItem(perk)
    
#     def remove_perk(self):
#         sel_items = self.perks_list.selectedItems()
#         for item in sel_items:
#             self.perks_list.takeItem(self.perks_list.row(item))

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
