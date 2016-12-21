# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class DuplicationError(frappe.ValidationError): pass

class ResponsibilityCost(Document):
	def validate(self):
		self.set_title()
		self.check_unique()
		
	def set_title(self):
		if self.employee:
			if not self.employee_name:
				self.employee_name = frappe.db.get_value("Employee", self.employee, "employee_name")
			self.title = _("{0} for {1}").format(self.employee_name, self.responsibility_type)
		else:
			self.title = self.responsibility_type

	def check_unique(self):
		if self.employee:
			if frappe.db.sql("""select name from `tabResponsibility Cost` where employee_name= %s and responsibility_type= %s and name != %s""",
				(self.employee_name, self.responsibility_type, self.name)):
					frappe.throw(_("Responsibility Cost exists for Employee {0} against Responsibility Type - {1}")
						.format(self.employee, self.responsibility_type), DuplicationError)
		else:
			if frappe.db.sql("""select name from `tabResponsibility Cost` where ifnull(employee, '')='' and responsibility_type= %s and name != %s""",
				(self.responsibility_type, self.name)):
					frappe.throw(_("Default Responsibility Cost exists for Responsibility Type - {0}")
						.format(self.responsibility_type), DuplicationError)
