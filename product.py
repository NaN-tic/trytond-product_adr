# The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
from trytond.model import ModelSQL
from trytond.model import ModelView
from trytond.pool import PoolMeta
from trytond.model import fields, DeactivableMixin

__all__ = ['Product', 'Package']


class Product(metaclass=PoolMeta):
    __name__ = 'product.product'

    adr = fields.Many2One('product.adr', 'Adr')
    units_per_package = fields.Float('Units per Package')
    packaging = fields.Many2One('product.package', 'Packaging',
        ondelete='RESTRICT')

    def adr_name(self):
        return self.name

    def adr_text(self):
        name = self.adr.type + ' ' + self.adr.code + ' ' + \
               self.adr.name if self.adr else ''
        if self.adr:
            if self.adr.warning_label:
                name = name + ' ' + self.adr.warning_label
            if self.adr.packaging_group:
                name = name + ' ' + self.adr.packaging_group
            if self.adr.tunnel_code:
                name = name + ' ' + self.adr.tunnel_code
        return name

    def adr_code_full(self):
        if not self.adr:
            return ''
        code = self.adr.code
        if self.adr.packaging_group:
            code = code + ' - ' + self.adr.packaging_group
        if self.adr.tunnel_code:
            code = code + ' - ' + self.adr.tunnel_code
        return code

    def adr_multiple(self):
        if self.adr and self.adr.transport_category:
                return self.adr.transport_category.package_multiple
        return 1


class Package(DeactivableMixin, ModelSQL, ModelView):
    """Product Package"""
    __name__ = 'product.package'

    name = fields.Char('Name', required=True)
