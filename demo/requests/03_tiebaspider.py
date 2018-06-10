# coding=utf-8
import requests
class TiebaSPider:
    def __init__(self,tieba_name):
        self.tieba_name = tieba_name
        self.url_temp = "https://tieba.baidu.com/f?kw="+tieba_name+"&ie=utf-8&pn={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}

    # 1.url list
    def get_url_list(self):
        # url_list = []
        # for i in range(1000):
        #     url = self.url_temp.format(i*50)
        #     url_list.append(url)
        url_list = [self.url_temp.format(i*50) for i in range(1000)]
        return url_list

    def parse_url(self,url):#发送请求，获取响应
        print("现在正在请求：",url)
        r = requests.get(url,headers=self.headers)
        return r.content.decode()

    def save_html_str(self,html_str,page_number):
        file_path = "{}_第{}页.html".format(self.tieba_name,page_number)
        with open(file_path,"w",encoding="utf-8") as f:
            f.write(html_str)
        print("保存成功")

    def run(self):#实现我们的主要逻辑
        #1.url list
        url_list = self.get_url_list()
        #2.遍历url，发送请求，获取响应
        for url in url_list:
            html_str = self.parse_url(url)
             #3.保存
            page_number = url_list.index(url)+1
            self.save_html_str(html_str,page_number)

if __name__ == '__main__':
    tieba_spider = TiebaSPider("李毅")
    tieba_spider.run()