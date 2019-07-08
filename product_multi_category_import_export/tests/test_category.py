# -*- coding: utf-8 -*-
# Copyright 2019 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests.common import TransactionCase


class TestCategory(TransactionCase):
    def setUp(self):
        super(TestCategory, self).setUp()
        ref = self.env.ref
        self.product = ref("product.product_product_1")
        self.categ_1 = ref("product.product_category_2")
        self.categ_2 = ref("product.product_category_3")
        self.categ_3 = ref("product.product_category_4")

    def test_setting_one_category(self):
        self.product.categ_secondary_one_id = self.categ_1
        self.assertEqual(self.product.categ_ids, self.categ_1)

    def test_setting_multi_category(self):
        self.product.categ_secondary_one_id = self.categ_1
        self.product.categ_secondary_two_id = self.categ_2
        self.product.categ_secondary_three_id = self.categ_3
        self.assertEqual(
            self.product.categ_ids, self.categ_1 + self.categ_2 + self.categ_3
        )
