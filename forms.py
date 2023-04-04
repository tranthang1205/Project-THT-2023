from flask_wtf import FlaskForm
import wtforms as forms

class LoginForm(FlaskForm):
    username = forms.StringField('Name')
    email = forms.EmailField('Email')
    password = forms.PasswordField('Pass')
    school = forms.StringField('School')
    graded = forms.BooleanField('Đã tốt nghiệp hay chưa')
    point = forms.FloatField('Điểm')
    date = forms.DateField('Thời gian vào trường')
