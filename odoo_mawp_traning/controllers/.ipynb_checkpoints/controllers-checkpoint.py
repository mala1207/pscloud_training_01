# -*- coding: utf-8 -*-
from odoo import http

# class ../user/odooMawpTraning(http.Controller):
#     @http.route('/../user/odoo_mawp_traning/../user/odoo_mawp_traning/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/../user/odoo_mawp_traning/../user/odoo_mawp_traning/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('../user/odoo_mawp_traning.listing', {
#             'root': '/../user/odoo_mawp_traning/../user/odoo_mawp_traning',
#             'objects': http.request.env['../user/odoo_mawp_traning.../user/odoo_mawp_traning'].search([]),
#         })

#     @http.route('/../user/odoo_mawp_traning/../user/odoo_mawp_traning/objects/<model("../user/odoo_mawp_traning.../user/odoo_mawp_traning"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('../user/odoo_mawp_traning.object', {
#             'object': obj
#         })