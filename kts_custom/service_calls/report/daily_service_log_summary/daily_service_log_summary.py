# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.desk.reportview import build_match_conditions

def execute(filters=None):
	if not filters:
		filters = {}
	elif filters.get("from_date") or filters.get("to_date"):
		filters["from_time"] = "00:00:00"
		filters["to_time"] = "24:00:00"

	columns = get_column()
	conditions = get_conditions(filters)
	data = get_data(conditions, filters)

	return columns, data

def get_column():
	return [_("Service Log") + ":Link/Service Log:120", _("Employee") + "::150", _("Employee Name") + "::150", 
		_("From Datetime") + "::140", _("To Datetime") + "::140", _("Hours") + "::70", 
		_("Activity Type") + "::120", _("Task") + ":Link/Task:150",
		_("Service Call") + ":Link/Service Call:120", _("Status") + "::70"]

def get_data(conditions, filters):
	service_log = frappe.db.sql(""" select `tabService Log`.name, `tabService Log`.employee, `tabService Log`.employee_name,
		`tabService Log Detail`.from_time, `tabService Log Detail`.to_time, `tabService Log Detail`.hours,
		`tabService Log Detail`.activity_type, `tabService Log Detail`.task, `tabService Log Detail`.service_call,
		`tabService Log`.status from `tabService Log Detail`, `tabService Log` where
		`tabService Log Detail`.parent = `tabService Log`.name and %s order by `tabService Log`.name"""%(conditions), filters, as_list=1)

	return time_sheet

def get_conditions(filters):
	conditions = "`tabService Log`.docstatus = 1"
	if filters.get("from_date"):
		conditions += " and `tabService Log Detail`.from_time >= timestamp(%(from_date)s, %(from_time)s)"
	if filters.get("to_date"):
		conditions += " and `tabService Log Detail`.to_time <= timestamp(%(to_date)s, %(to_time)s)"

	match_conditions = build_match_conditions("Service Log")
	if match_conditions:
		conditions += " and %s" % match_conditions

	return conditions
