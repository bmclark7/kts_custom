# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "KTS Custom",
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("KTS Custom")
		},
		{
			"module_name": "Service Calls",
			"color": "orange",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("Service Calls")
		}
	]
