# Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    manufacturer = fields.Many2one(
        comodel_name='res.partner', string='Manufacturer', help='Herstellerunternehmen aus Kontakten auswählen. Wenn nicht vorhanden --> neu anlegen.',
    )
    manufacturer_pname = fields.Char(string='Manuf. Product Name', help='Artikelbezeichnung des Herstellers')
    manufacturer_pref = fields.Char(string='Manuf. Product Code', help='Artikelnummer des Herstellers')
    manufacturer_purl = fields.Char(string='Manuf. Product URL', help='Adresse fuer digitale Produkte oder auf die Herstellerwebsite zur Produktbeschreibung')
