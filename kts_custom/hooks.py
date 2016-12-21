# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _
from . import __version__ as app_version

app_name = "kts_custom"
app_title = "KTS Custom"
app_publisher = "KTS"
app_description = "Custom modifications made for Kustom Technology Solutions LLC"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "servadmin@kustomtech.net"
app_license = "MIT"
source_link = "https://github.com/bmclark7/kts_custom.git"


# setup wizard
# boot_session = "erpnext.startup.boot.boot_session"
# notification_config = "erpnext.startup.notifications.get_notification_config"

# on_session_creation = "erpnext.shopping_cart.utils.set_cart_count"
# on_logout = "erpnext.shopping_cart.utils.clear_cart_count"

# website
# update_website_context = "erpnext.shopping_cart.utils.update_website_context"
# my_account_context = "erpnext.shopping_cart.utils.update_my_account_context"

email_append_to = ["Service Call"]

calendars = ["Service Call"]

# fixtures = ["Web Form"]

website_generators = ["Service Call"]

# website_context = {
#	"favicon": 	"/assets/erpnext/images/favicon.png",
#	"splash_image": "/assets/erpnext/images/splash.png"
# }

website_route_rules = [
	{"from_route": "/service_call", "to_route": "Service Call"},
]

portal_menu_items = [
	{"title": _("Service Calls"), "route": "/service_call", "reference_doctype": "Service Call"},
]

# default_roles = [
#	{'role': 'Customer', 'doctype':'Contact', 'email_field': 'email_id',
#		'filters': {'ifnull(customer, "")': ('!=', '')}},
#	{'role': 'Supplier', 'doctype':'Contact', 'email_field': 'email_id',
#		'filters': {'ifnull(supplier, "")': ('!=', '')}},
# ]

# has_website_permission = {
#	"Service Call": "kts_custom.service_calls.doctype.service_call.service_call.has_website_permission",
# }

# permission_query_conditions = {
# }

# has_permission = {
#	"Contact": "erpnext.utilities.address_and_contact.has_permission",
#	"Address": "erpnext.utilities.address_and_contact.has_permission"
# }

# dump_report_map = "erpnext.startup.report_data_map.data_map"

# before_tests = "erpnext.setup.utils.before_tests"

# standard_queries = {
#	"Service Call": "kts_custom.service_calls.doctype.service_call.service_call.get_service_call_list"
# }

# doc_events = {
# }

# scheduler_events = {
#	"hourly": [
#		"erpnext.controllers.recurring_document.create_recurring_documents"
#	],
#	"daily": [
#		"erpnext.stock.reorder_item.reorder_item",
#		"erpnext.setup.doctype.email_digest.email_digest.send",
#		"erpnext.support.doctype.issue.issue.auto_close_tickets",
#		"erpnext.controllers.accounts_controller.update_invoice_status",
#		"erpnext.accounts.doctype.fiscal_year.fiscal_year.auto_create_fiscal_year",
#		"erpnext.hr.doctype.employee.employee.send_birthday_reminders",
#		"erpnext.projects.doctype.task.task.set_tasks_as_overdue",
#		"erpnext.accounts.doctype.asset.depreciation.post_depreciation_entries"
#	]
# }


# get_translated_dict = {
#	("doctype", "Global Defaults"): "frappe.geo.country_info.get_translated_dict"
# }

# bot_parsers = [
#	'erpnext.utilities.bot.FindItemBot',
# ]

# get_site_info = 'erpnext.utilities.get_site_info'

# payment_gateway_enabled = "erpnext.accounts.utils.create_payment_gateway_and_account"
