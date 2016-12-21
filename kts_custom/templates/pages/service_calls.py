# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
import json

def get_context(context):
	service_call_users = frappe.db.get_value("Service Call Users", {"parent": frappe.form_dict.service_call, "user": frappe.session.user} , "user")
	if not service_call_users or frappe.session.user == 'Guest': 
		raise frappe.PermissionError
		
	context.no_cache = 1
	context.show_sidebar = True
	service_call = frappe.get_doc('Service Call', frappe.form_dict.service_call)

	service_call.has_permission('read')
	
	service_call.tasks = get_tasks(service_call.name, start=0, item_status='open',
		search=frappe.form_dict.get("search"))

	service_call.timesheets = get_timesheets(service_call.name, start=0,
		search=frappe.form_dict.get("search"))


	context.doc = service_call


def get_tasks(service_call, start=0, search=None, item_status=None):
	filters = {"service_call": service_call}
	if search:
		filters["subject"] = ("like", "%{0}%".format(search))
	# if item_status:
# 		filters["status"] = item_status
	tasks = frappe.get_all("Task", filters=filters,
		fields=["name", "subject", "status", "_seen", "_comments", "modified", "description"],
		limit_start=start, limit_page_length=10)

	for task in tasks:
		task.todo = frappe.get_all('ToDo',filters={'reference_name':task.name, 'reference_type':'Task'},
		fields=["assigned_by", "owner", "modified", "modified_by"])

		if task.todo:
			task.todo=task.todo[0]
			task.todo.user_image = frappe.db.get_value('User', task.todo.owner, 'user_image')

		
		task.comment_count = len(json.loads(task._comments or "[]"))

		task.css_seen = ''
		if task._seen:
			if frappe.session.user in json.loads(task._seen):
				task.css_seen = 'seen'

	return tasks

@frappe.whitelist()
def get_task_html(service_call, start=0, item_status=None):
	return frappe.render_template("erpnext/templates/includes/service_calls/service_call_tasks.html",
		{"doc": {
			"name": service_call,
			"service_call_name": service_call,
			"tasks": get_tasks(service_call, start, item_status=item_status)}
		}, is_path=True)

def get_timesheets(service_call, start=0, search=None):
	filters = {"service_call": service_call}
	if search:
		filters["activity_type"] = ("like", "%{0}%".format(search))

	timesheets = frappe.get_all('Timesheet Detail', filters=filters,
	fields=['service_call','activity_type','from_time','to_time','parent'],
	limit_start=start, limit_page_length=10)
	for timesheet in timesheets:
		timesheet.infos = frappe.get_all('Timesheet', filters={"name": timesheet.parent},
			fields=['name','_comments','_seen','status','modified','modified_by'],
			limit_start=start, limit_page_length=10)

		for timesheet.info in timesheet.infos:
			timesheet.info.user_image = frappe.db.get_value('User', timesheet.info.modified_by, 'user_image')

			timesheet.info.comment_count = len(json.loads(timesheet.info._comments or "[]"))

			timesheet.info.css_seen = ''
			if timesheet.info._seen:
				if frappe.session.user in json.loads(timesheet.info._seen):
					timesheet.info.css_seen = 'seen'		
	return timesheets

@frappe.whitelist()
def get_timesheet_html(service_call, start=0):
	return frappe.render_template("erpnext/templates/includes/service_calls/service_call_timesheets.html",
		{"doc": {"timesheets": get_timesheets(service_call, start)}}, is_path=True)

