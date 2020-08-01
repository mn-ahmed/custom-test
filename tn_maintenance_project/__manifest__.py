# Copyright 2019 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    'name': 'Maintenance Projects task',
    "summary": "Adds projects and list of tasks to maintenance equipments and requests",
    "version": "12.0.1.0.0",
    "author": "Odoo Community Association (OCA), Ahmed",
    'license': 'AGPL-3',
    "category": "Maintenance",
    "website": "",
    "depends": [
        "project",
        "maintenance",

    ],
    "data": [
        "security/maintenance_project_security.xml",
        "views/project_project_views.xml",
        "views/maintenance_equipment_views.xml",
        "views/maintenance_request_views.xml",

    ],
    "demo": [
        "data/demo_maintenance_project.xml",
    ],
    'installable': True,
}
