# Copyright 2017 - 2018 Modoolar <info@modoolar.com>
# License LGPLv3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).

from odoo import models, fields, api


class ProjectType(models.Model):
    _inherit = "project.type"
    _implements_syncer = True

    task_type_ids = fields.Many2many(
        comodel_name="project.task.type2", scrummer=True
    )


class Project(models.Model):
    _inherit = "project.project"

    image_key = fields.Char(scrummer=True)
    write_date = fields.Datetime(scrummer=True)
    todo_estimation = fields.Integer(scrummer=True)
    in_progress_estimation = fields.Integer(scrummer=True)
    done_estimation = fields.Integer(scrummer=True)
    default_task_type_id = fields.Many2one(
        comodel_name="project.task.type2", scrummer=True
    )

    
    def open_in_scrummer(self):
        self.ensure_one()
        url = "/scrummer/web#page=board&project=%s&view=%s"
        return {
            "type": "ir.actions.act_url",
            "target": "self",
            "url": url % (self.id, self.agile_method),
        }


class AnalyticAccount(models.Model):
    _inherit = "account.analytic.account"

    name = fields.Char(scrummer=True)
