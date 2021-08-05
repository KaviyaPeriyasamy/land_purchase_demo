from __future__ import unicode_literals
import frappe

def after_install():
	create_default_roles()
	create_workflow('Land Purchase')

def create_default_roles():
	roles = ['Purchase Officer','Manager','Senior Manager', 'CEO', 'CMO', 'CFO']
	for role in roles:
		if not frappe.db.exists('Role', role):
			role_doc = frappe.new_doc("Role")
			role_doc.role_name = role
			role_doc.save()

def create_workflow(document_name):
	#Create workflow state
	states_with_style = {'Success': ['Manager Approved','Senior Manager Approved'],
	'Danger': ['Manager Rejected', 'Senior Manager Rejected']}

	for style in states_with_style.keys():
		for state in states_with_style[style]:
			if not frappe.db.exists('Workflow State', state):
				frappe.get_doc({"doctype" : "Workflow State",
								"workflow_state_name" : state,
								"style" : style}).save()
	#Create default workflow
	if not frappe.db.exists('Workflow', f'{document_name} Workflow'):
		workflow_doc = frappe.get_doc({'doctype': 'Workflow',
				'workflow_name': f'{document_name} Workflow',
				'document_type': document_name,
				'workflow_state_field': 'workflow_state',
				'is_active': 1,
				'send_email_alert':0})

		workflow_doc.append('states',{'state': 'Pending',
					'doc_status': 0,
					'update_field': 'workflow_state',
					'update_value': 'Pending',
					'allow_edit': 'Purchase Officer'})

		pending_next_states = [['Approve', 'Manager Approved'], ['Reject', 'Manager Rejected']]
		for state in pending_next_states:
			workflow_doc.append('states',{'state': state[1],
						'doc_status': 0,
						'update_field': 'workflow_state',
						'update_value': state[1],
						'allow_edit': 'Manager'})
			transitions = { 'state': 'Pending',
							'action': state[0],
							'allow_self_approval': 0,
							'next_state': state[1],
							'allowed': 'Manager'}
			workflow_doc.append('transitions',transitions)	
		
		final_states = [['Approve', 'Senior Manager Approved']]
		for state in final_states:
			workflow_doc.append('states',{'state': state[1],
						'doc_status': 1,
						'update_field': 'workflow_state',
						'update_value': state[1],
						'allow_edit': 'Senior Manager'})
			transitions = { 'state': 'Manager Approved',
							'action': state[0],
							'allow_self_approval': 0,
							'next_state': state[1],
							'allowed': 'Senior Manager'}
			workflow_doc.append('transitions',transitions)	
		
		final_states = [['Reject', 'Senior Manager Rejected']]
		for state in final_states:
			workflow_doc.append('states',{'state': state[1],
						'doc_status': 0,
						'update_field': 'workflow_state',
						'update_value': state[1],
						'allow_edit': 'Senior Manager'})
			transitions = { 'state': 'Manager Approved',
							'action': state[0],
							'allow_self_approval': 0,
							'next_state': state[1],
							'allowed': 'Senior Manager'}
			workflow_doc.append('transitions',transitions)	
		workflow_doc.save()