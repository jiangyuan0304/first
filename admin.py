from django.contrib import admin
# # 你需要知道的是那些操作，对应的会有哪些的改变，熟记于心
# # Register your models here.
# from .models import  Grades,Student
# #在创建班级的时候给你添加两个学生类
# class Studentinfo(admin.TabularInline):#创建关联对象以及显示的方式 admin.StackedInline页面显示不一样
#     model = Student
#     extra = 2
# #别忘了关联生成两个类还有下面的操作，别忘了
#
# #修改admin Grade的显示方式
# class GradeAdmin(admin.ModelAdmin):
#     inlines = [Studentinfo]#关联类对象，在创建Grades 的时候，来创建Student 的对象
#     # 列表页属性
#     #list_display 来定义这个表的显示的字段名称
#     list_display = ['gname','gdate','gnum','gfile','gimg','isDelete']
#     #在数据比较多的时候，可以根据list_filter来获取gname 相同的或者gdate 相同的数据体
#     list_filter = ['gname','gdate','gnum','isDelete']#过滤字段
#
#     search_fields = ['gname']#搜索字段
#     list_per_page =1#分页显示
#
#     #添加页面属性
#     #field 规定添加页面关于属性的先后顺序
#     #并且field 和fieldsets 两个属性不能同时使用
#     #fields = ['gname','gnum','gdate','isDelete']#规定属性的先后顺序 注意和fieldsets 不能同时使用
#     #对Grades的属性进行分组 分为了num  和base 两个分组
#     fieldsets = [("num",{"fields":['gname','gnum','gfile','gimg']}),
#                  ("base",{"fields":['gdate','isDelete']})]
#
# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     def ggsex(self):
#         if self.ggsex==True:
#             return "男"
#         else:
#             return "女"
#     ggsex.short_description = '性别'#设置页面列的名称
#
#     #self.ggdate.show_full_result_count = '日期'
#     list_display = ['ggname',ggsex,'ggage','gggrades','ggdate']
#     list_filter = ['ggname']  # 过滤字段
#     search_fields = ['ggage']  # 搜索字段
#     list_per_page = 2  # 分页显示
#
#     # 添加页面属性
#     # fields = ['gname','gnum','gdate','isDelete']#规定属性的先后顺序 注意和fieldsets 不能同时使用
#     fieldsets = [("base_info", {"fields": ['ggname', 'ggsex','ggage']}),
#                  ("simple_info", {"fields": ['ggdate', 'isDelete']}),
#                  ("IMPORT",{'fields':['gggrades']})]#一个页面可以分好几个部分来显示
#
#
#
# #操作执行动作
#     actions_on_top = False#直接等于的False 和True 不用加双引号
#     actions_on_bottom = True
#
# #注册到站点
# #这是第一步，需要你注册到站点管理 admin.site.register(Grades)
# #第二步是将对页面的显示处理添加到我们的站点管理里面来admin.site.register(GradesAdmin)
# admin.site.register(Grades,GradeAdmin)
# # admin.site.register(Student,StudentAdmin)
# #@admin.register(Student)

#
# from django.contrib import admin
# from myapp.models import Grades,Student
#
# class Studnetinfo(admin.TabularInline):
#     model = Student
#     extra = 1
#
#
#
# class GradesAdmin(admin.ModelAdmin):
#     inlines = [Studnetinfo]
#     list_display = ["pk","gname","gnum","gdate","lasttime","gfile","gimg"]
#     list_filter = ["gname",'gdate']
#     list_per_page = 2
#
#     fieldsets = [
#         ("基本的信息",{"fields":["gdate","gname","gfile","gimg"]})
#         ,("数量",{"fields":["gnum","isDelete"]})
#     ]
#
#
#
# class StudentAdmin(admin.ModelAdmin):
#     def sex(self):
#         if self.ggsex:
#             return "男"
#         else:
#             return "女"
#     Student.ggname.short_description = "姓名"
#     list_display = ["ggname","ggdate",sex,"ggage","isDelete","gggrades"]
#     list_filter = ["ggname"]
#     list_per_page = 2
#
#
#     fieldsets = [
#         ("基本的信息",{"fields":["ggname","ggdate","ggsex","ggage"]})
#         ,("数量",{"fields":["isDelete","gggrades"]})
#     ]
#
#
#
# admin.site.register(Grades,GradesAdmin)
# admin.site.register(Student,StudentAdmin)

from .models import  Share
admin.site.register(Share)

from .models import  User
admin.site.register(User)