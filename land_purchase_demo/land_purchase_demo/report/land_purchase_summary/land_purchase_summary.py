# Copyright (c) 2013, kaviya and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
	columns, data = [], []
	if filters:
		columns = get_column()
		data = get_data(filters)
		if data:
			report_summary = get_report_summary(data)
			return columns, data, None, None, report_summary
	return columns, data

def get_column():
	columns = [
	{
	"label": "Document No",
	"fieldname": "document_no",
	"fieldtype": "Link",
	"options": "Land Purchase",
	"width": 150
	},
	{
	"label": "Seller Name",
	"fieldname": "seller_name",
	"fieldtype": "Data",
	"width": 150
	},
	{
	"label": "Contact No",
	"fieldname": "contact_no",
	"fieldtype": "Data",
	"width": 150
	},
	]
	return columns

def get_data(filters):
	data = frappe.db.sql("""select lp.name as document_no,
					lp.seller_name, lp.phone_number as contact_no
					from `tabLand Purchase` lp
					where lp.date 
					between %s and %s and lp.workflow_state = 'Senior Manager Approved'""",
					(filters['date'],filters['date']),  as_dict = True)
	return data

def get_report_summary(data):
		summary = []
		summary.append(
				{
				"value": len(data),
				"indicator": 'Green',
				"label": 'Ready for Process',
				"datatype": "Float",
			},
			)
		return summary