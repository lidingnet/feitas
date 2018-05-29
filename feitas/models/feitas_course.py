# -*- coding: utf-8 -*-

from odoo import models, fields, api


class feitas_course(models.Model):
    _name= 'feitas.course'
    name= fields.Char(string= "名称", require= True)
    description= fields.Text(string= "介绍")
    manager_id= fields.Many2one('res.users', string= "负责人" , require= True)
    type= fields.Selection([('i','理论'),('e','实操'),('both','理论+实操')], string='课程类型',default= 'both', require= True)
    total_hours= fields.Float(string= '总课时', require= True, compute='_compute_total_hours')
    lesson_hours= fields.Float(string= '理论课时', require= True)
    exercise_hours= fields.Float(string= '实操课时', require= True)

    @api.multi
    @api.depends('lesson_hours','exercise_hours')
    def _compute_total_hours(self):
        self.total_hours= self.lesson_hours + self.exercise_hours