#**odoo11 study**
###目录结构
####models目录
*	存放所有的模型文件
*	新模型前缀为feitas. 例如：课程模型——feitas.course  文件名为 courses.py
*	扩展模型的文件命名用原来官方的命名。
####views目录
*	存放所有的视图文件，命名格式***_views.xml，其中***为与模型文件名相同
*	menu_actions.xml 专门用来存放菜单和动作的定义
*	multi_actions.xml 专门用来存放multi动作
*	templates.xml 专门用来存放模板
####data目录
*	存放数据文件，通常只有一个文件 data.xml
####controllers目录
*	存放控制器，通常只有一个文件  main.py
####security目录
*	权限与规则定义文件
####static目录
*	src等
####wizard目录
*	存放向导py和xml文件




