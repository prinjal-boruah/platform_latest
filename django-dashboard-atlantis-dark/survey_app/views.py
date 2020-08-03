# from django.shortcuts import render
# from django.http import HttpResponse
# from limesurveyrc2api import LimeSurveyRemoteControl2API as LimeSurvey
# import base64,io, urllib
# import json
# import PyPDF2
# import slate3k as slate
# from tablib import Dataset
# from rest_framework.views import APIView
# from rest_framework.response import Response
# import matplotlib.pyplot as plt
# import time

# def survey(request):
#     return render(request, 'survey.html')


# class GetData(APIView):

#     def get(self, request):
#         url = "http://106.51.37.192:8000/ME_Survey/index.php/admin/remotecontrol"
#         username = "admin"
#         password = "admin123"

#         api = LimeSurvey(url=url)

#         session_key = api.sessions.get_session_key(username=username, password=password)

#         result = api.surveys.list_surveys(session_key=session_key['result'], username=username)

#         ### export_responses = api.respond.list_res(session_key=session_key['result'], survey_id="953879", document_type="json")
#         stats = api.statistics.list_stats(session_key=session_key['result'], survey_id="953879", document_type="xls")
#         ### print("TYPE ", type(stats['result']))
#         ### print("TYPE ", stats['result'])

#         ### decoded_export_responses = base64.b64decode(export_responses['result'])
#         decoded_stats = base64.b64decode(stats['result'])

#         ### encoding = 'utf-8-sig'
#         ### string_data = decoded_export_responses.decode(encoding)

#         ### print(decoded_stats)

#         f = open('filessss.xls', 'wb')
#         f.write(decoded_stats)
#         f.close()

#         dataset = Dataset()
#         g = open('filessss.xls', 'rb')
#         any_data = g.read()
#         g.close()
#         imported_data = dataset.load(any_data)

#         data = []
#         for i in imported_data:
#             data.append(list(i))
#         ### print(data)
#         return Response(data)

# ### def plots(request,lit):
# def plots(request):
#     viewfn = GetData.as_view()
#     response = viewfn(request)

#     new_list2 = [x for x in response.data if x != ['Answer', 'Count', 'Percentage']]
#     indices = [i for i, x in enumerate(new_list2) if x == ['', '', '']]

#     ques_list = []
#     i = 0
#     for x in indices:
#         try:
#             ques_list.append(new_list2[indices[i]+1:indices[i+1]])
#         except IndexError:
#             ques_list.append(new_list2[indices[i]+1:])
#         i+=1

#     ### print(ques_list)
#     ques_with_label = []
#     for q in ques_list:
#         whole_ques = []
#         if len(q) != 0:
#             whole_ques.append(q[1][0])
#             y = q[2:len(q)+1]
#             x_axis = []
#             y_axis = []
#             for z in y:
#                 x_axis.append(z[0])
#                 y_axis.append(z[1])
#             whole_ques.append(x_axis)
#             whole_ques.append(y_axis)
#         if len(whole_ques) != 0:
#             ques_with_label.append(whole_ques)

#     ### print(ques_with_label)

#     title_list = [ x[0] for x in ques_with_label]
#     y_list = [ x[1] for x in ques_with_label]
#     x_list = [ x[2] for x in ques_with_label]

#     len_list = len(x_list)
#     i = 1
#     plt.figure(figsize=(10,8))
#     for x in range(0,len_list):
#         plot_num = str(len_list) + "1" + str(i)
#         print("plot_pos ========== ",plot_num)

#         plt.subplot(int(plot_num))
#         plt.title(title_list[i-1])
#         plt.bar(y_list[i-1], x_list[i-1])
#         i+=1

#     plt.tight_layout()
#     fig = plt.gcf()
#     ###convert graph into dtring buffer and then we convert 64 bit code into image
#     buf = io.BytesIO()
#     fig.savefig(buf,format='png')
#     buf.seek(0)
#     string = base64.b64encode(buf.read())
#     uri =  urllib.parse.quote(string)
#     plt.close()
#     return render(request,'plot.html',{'data':uri})