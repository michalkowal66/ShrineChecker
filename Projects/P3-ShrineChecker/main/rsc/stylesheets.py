ui_stylesheet = '''
QLabel#lbl1{
	font: 24px "Sylfaen";
	color: white;
	background-color: rgba(0, 0, 0, 0);
}

QLabel#lbl1_2{
	font: 30px "Sylfaen";
	color: white;
	background-color: rgba(0, 0, 0, 0);
}

QPushButton {
	font: 18px "Sylfaen";
	color: white;
	background-color:#2F3538;
}

QPushButton:hover {
	font: 18px "Sylfaen";
	color: white;
	background-color:#404040;
}

QComboBox {
	font: 18px "Sylfaen";
	color: white;
	background-color:#2F3538;
	selection-background-color:#2F3538;
}

QComboBox QAbstractItemView {
	font: 18px "Sylfaen";
	color: white;
    background-color:#2F3538;
	selection-background-color: #404040;
	outline: 0;
}

QScrollBar:vertical {
	font: 18px "Sylfaen";
	color: white;
	background:#404040;
}

QPushButton#settings_btn{
	font: 18px "Sylfaen";
	color: white;
	qproperty-iconSize: 30px;
}

QLabel#perk1_lbl {
	font: 20px "Sylfaen";
	color: #6e6d6d;
	background-color: rgba(0, 0, 0, 0);
}
QLabel#perk2_lbl {
	font: 20px "Sylfaen";
	color: #6e6d6d;
	background-color: rgba(0, 0, 0, 0);
}
QLabel#perk3_lbl {
	font: 20px "Sylfaen";
	color: #6e6d6d;
	background-color: rgba(0, 0, 0, 0);
}
QLabel#perk4_lbl {
	font: 20px "Sylfaen";
	color: #6e6d6d;
	background-color: rgba(0, 0, 0, 0);
}

QLabel#date_lbl {
	font: 16px "Sylfaen";
	color: #6e6d6d;
	background-color: rgba(0, 0, 0, 0);
}

QListWidget{
	font: 18px "Sylfaen";
	color: white;
	background-color: rgba(0, 0, 0, 0);
	border: 1px solid rgba(255, 255, 255, 0.3);
	outline: 0;
}

QListWidget::item:hover {
	font: 18px "Sylfaen";
	color: white;
    background-color: rgba(47, 53, 56, 0.3);
}

QListWidget::item:selected {
	font: 18px "Sylfaen";
	color: white;
	background-color: rgba(64, 64, 64, 0.3);
}
'''

message_stylesheet = '''
QLabel#bg {
	border: 1px solid white;
}

QLabel#msg_lbl{
	color: white;
	font: 16px "Sylfaen";
}
QLabel#title_lbl {
	color: white;
	font: 20px "Sylfaen";
}

QPushButton {
	color: white;
	font: 18px "Sylfaen";
	background-color:#2F3538;
}

QPushButton:hover {
	background-color:#404040;
}

QPushButton:disabled {
	color: black;
	background-color:#141718;
}
'''

notification_stylesheet = '''
QLabel#perk1_lbl {
	font: 20px "Sylfaen";
	color: white;
}

QLabel#msg1_lbl {
	font: 16px "Sylfaen";
	color: white;
}

QLabel#perk2_lbl {
	font: 20px "Sylfaen";
	color: white;
}

QLabel#msg2_lbl {
	font: 16px "Sylfaen";
	color: white;
}

QLabel#perk3_lbl {
	font: 20px "Sylfaen";
	color: white;
}

QLabel#msg3_lbl {
	font: 16px "Sylfaen";
	color: white;
}

QLabel#perk4_lbl {
	font: 20px "Sylfaen";
	color: white;
}

QLabel#msg4_lbl {
	font: 16px "Sylfaen";
	color: white;
}

QPushButton {
	font: 18px "Sylfaen";
	background-color:#2F3538;
	color: white;
}

QPushButton:hover {
	font: 18px "Sylfaen";
	background-color:#404040;
	color: white;
}
'''

progress_stylesheet = '''
QLabel#bg {
	border: 1px solid white;
}

QLabel#wait_lbl{
	color: white;
	font: 20px "Sylfaen";
}
QLabel#msg_lbl {
	color: white;
	font: 16px "Sylfaen";
}

QProgressBar{
	border: solid black;
	border-radius: 2px;
	color: black;
	background-color: #404040;
}

QProgressBar::chunk {
background-color: white;
}  

QPushButton {
	color: white;
	font: 18px"Sylfaen";
	background-color:#2F3538;
}

QPushButton:hover {
	background-color:#404040;
}

QPushButton:disabled {
	color: black;
	background-color:#141718;
}
'''

settings_stylesheet = '''
QLabel#settings_lbl {
	color: white;
	font: 24px "Sylfaen";
}

QCheckBox {
	color: white;
	font: 18px "Sylfaen";
}

QLabel {
	color: white;
	font: 18px "Sylfaen";
}

QPushButton {
	color: white;
	font: 18px "Sylfaen";
	background-color:#2F3538;
}

QPushButton:hover {
	color: white;
	font: 18px "Sylfaen";
	background-color:#404040;
}

QLabel#bg {
	border: 1px solid rgba(255, 255, 255, 0.2);
}

QComboBox {
	color: white;
	font: 18px "Sylfaen";
	background-color:#2F3538;
	selection-background-color:#2F3538;
}

QComboBox QAbstractItemView {
	color: white;
	font: 18px "Sylfaen";
    background-color:#2F3538;
	selection-background-color: #404040;
	outline: 0;
}

QScrollBar:vertical {    
	color: white;
	font: 18px "Sylfaen";
	background:#404040;
}
'''