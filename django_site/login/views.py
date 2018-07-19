from django.shortcuts import render
from django.shortcuts import redirect

from . import forms
from . import models
import hashlib


# Create your views here.

def leesang(request):
	return render(request, 'login/leesang.html')


def index(request):
	return render(request, 'login/index.html')


def login(request):
	#
	if request.session.get('is_login', ):
		return redirect("/index/")
	if request.method == "POST":
		login_form = forms.UserForm(request.POST)
		message = "请检查填写内容 ！"

		if login_form.is_valid():  # 表单类自带的is_valid()方法一步完成数据验证工作
			username = login_form.cleaned_data['username']
			password = login_form.cleaned_data['password']
			# username = username.strip()  # 通过strip()方法，将用户名前后无效的空格剪除；
			try:
				user = models.User.objects.get(name=username)
				if user.password == password:
					request.session['is_login'] = True
					request.session['user_id'] = user.id
					request.session['user_name'] = user.name
					return redirect('/index/')
				else:
					message = '密码错误~'
			except:
				message = '用户名不存在~'
		return render(request, 'login/login.html', locals())  # locals()函数，它返回当前所有的本地变量字典
	login_form = forms.UserForm()

	return render(request, 'login/login.html', locals())


def register(request):
	if request.session.get('is_login', None):
		# 登录状态不允许注册。你可以修改这条原则！
		return redirect("/index/")
	if request.method == "POST":
		register_form = forms.RegisterForm(request.POST)
		# message = "请检查填写的内容！"
		if register_form.is_valid():  # 获取数据
			username = register_form.cleaned_data['username']
			password1 = register_form.cleaned_data['password1']
			password2 = register_form.cleaned_data['password2']
			email = register_form.cleaned_data['email']
			sex = register_form.cleaned_data['sex']
			if password1 != password2:  # 判断两次密码是否相同
				message = "两次输入的密码不同！"
				return render(request, 'login/register.html', locals())
			else:
				same_name_user = models.User.objects.filter(name=username)
				if same_name_user:  # 用户名唯一
					message = '用户已经存在，请重新选择用户名！'
					return render(request, 'login/register.html', locals())
				same_email_user = models.User.objects.filter(email=email)
				if same_email_user:  # 邮箱地址唯一
					message = '该邮箱地址已被注册，请使用别的邮箱！'
					return render(request, 'login/register.html', locals())

				# 当一切都OK的情况下，创建新用户

				new_user = models.User()
				new_user.name = username
				new_user.password = hash_code(password1)
				new_user.email = email
				new_user.sex = sex
				new_user.is_delted = False
				new_user.save()
				return redirect('/login/')  # 自动跳转到登录页面
	register_form = forms.RegisterForm()
	return render(request, 'login/register.html', locals())


def logout(request):
	if not request.session.get('is_login', None):
		# 如果本来就未登录，也就没有登出一说
		return redirect("/index/")
	request.session.flush()
	# 或者使用下面的方法
	# del request.session['is_login']
	# del request.session['user_id']
	# del request.session['user_name']
	return redirect("/index/")


def hash_code(s, salt='mysite'):
	h = hashlib.sha256()
	s += salt
	h.update(s.encode())
	return h.hexdigrst()

