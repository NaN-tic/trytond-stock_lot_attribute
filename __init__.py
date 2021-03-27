# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from . import stock

def register():
    Pool.register(
        stock.LotAttributeSet,
        stock.LotAttribute,
        stock.LotAttributeAttributeSet,
        stock.Template,
        stock.Lot,
        module='stock_lot_attribute', type_='model')
