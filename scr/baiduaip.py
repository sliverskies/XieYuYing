# import urllib, sys
# import urllib.request
# import ssl

# # client_id 为官网获取的AK， client_secret 为官网获取的SK   现在这个模块暂时用不到
# host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=G1G94LhsYYQj8shzjFtNQjLI&client_secret=G3ox550tETG34F9ZcduqbiHTLDd65IoZ'
# request = urllib.request.Request(host)
# request.add_header('Content-Type', 'application/json; charset=UTF-8')
# response = urllib.request.urlopen(request)
# content = response.read()
# if (content):
#     print(content)


from aip import AipNlp
#情感倾向分析,,返回值是个字典,调用字典的key:sentiment 来判断是好的还是坏的,就行了
""" 你的 APPID AK SK """
APP_ID = '11553722'
API_KEY = 'oibkBOpvGpuSHCbRqv3W2AjN'
SECRET_KEY = '1GpZltLF6kod3dkleGEChq5Aqe999PFo'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
# Your_select = "苹果是一家伟大的公司"
# res = client.sentimentClassify(Your_select)['items'][0]['sentiment']
# print(res)
'''
参数	是否必须	类型	说明
text	是	string	输入的文本内容
items	是	array	输入的词列表
+sentiment	是	number	表示情感极性分类结果, 0:负向，1:中性，2:正向
+confidence	是	number	表示分类的置信度
+positive_prob	是	number	表示属于积极类别的概率
+negative_prob	是	number	表示属于消极类别的概率

'''