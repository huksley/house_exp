import frappe
from frappe import _
from frappe.utils import nowdate
import json

@frappe.whitelist(allow_guest=True)
def create_house_expense(title, amount, category, description, date=None ):
    """Create a new House Expense record"""
    try:
        # Create new document
        doc = frappe.new_doc("HouseExpense")
        doc.title = title
        doc.amount = amount
        doc.category = category
        doc.description = description
        doc.date = date or nowdate()
        doc.created_by = frappe.session.user
        
        # Insert the document
        doc.insert(ignore_permissions=True)
        
        return {
            "status": "success",
            "message": "House Expense created successfully",
            "data": doc.as_dict()
        }
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "House Expense Creation Failed")
        return {
            "status": "error",
            "message": str(e)
        }

@frappe.whitelist(allow_guest=True)
def get_house_expense(name):
    """Get a single House Expense record by name"""
    try:
        doc = frappe.get_doc("HouseExpense", name)
        return {
            "status": "success",
            "data": doc.as_dict()
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

@frappe.whitelist(allow_guest=True)
def get_all_house_expenses():
    """Get all House Expense records"""
    try:
        expenses = frappe.get_all("HouseExpense",
                                 fields=["name", "title", "amount", "category", "date", "description", "created_by"],
                                 order_by="creation desc")
        return {
            "status": "success",
            "data": expenses
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

@frappe.whitelist(allow_guest=True)
def update_house_expense(name, amount=None, category=None, description=None, date=None):
    """Update an existing House Expense record"""
    try:
        doc = frappe.get_doc("HouseExpense", name)
        
        if amount: doc.amount = amount
        if category: doc.category = category
        if description: doc.description = description
        if date: doc.date = date
        
        doc.save(ignore_permissions=True)
        
        return {
            "status": "success",
            "message": "House Expense updated successfully",
            "data": doc.as_dict()
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

@frappe.whitelist(allow_guest=True)
def delete_house_expense(name):
    """Delete a House Expense record"""
    try:
        frappe.delete_doc("HouseExpense", name, ignore_permissions=True)
        return {
            "status": "success",
            "message": "House Expense deleted successfully"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

# For guest access (if needed)
@frappe.whitelist(allow_guest=True)
def test_api():
    """Test API endpoint"""
    return {
        "status": "success",
        "message": "API is working",
        "user": frappe.session.user if frappe.session.user != "Guest" else "Guest User"
    }