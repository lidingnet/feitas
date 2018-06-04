# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

from odoo import tools, _
from odoo.modules.module import get_module_resource


class feitas_course(models.Model):
    _name= 'feitas.course'
    name= fields.Char(string= "名称", required= True)
    description= fields.Text(string= "介绍")
    manager_id= fields.Many2one('res.users', string= "负责人" , required= True)
    type= fields.Selection([('i','理论'),('e','实操'),('both','理论+实操')], string='课程类型',default= 'both', required= True)
    total_hours= fields.Float(string= '总课时', required= True, compute='_compute_total_hours')
    lesson_hours= fields.Float(string= '理论课时', required= True)
    exercise_hours= fields.Float(string= '实操课时', required= True, help='实操课时只允许填写3或者4的倍数')
    state= fields.Selection( [('0','草稿'), ('1','审核中'), ('2','审批中'), ('3','退回'),('4','已批')] , string= '状态', default= '0')

    @api.multi
    @api.depends('lesson_hours','exercise_hours')
    def _compute_total_hours(self):
        for item in self:
            item.total_hours= item.lesson_hours + item.exercise_hours

    _sql_constraints = [
        ('name_unique',
         'UNIQUE(name)',
        '课程名称不能重复!!!'),
        ('lesson_hours_nozero',
         'check(lesson_hours>0)',
         '理论课时数必须大于零'),
        ('exercise_hours_nozero',
         'check(exercise_hours>0)',
         '理论课时数必须大于零')
    ]

    # 实操课时只允许填写3或者4的倍数
    @api.constrains('exercise_hours')
    def _check_exercise_hours(self):
        if(self.exercise_hours%3 !=0 and self.exercise_hours%4 != 0):
            raise ValidationError("实操课时只允许填写3或者4的倍数!!!!")


    def _check_course_hourse(self, vals):
        # 课程数量检查
        if self.search_count([('manager_id','=',vals.get('manager_id',0))]) >= 3:
            raise ValidationError("同一个用户不能负责3门以上的课程")

        # 课时检查
        # 将要保存的本课程负责人ID
        current_manager_id= vals.get('manager_id', self['manager_id']['id'])
        # 将要保存的本课程的 理论课时
        all_of_lesson_hours= vals.get('lesson_hours', self['lesson_hours'])
        all_of_total_hours= vals.get('lesson_hours', self['lesson_hours'])+ vals.get('exercise_hours', self['exercise_hours'])
        # 除了本课程，其他所有课程，此负责人课程集合
        all_of_other_curse = self.search([ ('id', '!=', self['id']), ('manager_id','=',current_manager_id)])
        # 此负责人将要承担理论课时数
        for item in all_of_other_curse:
            all_of_lesson_hours += item['lesson_hours']
            all_of_total_hours += item['lesson_hours'] + item['exercise_hours']
        print(str(current_manager_id) + ':'+ str(all_of_lesson_hours))
        if all_of_lesson_hours > 100:
            raise ValidationError('同一人所负责课程理论课时数不能大于100')
        if all_of_total_hours >200:
            raise ValidationError('同一人所负责课程总课时不能大于200')

    @api.multi
    def write(self, vals):
        # 课程数量/课时检查
        self._check_course_hourse(vals)
        # 执行保存
        return super(feitas_course, self).write(vals)

    @api.model
    def create(self, vals):
        # 课程数量/课时检查
        self._check_course_hourse(vals)
        # 执行创建
        return super(feitas_course, self).create(vals)

    # 提交按钮调用该方法，课程单据状态由草稿改为审核中
    def btn_submit(self):
        self.state= '1'

    # 审核按钮调用该方法，课程单据状态由审核中改为审批中
    def btn_approve_one(self):
        self.state= '2'

    # 审批按钮调用该方法，课程单据状态由审批中改为已通过。
    def btn_approve_second(self):
        self.state = '4'

    # 审核或审批过程中，点击打回按钮调用该方法，课程单据状态由审核中 / 审批中改为被打回。
    def btn_approve_refuse(self):
        self.state = '3'

