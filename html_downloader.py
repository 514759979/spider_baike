# -*- coding: utf-8 -*-
import urllib.request

class Downloader(object):

    def download(self, url):
        if url is None:
            return

        resp = urllib.request.urlopen(url)

        if resp.getcode() != 200:
            print("[Error]:Getcode fail!")
            return None

        return resp.read()
