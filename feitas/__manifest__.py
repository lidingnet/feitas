# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# 描述模块一些信息
{
    'name' : 'Feitas ',
    #'version' : 0.1,
    'summary': 'Feitas Course',
    'sequence': 2,
    'description': """
        odoo study by feitas
    """,
    # 'category': 'Accounting',
    'website': 'feitas.com',
    'images' : [],
    'depends' : ['web'],
    # 注意data中的文件顺序，ref的ID对应的record一定要在前面
    # 不理解的看views.xml中的action和menuitem的定义顺序
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/menu_actions.xml',
        'views/course_views.xml',
        'views/course_log_views.xml',
        'data/feitas_course_log_no.xml'
    ],
    'demo': [
    ],
    'qweb': [
    ],
    # 'installable': True,
    'application': True,
    # 'auto_install': False,
    # 'post_init_hook': '_auto_install_l10n',
}
