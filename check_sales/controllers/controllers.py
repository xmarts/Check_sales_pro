# -*- coding: utf-8 -*-
from odoo import http

# class CheckSales(http.Controller):
#     @http.route('/check_sales/check_sales/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/check_sales/check_sales/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('check_sales.listing', {
#             'root': '/check_sales/check_sales',
#             'objects': http.request.env['check_sales.check_sales'].search([]),
#         })

#     @http.route('/check_sales/check_sales/objects/<model("check_sales.check_sales"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('check_sales.object', {
#             'object': obj
#         })