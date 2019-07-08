# -*- coding: utf-8 -*-
# Copyright 2019 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    categ_secondary_one_id = fields.Many2one(
        "product.category",
        "Categ Secondary One",
        inverse="_inverse_secondary_category",
        compute="_compute_secondary_one_category",
    )
    categ_secondary_two_id = fields.Many2one(
        "product.category",
        "Categ Secondary Two",
        inverse="_inverse_secondary_category",
        compute="_compute_secondary_two_category",
    )
    categ_secondary_three_id = fields.Many2one(
        "product.category",
        "Categ Secondary Three",
        inverse="_inverse_secondary_category",
        compute="_compute_secondary_three_category",
    )
    categ_secondary_four_id = fields.Many2one(
        "product.category",
        "Categ Secondary Four",
        inverse="_inverse_secondary_category",
        compute="_compute_secondary_four_category",
    )

    def _get_secondary_category(self, position):
        self.ensure_one()
        if len(self.categ_ids) >= position:
            return self.categ_ids[position - 1]
        else:
            return self.env["product.category"].browse(False)

    @api.depends("categ_ids")
    def _compute_secondary_one_category(self):
        for record in self:
            record.categ_secondary_one_id = record._get_secondary_category(1)

    @api.depends("categ_ids")
    def _compute_secondary_two_category(self):
        for record in self:
            record.categ_secondary_two_id = record._get_secondary_category(2)

    @api.depends("categ_ids")
    def _compute_secondary_three_category(self):
        for record in self:
            record.categ_secondary_three_id = record._get_secondary_category(3)

    @api.depends("categ_ids")
    def _compute_secondary_four_category(self):
        for record in self:
            record.categ_secondary_four_id = record._get_secondary_category(4)

    def _inverse_secondary_category(self):
        for record in self:
            categs = (
                record.categ_secondary_one_id
                + record.categ_secondary_two_id
                + record.categ_secondary_three_id
                + record.categ_secondary_four_id
            )
            record.categ_ids = categs
