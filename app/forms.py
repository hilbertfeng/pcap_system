#coding:UTF-8
__author__ = 'Hilbert'

from flask_wtf import Form
from flask_wtf.file import FileField
from app.get_file import GetField
from wtforms.validators import DataRequired, AnyOf


#上传表单
class Upload(Form):
    pcap = FileField('pcap', validators=[DataRequired()])

#协议过滤表单
class ProtoFilter(Form):
    value = FileField('value')
    filter_type = FileField('filter_type', validators=[DataRequired(), AnyOf([u'all', u'proto', u'ipsrc', u'ipdst'])])


# User find form
class UserFilter(Form):
    user_name = GetField('user_name')
    staff_no = GetField('staff_no')
    mobile_no = GetField('mobile_no')



