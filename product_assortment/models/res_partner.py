# Copyright 2020 Tecnativa - Carlos Roca
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
from odoo import models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def action_define_product_assortment(self):
        self.ensure_one()
        whitelists = self.env['ir.filters'].search([
            ('partner_ids', 'in', self.ids),
            ('is_assortment', '=', True),
        ])

        action = self.env.ref(
            "product_assortment.actions_product_assortment_view")
        action_dict = action.read()[0]
        action_dict['domain'] = [('id', 'in', whitelists.ids)]
        ctx = self.env.context.copy()
        ctx.update({
            'default_partner_ids': self.ids,
            'product_assortment': True,
        })
        action_dict['context'] = ctx
        return action_dict
