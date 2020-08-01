# Copyright 2019 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields, api


class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'

    project_id = fields.Many2one(comodel_name='project.project', ondelete='restrict')
    create_project_from_equipment = fields.Boolean(
        default=True)
    preventive_default_task_id = fields.Many2one(string='Default Task', comodel_name='project.task')
    task_ids = fields.One2many(string='Task', comodel_name='project.task', inverse_name='equipment_id')
    task_count = fields.Integer(compute='_compute_task_count', string="Taches", store=True)

    @api.depends('task_ids')
    def _compute_task_count(self):
        for task in self:
            task.task_count = len(
                task.with_context(active_test=False).task_ids)

    @api.model
    def create(self, values):
        if values.get('create_project_from_equipment'):
            new_project = self.env['project.project'].create(
                self._prepare_project_from_equipment_values(values))
            values['project_id'] = new_project.id
        return super().create(values)

    def _prepare_project_from_equipment_values(self, values):
        """
        Default project data creation hook
        """
        return {
            'name': values.get('name'),
        }
