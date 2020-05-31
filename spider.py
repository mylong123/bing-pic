import json
from requests import get
import re

def GetPic():
    api_url = r'https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'
    api = get(api_url)
    # json_data =  str(json.loads(api.text))
    json_data = json.loads(api.text)
    # 获取图片地址
    pic_url = r'https://www.bing.com{0}'.format(json_data['images'][0]['url'])
    #获取时间信息
    start_date = json_data['images'][0]['startdate']
    #获取标题
    title_date = json_data['images'][0]['copyright']
    title_date = re.sub('\(©', '-', title_date)
    title_date = re.sub('/Minden Pictures\)', '', title_date)
    # 获取MD文本url
    permalink = json_data['images'][0]['fullstartdate']
    # open(r'./json/{0}.json'.format(start_date), 'wb').write(api.content)
    print('Create Json Success!')
    pic = get(pic_url, stream=True)
    if(pic.status_code == 200):
        # open(r'./pic/{0}.png'.format(start_date), 'wb').write(pic.content)
        catemd(title_date,permalink,start_date)
        print('Create Image Success!')
    else:
        print('Create Image Faild!')

def catemd(title_date,permalink,start_date):
    str = '---\n' \
          'title: ' + title_date + '\n' \
          'permalink: ' + permalink + '\n' \
          'date: ' + start_date + '\n' \
          'categories: \n' \
          '  - 每日一图\n' \
          '  - 桌面背景\n' \
          'tags: \n' \
          '  - 每日一图\n' \
          '  - 桌面图片\n' \
          '  - 图片\n' \
          '  - 风景\n' \
          '---\n' \
          '![' + permalink + '](https://cdn.jsdelivr.net/gh/mylong123/bing-pic/pic/' + start_date + '.png)\n' \
          + title_date +'图片分享，每日一图每天提供不一样的风景图片，仅供参考，下载作为桌面壁纸使用'

    open(r'./md/{0}pic.md'.format(start_date), 'wb').write(str.encode())
    print('Create md Success!')

if __name__ == "__main__":
    GetPic()