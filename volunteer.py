# conding:utf-8
import requests,urllib.request
from lxml import html,etree
from bs4 import BeautifulSoup
import re
#url = 'http://www.baobeihuijia.com/list.aspx?tid=1&sex=&photo=&page=2'
# csvFile = open("C:/Users/TOMORROW/Desktop/present/try.csv", 'w+', newline="")
# csvFile.write(codecs.BOM_UTF8)
def paqu():
    resp = requests.get('https://gz.izyz.org/mission/detail.do?missionId=2323328')
    str_html = resp.text
    tree = etree.HTML(str_html)
    node=[]
    #活动主题
    title = tree.xpath('/html/body/section/div[1]/h1/text()')
    node.append(title[0])
    #活动类型
    leixing = tree.xpath('/html/body/section/div[1]/div/div[1]/div/span[1]/text()')
    node.append(leixing[0])
    #发布组织
    station = tree.xpath('/html/body/section/div[1]/div/div[1]/div/span[3]/text()')
    node.append(station[0])
    #活动图片
    img = tree.xpath('/html/body/section/div[2]/div[1]/div[1]/div[1]/img/@src')
    node.append(img[0])
    #活动时间
    time = tree.xpath('/html/body/section/div[2]/div[1]/div[1]/div[2]/p[2]/text()')
    node.append(time[0])
    #联系方式
    link1 = tree.xpath('/html/body/section/div[2]/div[1]/div[1]/div[3]/p[2]/text()')
    link2 = tree.xpath('/html/body/section/div[2]/div[1]/div[1]/div[3]/p[3]/text()')
    node.append(link1[0])
    node.append(link2[0])
    #地址
    address = tree.xpath('/html/body/section/div[2]/div[1]/div[1]/div[4]/p[2]/text()')
    add = tree.xpath('/html/body/section/div[2]/div[1]/div[1]/div[4]/p[2]/button/@onclick')[0]
    add = add.encode('utf-8')
    add = add.decode('utf8')
    aaa =re.findall('[0-9.]+',add)
    print(aaa[0],aaa[1])
    node.append(address[0])
    #活动简介
    instruction = tree.xpath('/html/body/section/div[2]/div[1]/div[1]/div[5]/p[2]/text()')
    node.append(instruction[0])
    #服务内容
    content = tree.xpath('/html/body/section/div[2]/div[1]/div[1]/div[6]/p[2]/text()')
    node.append(content[0])
    #服务要求
    need = tree.xpath('/html/body/section/div[2]/div[1]/div[1]/div[7]/p[2]/text()')
    node.append(need[0])
    #招募人数
    num_person = tree.xpath('/html/body/section/div[2]/div[2]/div[1]/div[2]/a[2]/p[2]/text()')
    node.append(num_person[0])
    # writer = csv.writer(csvFile)

    # try:
    #     writer.writerow(node)
    # except:
    #     print('有错')
paqu()
