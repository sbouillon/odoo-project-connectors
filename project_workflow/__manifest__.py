# Copyright 2017 - 2018 Modoolar <info@modoolar.com>
# License LGPLv3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).

{
    "name": "Project Workflow",
    "summary": "This module provides workflow for project tasks",
    "category": "Project",
    "version": "16.0.1.0.0",
    "license": "LGPL-3",
    "author": "Odoo Community Association (OCA), Modoolar",
    "website": "https://www.modoolar.com/",
    "depends": [
        "project",
        "project_portal",
        "web_diagram_position",
        "web_ir_actions_act_multi",
        "web_ir_actions_act_view_reload",
        "website",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/project_workflow.xml",
        "views/project_workflow_views.xml",
        "views/portal_templates.xml",
        "wizard/stage_change_confirmation_wizard.xml",
        "wizard/workflow_import_wizard.xml",
        "wizard/workflow_export_wizard.xml",
        "wizard/workflow_edit_wizard.xml",
        "wizard/workflow_mapping_wizard.xml",
        "wizard/project_apply_workflow_wizard.xml",
    ],
    "images": [],
    "qweb": ["static/src/xml/diagram.xml", "static/src/xml/base.xml",],
}
