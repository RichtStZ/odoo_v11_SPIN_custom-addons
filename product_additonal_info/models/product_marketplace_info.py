# -*- coding: utf-8 -*-
from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    xrs_product_ref_ebay = fields.Char(string="eBay-Art.Nr.", help="Artikelnummer bei eBay")
    xrs_product_ASIN_amazon = fields.Char(string="Amazon-ASIN", help="ASIN = Artikelnummer bei Amazon")
    #xrs_product_NrOfPeter = fields.Char(string="Peters ArtikelNr.", help="Von Peter G. genutzte SKU")

