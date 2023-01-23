from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    country_of_origin_id = fields.Many2one(comodel_name='res.country', string='Country of Origin', help='Land auswählen.')