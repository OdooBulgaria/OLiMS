# -*- coding: utf-8 -*-
from openerp import http

# class DemoModule(http.Controller):
#     @http.route('/demo_module/demo_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/demo_module/demo_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('demo_module.listing', {
#             'root': '/demo_module/demo_module',
#             'objects': http.request.env['demo_module.demo_module'].search([]),
#         })

#     @http.route('/demo_module/demo_module/objects/<model("demo_module.demo_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('demo_module.object', {
#             'object': obj
#         })