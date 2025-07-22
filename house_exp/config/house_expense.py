from frappe import _

def get_data():
    return [
        {
            "module_name": "House Expense",
            "type": "module",
            "label": _("House Expense")
        },
        {
            "label": _("House Expense API"),
            "icon": "octicon octicon-file-directory",
            "items": [
                {
                    "type": "page",
                    "name": "house-expense-api",
                    "label": _("House Expense API Docs"),
                    "description": _("API documentation for House Expense")
                }
            ]
        }
    ]