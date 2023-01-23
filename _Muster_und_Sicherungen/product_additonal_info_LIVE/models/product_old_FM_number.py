# -*- coding: utf-8 -*-
from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    xrs_old_FM_number = fields.Char(string="FM-Art.Nr.", help="Artikelnummer aus dem Flexmaster")

