{
    "name": "Sale - Pay before Confirm",
    "version": "0.1",
    "description": """
    This module allows you to prevent orders from being confirmed unless you have created and paid (at least 1) advance invoice.
    """,
    "category": "Generic Modules/Sales & Purchases",
    "author": "Agaplan",
    "website": "http://www.agaplan.eu",
    "depends": [
        "sale",
    ],
    "init": [],
    "update_xml": [
        'sale_workflow.xml',
        'sale_view.xml',
    ],
    "demo": [],
    "test": [],
    "installable": True,
}
# vim:sts=4:et
