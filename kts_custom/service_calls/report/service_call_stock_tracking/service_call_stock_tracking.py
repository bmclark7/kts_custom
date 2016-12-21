# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt
from __future__ import unicode_literals

import frappe
from frappe import _

def execute(filters=None):
	columns = get_columns()
	serv_details = get_service_call_details()
	pr_item_map = get_purchased_items_cost()
	se_item_map = get_issued_items_cost()
	dn_item_map = get_delivered_items_cost()

	data = []
	for service_call in serv_details:
		data.append([service_call.name, pr_item_map.get(service_call.name, 0),
			se_item_map.get(service_call.name, 0), dn_item_map.get(service_call.name, 0),
			service_call.service_call_name, service_call.status, service_call.company,
			service_call.customer, service_call.estimated_costing, service_call.expected_start_date,
			service_call.expected_end_date])

	return columns, data

def get_columns():
	return [_("Service Call Id") + ":Link/Service Call:140", _("Cost of Purchased Items") + ":Currency:160",
		_("Cost of Issued Items") + ":Currency:160", _("Cost of Delivered Items") + ":Currency:160",
		_("Service Call Name") + "::120", _("Service Call Status") + "::120", _("Company") + ":Link/Company:100",
		_("Customer") + ":Link/Customer:140", _("Service Call Value") + ":Currency:120",
		_("Service Call Start Date") + ":Date:120", _("Completion Date") + ":Date:120"]

def get_service_call_details():
	return frappe.db.sql(""" select name, service_call_name, status, company, customer, estimated_costing,
		expected_start_date, expected_end_date from tabService Call where docstatus < 2""", as_dict=1)

def get_purchased_items_cost():
	pr_items = frappe.db.sql("""select service_call, sum(base_net_amount) as amount
		from `tabPurchase Receipt Item` where ifnull(service_call, '') != ''
		and docstatus = 1 group by service_call""", as_dict=1)

	pr_item_map = {}
	for item in pr_items:
		pr_item_map.setdefault(item.service_call, item.amount)

	return pr_item_map

def get_issued_items_cost():
	se_items = frappe.db.sql("""select se.service_call, sum(se_item.amount) as amount
		from `tabStock Entry` se, `tabStock Entry Detail` se_item
		where se.name = se_item.parent and se.docstatus = 1 and ifnull(se_item.t_warehouse, '') = ''
		and ifnull(se.service_call, '') != '' group by se.service_call""", as_dict=1)

	se_item_map = {}
	for item in se_items:
		se_item_map.setdefault(item.service_call, item.amount)

	return se_item_map

def get_delivered_items_cost():
	dn_items = frappe.db.sql("""select dn.service_call, sum(dn_item.base_net_amount) as amount
		from `tabDelivery Note` dn, `tabDelivery Note Item` dn_item
		where dn.name = dn_item.parent and dn.docstatus = 1 and ifnull(dn.service_call, '') != ''
		group by dn.service_call""", as_dict=1)

	si_items = frappe.db.sql("""select si.service_call, sum(si_item.base_net_amount) as amount
		from `tabSales Invoice` si, `tabSales Invoice Item` si_item
		where si.name = si_item.parent and si.docstatus = 1 and si.update_stock = 1
		and si.is_pos = 1 and ifnull(si.service_call, '') != ''
		group by si.service_call""", as_dict=1)


	dn_item_map = {}
	for item in dn_items:
		dn_item_map.setdefault(item.service_call, item.amount)

	for item in si_items:
		dn_item_map.setdefault(item.service_call, item.amount)

	return dn_item_map
