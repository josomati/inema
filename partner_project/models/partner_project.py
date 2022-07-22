from dataclasses import field
from unicodedata import name
from bs4 import Tag
from odoo import api, fields, models
from random import randint

class PartnerProject(models.Model):
    _description = 'project Tags'
    _name = 'res.partner.project'

    def _get_default_color(self):
        return randint(1, 11)

    name = fields.Char(string='project name', required=True)
    color = fields.Integer(string='Color', default=_get_default_color)
    description = fields.Text('Description')

class Partner(models.Model):
    _inherit ='res.partner'
    commercial_name_id = fields.Char('Commercial name')
    partner_project_id = fields.Many2many('res.partner.project', string='Partner project')
