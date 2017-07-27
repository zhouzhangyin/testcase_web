# testcase_web 
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="知识共享许可协议" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />本作品采用<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">知识共享署名 4.0 国际许可协议</a>进行许可。
***
自动化测试用例web管理页面
## 前言
在自动化测试，一项重要的工作就是自动化测试用例的管理和维护，一套成熟的自动化测试框架包含：自动化测试脚本框架+自动化测试用例管理，只有将自动化测试用例规范的管理和维护起来，才能在需求变动时，可以很快的的去更新测试用例，让自动化测试不在因为修改测试用例繁琐成为头疼的问题
## 设计
- 采用python+Django框架，搭建web应用，用于测试用例的展示
- 功能：
  1. 前端展示测试用例信息，只允许查看
  2. 可自定义用例模板，目前用例模板包含：接口自动化测试用例、App自动化测试用例、web自动化测试用例
  3. 后端管理界面可进行编辑和新增测试用例
  4. 可以直接导入导出xls格式的测试用例数据
  5. 支持在页面中直接运行接口测试用例
  6. 支持用户权限管理
## 版本
python 2.7 + Django 1.9.7 + xadmin 0.6.1 + MySql 5.7

* [Django]-pythonWeb框架，用于快速搭建blog，自带管理后台（界面比较难看，功能少，不可扩展）
* [xadmin]-Django后台管理页面升级版，界面展示美观，可自定义插件，功能可扩展

## 截图
![](https://cl.ly/k3wX/WX20170418-182035.png)


[Django]:<https://github.com/django/django.git>
[xadmin]:<https://github.com/sshwsfc/xadmin>

