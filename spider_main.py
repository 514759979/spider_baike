# -*- coding: utf-8 -*-

from spider_baidu import url_manager
from spider_baidu import html_downloader
from spider_baidu import html_parser
from spider_baidu import html_outputer

class SpiderMain(object):
    def __init__(self):
        self.urls       = url_manager.UrlManager()
        self.downloader = html_downloader.Downloader()
        self.parser     = html_parser.Htmlparser()
        self.outputer   = html_outputer.Outputer()

    def craw(self, root_url):
        self.urls.add_new_url(root_url)

        while self.urls.has_new_url():
            try:
                count = 1
                new_url = self.urls.get_new_url()
                print("craw %d") % count
                html_cont = self.downloader.download(new_url)
                new_url, new_data = self.html_parser.parser(new_url, html_cont)
                self.urls.add_new_urls(new_url)
                self.outputer.collect_data()

                if count == 1000:
                    break

                count = count + 1
            except:
                print("craw fail!")

        self.outputer.outputer_html()



if __name__ == "__main__":
    root_url   = "https://baike.baidu.com/item/Python/407313?fr=aladdin"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
