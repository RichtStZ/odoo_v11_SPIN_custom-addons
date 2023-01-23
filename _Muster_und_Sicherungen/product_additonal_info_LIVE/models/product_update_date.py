# -*- coding: utf-8 -*-
from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    xrs_lastupdatePrice = fields.Date(string="Preispflege", help="Datum der letzten Preispflege")
    xrs_lastupdateProduct = fields.Date(string="Produktpflege", help="Datum der letzten Produktpflege")

