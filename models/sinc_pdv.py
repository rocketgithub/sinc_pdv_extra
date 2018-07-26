# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Location(models.Model):
    _inherit = "stock.location"

    sinc_id = fields.Integer('Sinc ID')

class pos_sat_resolucion(models.Model):
    _inherit = "pos_sat.resolucion"

    sinc_id = fields.Integer('Sinc ID')

class AccountJournal(models.Model):
    _inherit = "account.journal"

    sinc_id = fields.Integer('Sinc ID')

class PosCategory(models.Model):
    _inherit = "pos.category"

    sinc_id = fields.Integer('Sinc ID')

class ProductCategory(models.Model):
    _inherit = "product.category"

    sinc_id = fields.Integer('Sinc ID')

class PosConfig(models.Model):
    _inherit = "pos.config"

    sinc_id = fields.Integer('Sinc ID')

class Users(models.Model):
    _inherit = "res.users"

    sinc_id = fields.Integer('Sinc ID')

class ProductProduct(models.Model):
    _inherit = "product.product"

    sinc_id = fields.Integer('Sinc ID')

class ProductTemplate(models.Model):
    _inherit = "product.template"

    sinc_id = fields.Integer('Sinc ID')

class PosGTExtra(models.Model):
    _inherit = "pos_gt.extra"

    sinc_id = fields.Integer('Sinc ID')

class MrpBom(models.Model):
    _inherit = "mrp.bom"

    sinc_id = fields.Integer('Sinc ID')

class PosSession(models.Model):
    _inherit = "pos.session"

    sinc_id = fields.Integer('Sinc ID', default=0)

class Inventory(models.Model):
    _inherit = "stock.inventory"

    sinc_id = fields.Integer('Sinc ID', default=0)
