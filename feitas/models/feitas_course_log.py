# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class feitas_course_log(models.Model):
    _name= 'feitas.course.log'
    name= fields.Char(string= "编号",  readonly=True)
    course_id = fields.Many2one('feitas.course', string= '课程',  ondelete='cascade', required= True )
    start_date = fields.Date(String= '开始日期', required= True)
    seats= fields.Integer(String= '座位数', required= True)
    partner_ids= fields.Many2many( 'res.partner',String= '学员')

    def btn_open_course_log(self):
        print('...........')

    # 自动编号
    @api.model
    def create(self, vals):
        if not vals.get('name'):
            vals['name'] = self.env['ir.sequence'].next_by_code('feitas.course.log.no') or '/'

        return super(feitas_course_log, self).create(vals)