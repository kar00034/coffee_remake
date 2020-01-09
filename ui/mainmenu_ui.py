from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from dao.product_dao import ProductDao
from dao.sale_dao import SaleDao
from ui.sel1_ui import select_sale
from ui.sel2_ui import select_sale2


class mainmenu(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("ui/main.ui")

        self.ui.btn_add.clicked.connect(self.add_val)
        self.ui.btn_sel1.clicked.connect(self.select1)
        self.ui.btn_sel2.clicked.connect(self.select2)
        self.ui.show()

    def add_val(self):
        self.get_item_form_le()
        self.init_item()

    def select1(self):
        self.sel1=select_sale()

    def select2(self):
        self.sel2=select_sale2()

    def get_item_form_le(self):
        pdt = ProductDao()
        sdt = SaleDao()
        code = self.ui.line_code.text()
        name = self.ui.line_name.text()
        price = self.ui.line_price.text()
        count = self.ui.line_count.text()
        margin = self.ui.line_margin.text()

        pdt.insert_product(code=code, name=name)
        sdt.insert_item(price=price,salecnt=count,marginrate=margin)
        return self.create_item(code, name)

    def create_item(self, code, name):
        item_code = QTableWidgetItem()
        item_code.setTextAlignment(Qt.AlignCenter)
        item_code.setData(Qt.DisplayRole, code)
        item_name = QTableWidgetItem()
        item_name.setTextAlignment(Qt.AlignCenter)
        item_name.setData(Qt.DisplayRole, name)
        return item_code, item_name

    def init_item(self):
        self.ui.line_code.clear()
        self.ui.line_name.clear()
        self.ui.line_price.clear()
        self.ui.line_margin.clear()
        self.ui.line_count.clear()