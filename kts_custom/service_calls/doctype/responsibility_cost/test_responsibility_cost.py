# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest

from erpnext.service_calls.doctype.responsibility_cost.responsibility_cost import DuplicationError

class TestResponsibilityCost(unittest.TestCase):
	def test_duplication(self):
		frappe.db.sql("delete from `tabResponsibility Cost`")
		responsibility_cost1 = frappe.new_doc('Responsibility Cost')
		responsibility_cost1.update({
			"employee": "_T-Employee-0001",
			"employee_name": "_Test Employee",
			"responsibility_type": "_Test Responsibility Type 1",
			"billing_rate": 100,
			"costing_rate": 50
		})
		responsibility_cost1.insert()
		responsibility_cost2 = frappe.copy_doc(responsibility_cost1)
		self.assertRaises(DuplicationError, responsibility_cost2.insert )
		frappe.db.sql("delete from `tabResponsibility Cost`")
