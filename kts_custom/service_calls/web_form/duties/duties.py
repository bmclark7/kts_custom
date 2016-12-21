from __future__ import unicode_literals

import frappe

def get_context(context):
	if frappe.form_dict.service_call:
		context.parents = [{'title': frappe.form_dict.service_call, 'route': '/service_calls?service_call='+ frappe.form_dict.service_call}]
		context.success_url = "/service_calls?service_call=" + frappe.form_dict.service_call
		
	elif context.doc and context.doc.get('service_call'):
		context.parents = [{'title': context.doc.service_call, 'route': '/service_calls?service_call='+ context.doc.service_call}]
		context.success_url = "/service_calls?service_call=" + context.doc.service_call
