# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions

class ean13project(models.Model):
    _inherit = 'product.template'

    # ean13 = fields.Char( required=True)
    # default_code = fields.Char(required=True)



class Ean13(models.Model):
    _inherit = 'product.product'

    ean13 = fields.Char(string ="Réference S")
    default_code = fields.Char(string ="Réference L")

    def _check_ean_key(self, cr, uid, ids, context=None):
        return True

    _constraints = [(_check_ean_key, 'override function', ['ean13'])]
