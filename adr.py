# The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
from trytond.model import ModelSQL, ModelView, fields
from trytond.modules.company import CompanyReport
from trytond.wizard import Wizard, Button, StateReport, StateView
from trytond.pool import Pool
from functools import partial
from itertools import groupby

__all__ = ['Adr', 'TransportCategory']

CATEGORIES = 5

class Adr(ModelView, ModelSQL):
    """Adr"""
    __name__ = 'product.adr'

    type = fields.Char('Type', required=True)
    code = fields.Char('Code', required=True)
    name = fields.Char('Name', required=True)
    adr_class = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4.1', '4.1'),
        ('4.2', '4.2'),
        ('4.3', '4.3'),
        ('5.1', '5.1'),
        ('5.2', '5.2'),
        ('6.1', '6.1'),
        ('6.2', '6.2'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('', '')], 'Class', translate=False)
    warning_label = fields.Char('Warning Label')
    packaging_group = fields.Selection([
        ('I', 'I'),
        ('II', 'II'),
        ('III', 'III'),
        ('', '')], 'Packaging Group', translate=False)
    tunnel_code = fields.Selection([
        ('(A)', '(A)'),
        ('(B)', '(B)'),
        ('(C)', '(C)'),
        ('(D)', '(D)'),
        ('(D/E)', '(D/E)'),
        ('(E)', '(E)'),
        ('', '')], 'Tunnel Code', translate=False)
    transport_category = fields.Many2One('product.adr.transport_category',
        'Transport Category')

    @classmethod
    def default_type(cls):
        return 'UN'


class TransportCategory(ModelView, ModelSQL):
    """Transport Category"""
    __name__ = 'product.adr.transport_category'

    code = fields.Char('Code', required=True)
    name = fields.Char('Name', required=True)
    package_multiple = fields.Integer('Package Multiple', required=True)

    @staticmethod
    def default_package_multiple():
        return 1
