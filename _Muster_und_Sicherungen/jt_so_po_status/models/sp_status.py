# -*- coding: utf-8 -*-
#################################################################################
#                                                                               #
#    Part of Odoo. See LICENSE file for full copyright and licensing details.   #
#    Copyright (C) 2018 Jupical Technologies Pvt. Ltd. <http://www.jupical.com> #
#                                                                               #
#################################################################################

from odoo import api, fields, models

class SaleOrder(models.Model):

    _inherit = "sale.order"

    @api.multi
    @api.depends('picking_ids.state')
    def check_status(self):
        """
         Check all deliveries are done or not.If all deliveries done return done else open.
        :return: status done or open.
        """
        for order in self:
            done = 0
            if order.picking_ids:
                for picking in order.picking_ids:
                    if picking.state == 'done':
                        done += 1
                if done == order.delivery_count:
                    order.delivery_status = 'done'
                else:
                    order.delivery_status = 'open'
            else:
                order.delivery_status = 'open'

    delivery_status = fields.Selection([
        ('done', 'Done'),
        ('open', 'Open'),
    ], compute='check_status', string='Delivery Status', store=True, default='open')

class PurchaseOrder(models.Model):

    _inherit = "purchase.order"

    @api.multi
    @api.depends('picking_ids.state')
    def check_status(self):
        """
         Check all deliveries are done or not.If all deliveries done return done else open.
        :return: status done or open.
        """
        for order in self:
            done = 0
            if order.picking_ids:
                for picking in order.picking_ids:
                    if picking.state == 'done':
                        done += 1
                if done == order.picking_count:
                    order.shipping_status = 'done'
                else:
                    order.shipping_status = 'open'
            else:
                order.shipping_status = 'open'

    shipping_status = fields.Selection([
        ('done', 'Done'),
        ('open', 'Open'),
    ], compute='check_status', string='Shipping Status', store=True, default='open')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: