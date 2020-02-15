# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import adr
from . import product

def register():
    Pool.register(
        adr.Adr,
        adr.TransportCategory,
        product.Package,
        product.Template,
        module='product_adr', type_='model')
