from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QTableWidgetItem

from dao.product_dao import ProductDao
from dao.sale_detail_dao import SaleDetailDao
from ui.table import create_table


class select_sale2(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("ui/sel2.ui")

        self.margin_table = create_table(table=self.ui.margin_table,
                                     data=['순위', '제품코드', '제품명', '제품단가', '판매수량', '공급가액', '부가세액',
                                           '판매금액','마진율(%)', '마진액'])

        self.saledetail_load_data(False)
        self.ui.show()

    def saledetail_load_data(self, rank):
        sd = SaleDetailDao()
        res = sd.select_item(rank)
        self.ui.margin_table.setRowCount(0)
        for idx, (
                rank, code, name, price, salecnt, supply_price, addtax, sale_price, marginrate,
                marginprice) in enumerate(res):
            item_code, item_name, item_price, item_salecnt, item_supply_price, item_addtax, item_sale_price, item_marginrate, item_marginprice, item_rank = self.saledetail_create_item(
                code, name, price, salecnt, supply_price, addtax, sale_price, marginrate, marginprice, rank)
            nextIdx = self.ui.margin_table.rowCount()
            self.ui.margin_table.insertRow(nextIdx)
            self.ui.margin_table.setItem(nextIdx, 0, item_rank)
            self.ui.margin_table.setItem(nextIdx, 1, item_code)
            self.ui.margin_table.setItem(nextIdx, 2, item_name)
            self.ui.margin_table.setItem(nextIdx, 3, item_price)
            self.ui.margin_table.setItem(nextIdx, 4, item_salecnt)
            self.ui.margin_table.setItem(nextIdx, 5, item_supply_price)
            self.ui.margin_table.setItem(nextIdx, 6, item_addtax)
            self.ui.margin_table.setItem(nextIdx, 7, item_sale_price)
            self.ui.margin_table.setItem(nextIdx, 8, item_marginrate)
            self.ui.margin_table.setItem(nextIdx, 9, item_marginprice)

    def saledetail_create_item(self, code, name, price, salecnt, supply_price, addtax, sale_price, marginrate,
                               marginprice, rank):
        item_rank = QTableWidgetItem()
        item_rank.setTextAlignment(Qt.AlignHCenter)
        item_rank.setData(Qt.DisplayRole, rank)

        item_code = QTableWidgetItem()
        item_code.setTextAlignment(Qt.AlignHCenter)
        item_code.setData(Qt.DisplayRole, code)

        item_name = QTableWidgetItem()
        item_name.setTextAlignment(Qt.AlignHCenter)
        item_name.setData(Qt.DisplayRole, name)

        item_price = QTableWidgetItem()
        item_price.setTextAlignment(Qt.AlignRight)
        item_price.setData(Qt.DisplayRole, format(int(price), ',d'))

        item_salecnt = QTableWidgetItem()
        item_salecnt.setTextAlignment(Qt.AlignRight)
        item_salecnt.setData(Qt.DisplayRole, format(int(salecnt), ',d'))

        item_supply_price = QTableWidgetItem()
        item_supply_price.setTextAlignment(Qt.AlignRight)
        item_supply_price.setData(Qt.DisplayRole, format(int(supply_price), ',d'))

        item_addtax = QTableWidgetItem()
        item_addtax.setTextAlignment(Qt.AlignRight)
        item_addtax.setData(Qt.DisplayRole, format(int(addtax), ',d'))

        item_sale_price = QTableWidgetItem()
        item_sale_price.setTextAlignment(Qt.AlignRight)
        item_sale_price.setData(Qt.DisplayRole, format(int(sale_price), ',d'))

        item_marginrate = QTableWidgetItem()
        item_marginrate.setTextAlignment(Qt.AlignRight)
        item_marginrate.setData(Qt.DisplayRole, marginrate)

        item_marginprice = QTableWidgetItem()
        item_marginprice.setTextAlignment(Qt.AlignRight)
        item_marginprice.setData(Qt.DisplayRole, format(int(marginprice), ',d'))

        return item_code, item_name, item_price, item_salecnt, item_supply_price, item_addtax, item_sale_price, item_marginrate, item_marginprice, item_rank
