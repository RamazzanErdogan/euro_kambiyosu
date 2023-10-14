import sys
import typing
import requests
import json
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget
from eurokambiyosu import Ui_MainWindow
import random
class pencere(QtWidgets.QMainWindow):
    def __init__(self):
        super(pencere,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.cevir_button.clicked.connect(self.yazdir)
    def yazdir(self):
        para_birimi = self.ui.parabirimi.currentText()
        kisaltma = self.islemler(para_birimi)
        return kisaltma
    def islemler(self, para_birimi):
        x=random.randint(0,250)
        y=random.randint(0,250)
        z=random.randint(0,250)
        if '(' in para_birimi and ')' in para_birimi:
            kisaltma = para_birimi.split('(')[1].split(')')[0]
            apı_url="http://api.exchangeratesapi.io/v1/latest?access_key=f40e16ed6bd6462c7c1423a8fcfd67fa&format=1"
            result=requests.get(apı_url)
            result=json.loads(result.text)
            bozdurulan_euro_miktari=int(self.ui.euro_deger.text())
            alinan_doviz=kisaltma
            sonuc0=bozdurulan_euro_miktari*result['rates'][alinan_doviz]
            self.ui.sonuc.setStyleSheet(f"background: rgb({y}, {x}, {z}); font: 63 10pt 'Sitka Display Semibold';")
            self.ui.sonuc.setText(f"{bozdurulan_euro_miktari}€=={sonuc0}{alinan_doviz}")        
def calistir():
    app = QtWidgets.QApplication(sys.argv)
    win = pencere()
    win.show()
    sys.exit(app.exec_())
calistir()