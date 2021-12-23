# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools

class salescustom(models.Model):
    _inherit = "sale.order"
    employee_name = fields.Many2one('hr.employee', string="Employee Name")