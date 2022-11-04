import requests
import json
import base64
import os
import sys
import getopt
#守卫者安全 fofa查询爬虫脚本
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
}
   
def fofaspider(pages,fullurl):
    if os.path.exists("fofa查询结果.txt"): 
        f = open("fofa查询结果.txt", 'w') 
        f.truncate()   #先清除现有文件的内容
    with open("fofa查询结果.txt", 'a') as f:
        f.write('fofa查询结果如下：'+"\n")
        for i in range(1,pages+1):  #遍历页数
            fullurl=fullurl+'&page='+str(i)
            response = requests.get(fullurl,headers=headers).text
            j=json.loads(response)  #将爬取结果由json格式转化为列表格式
            results=j['results']    #单独读取返回具体结果
            if results !=[]:                      
                    for page in results:
                        f.write('[+]第'+str(i)+'页第'+str(results.index(page)+1)+'条：'+page[0] + "\n") 
                    f.write('\n')                   
                    print('第'+str(i)+'页查询完毕，结果已写入！！！')
            else:
                print('第'+str(i)+'页不存在！！！')
        f.close()
        print('*'*8+'查询完毕！'+'*'*8)
        

if __name__ == '__main__':
    print('')    
    q = input('请输入关键字,如 "app="xxx" && country="CN"等等：')
    pages = int(input("请输入查询的页数："))
    email = input("请输入你的email：")
    api=input("请输入你的api：")
    q=base64.b64encode(q.encode('utf-8')).decode("utf-8")
    fullurl='https://fofa.info/api/v1/search/all?email='+email+'&key='+api+'&qbase64='+q
    print('*'*8+'开始查询！'+'*'*8)
    fofaspider(pages,fullurl)
