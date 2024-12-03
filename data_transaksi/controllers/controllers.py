# -*- coding: utf-8 -*-
# from odoo import http


# class DataTransaksi(http.Controller):
#     @http.route('/data_transaksi/data_transaksi', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/data_transaksi/data_transaksi/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('data_transaksi.listing', {
#             'root': '/data_transaksi/data_transaksi',
#             'objects': http.request.env['data_transaksi.data_transaksi'].search([]),
#         })

#     @http.route('/data_transaksi/data_transaksi/objects/<model("data_transaksi.data_transaksi"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('data_transaksi.object', {
#             'object': obj
#         })

