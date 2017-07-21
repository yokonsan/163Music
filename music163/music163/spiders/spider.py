# -*- coding: utf-8 -*-
from scrapy import Spider, Request


class MusicSpider(Spider):
    name = "music"
    allowed_domains = ["163.com"]
    artist_url = 'https://music.163.com/discover/artist/'
    ids = ['1001','1002','1003','2001','2002','2003','6001','6002','6003','7001','7002','7003','4001','4002','4003']
    initials = [i for i in range(65, 91)]+[0]

    def start_requests(self):
        for id in self.ids:
            for initial in self.initials:
                url = '{url}cat?id={id}&initial={initial}'.format(url=self.artist_url,id=id,initial=initial)
                yield Request(url, callback=self.parse_artist)

    def parse_artist(self, response):
        print(response.text)

