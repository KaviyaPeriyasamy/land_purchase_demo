// Copyright (c) 2016, kaviya and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Land Purchase Summary"] = {
	"filters": [
		{
			fieldname: "date",
			label: __("Date"),
			fieldtype: "Date",
			default: frappe.datetime.get_today(),
			reqd: 1
		}
	]
};
