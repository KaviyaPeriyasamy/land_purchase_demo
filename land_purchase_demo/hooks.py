from . import __version__ as app_version

app_name = "land_purchase_demo"
app_title = "Land Purchase Demo"
app_publisher = "kaviya"
app_description = "Frappe based custom application to handle land purchase-related workflow"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "kaviyaperiyasamy22@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/land_purchase_demo/css/land_purchase_demo.css"
# app_include_js = "/assets/land_purchase_demo/js/land_purchase_demo.js"

# include js, css files in header of web template
# web_include_css = "/assets/land_purchase_demo/css/land_purchase_demo.css"
# web_include_js = "/assets/land_purchase_demo/js/land_purchase_demo.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "land_purchase_demo/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "land_purchase_demo.install.before_install"
# after_install = "land_purchase_demo.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "land_purchase_demo.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
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
# 		"land_purchase_demo.tasks.all"
# 	],
# 	"daily": [
# 		"land_purchase_demo.tasks.daily"
# 	],
# 	"hourly": [
# 		"land_purchase_demo.tasks.hourly"
# 	],
# 	"weekly": [
# 		"land_purchase_demo.tasks.weekly"
# 	]
# 	"monthly": [
# 		"land_purchase_demo.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "land_purchase_demo.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "land_purchase_demo.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "land_purchase_demo.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"land_purchase_demo.auth.validate"
# ]

