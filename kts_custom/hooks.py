# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "kts_custom"
app_title = "KTS Custom"
app_publisher = "KTS"
app_description = "Custom changes made to erpnext for Kustom Technology Solutions LLC"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "servadmin@kustomtech.net"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/kts_custom/css/kts_custom.css"
# app_include_js = "/assets/kts_custom/js/kts_custom.js"

# include js, css files in header of web template
# web_include_css = "/assets/kts_custom/css/kts_custom.css"
# web_include_js = "/assets/kts_custom/js/kts_custom.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "kts_custom.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "kts_custom.install.before_install"
# after_install = "kts_custom.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "kts_custom.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"kts_custom.tasks.all"
# 	],
# 	"daily": [
# 		"kts_custom.tasks.daily"
# 	],
# 	"hourly": [
# 		"kts_custom.tasks.hourly"
# 	],
# 	"weekly": [
# 		"kts_custom.tasks.weekly"
# 	]
# 	"monthly": [
# 		"kts_custom.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "kts_custom.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "kts_custom.event.get_events"
# }

