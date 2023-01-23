# -*- coding: utf-8 -*-
#################################################################################
#                                                                               #
#    Part of Odoo. See LICENSE file for full copyright and licensing details.   #
#    Copyright (C) 2018 Jupical Technologies Pvt. Ltd. <http://www.jupical.com> #
#                                                                               #
#################################################################################

{
    "name": "Sale, Purchase Delivery and Shipping Status",
    "version": "11.0.0.1.0",
    "author":"Jupical Technologies Pvt. Ltd.",
    "maintainer": "Jupical Technologies Pvt. Ltd.",
    "category": "Sale and Purchase",
    "summary": "Sale, Purchase Delivery and Shipping Status",
    "depends": [
        'sale_management','purchase','sale_stock'
    ],
    'description': """

Sale and Purchase Status
========================

- Now can set the status of Delivery status and Shipping status to done, if all pickings or shippings are done.
- Can print Sale BI/Purchase BI report based on Delivery status or Shipping status
        """,
    'website': "http://www.jupical.com",
    'license': 'AGPL-3',
    'price': 25.00,
    "currency":"EUR",
    'images': ['static/description/Banner.png'],
    'license':'AGPL-3',
    "data": [
        'views/sp_status_view.xml',
        'report/purchase_report_views.xml',
        'report/sale_report_view.xml'
    ],
    "installable": True,
    "auto_install": False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: