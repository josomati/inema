from odoo import _, api, fields, models

import datetime

class CrmLead(models.Model):
    _inherit = "crm.lead"

    pricelist_id = fields.Many2one(
        'product.pricelist', string='Pricelist', check_company=True, readonly=False,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]", tracking=1,
        help="If you change the pricelist, only newly added lines will be affected.")
    currency_id = fields.Many2one(related='pricelist_id.currency_id', depends=["pricelist_id"], store=True)
    amount_total = fields.Monetary('Amount Total', currency_field='currency_id', tracking=True)


    @api.onchange('amount_total')
    def _change_amount(self):
        for rec in self:
            if rec.pricelist_id:
                if rec.currency_id.id != rec.company_currency.id:
                    convert_amount = rec.currency_id._convert(rec.amount_total, rec.company_currency, rec.company_id, datetime.date.today())
                    rec.expected_revenue = convert_amount
                else:
                    convert_amount = rec.amount_total
                    rec.expected_revenue = convert_amount