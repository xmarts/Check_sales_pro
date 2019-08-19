# -*- coding: utf-8 -*-

from odoo import models, fields, api
from openerp.exceptions import UserError, RedirectWarning, ValidationError


# class check_sales(models.Model):
#     _name = 'check_sales.check_sales'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class chec_box(models.Model):
    _inherit = 'sale.order'

    Crear_proyect = fields.Boolean(string="Crear proyecto")

    def action_confirm(self): 
        if self.Crear_proyect == True:
            project_obj = self.env['project.project']
            project_values = {
                'name': self.name
                } 
            project_id = project_obj.create(project_values)
            if project_id:

                cr = self.env.cr
                sql = "INSERT INTO project_task_type_rel(type_id, project_id) VALUES(%s,%s)"

                project_task_type_obj = self.env['project.task.type']
                project_task_type_values = {
                    'name': 'Inicio del proyecto'
                }
                project_task_type_id = project_task_type_obj.create(project_task_type_values)

                if project_task_type_id:
                    datos = (project_task_type_id.id, project_id.id)
                    cr.execute(sql, datos)
                 
                project_task_type_obj2 = self.env['project.task.type']
                project_task_type_values2 = {
                    'name': 'Levantamiento lógico'
                }
                project_task_type_id2 = project_task_type_obj2.create(project_task_type_values2)

                if project_task_type_id:
                    datos2 = (project_task_type_id2.id, project_id.id)
                    cr.execute(sql, datos2)


                project_task_type_obj3 = self.env['project.task.type']
                project_task_type_values3 = {
                    'name': 'Levantamiento fisico'
                }
                project_task_type_id3 = project_task_type_obj3.create(project_task_type_values3)

                if project_task_type_id:
                    datos3 = (project_task_type_id3.id, project_id.id)
                    cr.execute(sql, datos3)

                
                project_task_type_obj4 = self.env['project.task.type']
                project_task_type_values4 = {
                    'name': 'Diseño de solución'
                }
                project_task_type_id4 = project_task_type_obj4.create(project_task_type_values4)

                if project_task_type_id:
                    datos4 = (project_task_type_id4.id, project_id.id)
                    cr.execute(sql, datos4)

                project_task_type_obj5 = self.env['project.task.type']
                project_task_type_values5 = {
                    'name': 'Implementación'
                }
                project_task_type_id5 = project_task_type_obj5.create(project_task_type_values5)

                if project_task_type_id:
                    datos5 = (project_task_type_id5.id, project_id.id)
                    cr.execute(sql, datos5)

                
                project_task_type_obj6 = self.env['project.task.type']
                project_task_type_values6 = {
                    'name': 'Transferencia / capacitación'
                }
                project_task_type_id6 = project_task_type_obj6.create(project_task_type_values6)

                if project_task_type_id:
                    datos6 = (project_task_type_id6.id, project_id.id)
                    cr.execute(sql, datos6) 

                project_task_type_obj7 = self.env['project.task.type']
                project_task_type_values7 = {
                    'name': 'Cierre del proyecto'
                }
                project_task_type_id7 = project_task_type_obj7.create(project_task_type_values7)

                if project_task_type_id:
                    datos7 = (project_task_type_id7.id, project_id.id)
                    cr.execute(sql, datos7) 

                project_task_type_obj8 = self.env['project.task.type']
                project_task_type_values8 = {
                    'name': 'Póliza de soporte'
                }
                project_task_type_id8 = project_task_type_obj8.create(project_task_type_values8)

                if project_task_type_id:
                    datos8 = (project_task_type_id8.id, project_id.id)
                    cr.execute(sql, datos8)
                return super(chec_box, self).action_confirm()              
        else:
            return super(chec_box, self).action_confirm()                           

                        
        


         


