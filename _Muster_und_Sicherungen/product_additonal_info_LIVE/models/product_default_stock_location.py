# -*- coding: utf-8 -*-
from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = "product.template"

    xrs_product_default_location1 = fields.Many2one(comodel_name="stock.location", string="Haupt-Lagerort", help="Der Lagerort, wo das Produkt normalerweise sein soll.")
    xrs_product_default_location2 = fields.Many2one(comodel_name="stock.location", string="Neben-Lagerort", help="Der Lagerort, wo das Produkt noch sein kann. (z.B. im Ladenbereich)")

