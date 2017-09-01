# -*- coding: utf-8 -*-
import urllib2

class Downloader(object):

    def download(self, url):
        if url is None:
            return

        resp = urllib2.urlopen(url)

        if resp.getcode() != 200:
            return None

        return resp.read()
