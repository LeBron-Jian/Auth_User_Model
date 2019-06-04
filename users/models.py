from django.db import models

# Create your models here.
from django.contrib.auth.models import User

'''
 这里我们自定义的UserProfile模型有三个字段
 1，user 与User是1对1 的关系
 2，org 用户名
 3，telephone 电话
 4， mod_date：最后修改日期，系统自动生成
'''

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile')
    # 模型类中设置:blank=True,表示代码中创建数据库记录时该字段可传空白(空串,空字符串)
    org = models.CharField('Organization', max_length=128, blank=True)
    telephone = models.CharField('Telephone', max_length=50, blank=True)
    mod_data = models.DateTimeField('Last modified', auto_now=True)

    class Meta:
        verbose_name = 'User profile'

    def __str__(self):
        # return self.user.__str__()
        return "{}".format(self.user.__str__())


