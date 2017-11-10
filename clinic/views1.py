# from django.shortcuts import render
# from django.http import HttpResponse
# from django.http import HttpResponseRedirect
# from clinic.models import User
# from django.contrib import messages


# def login(request):
#     try:
#         if request.method == 'POST':
#             response = HttpResponse()
#             username = request.POST['username']
#             password = request.POST['password']
#             try:
#                 userlogin  = User.objects.get(user_login_id=username)
#                 if userlogin.user_password != password:
#                     messages.error(request, 'Mật khẩu không đúng! Xin vui lòng nhập lại.')
#                     return render(request, 'login.html')
#                 else:
#                     request.session['user_id'] = userlogin.user_id
#                     request.session['user_name'] = userlogin.user_name
#                     request.session['role'] = userlogin.user_role
#                     request.session['brand_id'] = userlogin.brand_id
#                     return HttpResponseRedirect(request,"index")
#             except Exception as e:
#                 messages.error(request, 'Có phát sinh lỗi hệ thống hoặc tài khoản này không tồn tại!')
#                 return render(request, 'login.html')
#         elif request.session.has_key('user_id') and request.session.has_key('user_name') and request.session['role']:
#             return HttpResponseRedirect(request,"index")
#     except Exception as e:
#         messages.error(request, 'Có phát sinh lỗi hệ thống hoặc tài khoản này không tồn tại!')
#         return render(request, 'login.html')
#     return render(request, 'login.html')

# def logout(request):
#     try:
#        del request.session['user_id']
#        del request.session['user_name']
#        del request.session['role']
#     except:
#        pass
#     return HttpResponseRedirect("/login")

# def crm_dentalclinic_overview(request):
#     return render(request,"clinic/crm_dentalclinic_overview.html")

# def crm_contactcenter_overview(request):
#     return render(request,"clinic/crm_contactcenter_overview.html")

# def crm_openchannel_overview(request):
#     return render(request,"clinic/crm_openchannel_overview.html")

# def crm_ordermanagement_overview(request):
#     return render(request,"clinic/crm_ordermanagement_overview.html")





# def calendar_index(request):
#     return render(request,"clinic/calendar_index.html")

# def inventory_index(request):
#     return render(request,"clinic/inventory_index.html")

# def hr_index(request):
#     return render(request,"clinic/hr_index.html")