# -*- coding: utf-8 -*-

# Scrapy settings for music163 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'music163'

SPIDER_MODULES = ['music163.spiders']
NEWSPIDER_MODULE = 'music163.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'music163 (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie':'_ntes_nuid=5e2135ea19041c08d61bddbb9009de63; _ntes_nnid=a387121ca9ed891dca82492f6c088c57,1483420952257; __utma=187553192.690483437.1489583101.1489583101.1489583101.1; __utmz=187553192.1489583101.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __oc_uuid=ff821060-097f-11e7-8c2a-73421a9a1bc4; mail_psc_fingerprint=032ad52396a72877e07f21386dee35a2; NTES_CMT_USER_INFO=106964635%7C%E6%9C%89%E6%80%81%E5%BA%A6%E7%BD%91%E5%8F%8B06o2qr%7Chttps%3A%2F%2Fsimg.ws.126.net%2Fe%2Fimg5.cache.netease.com%2Ftie%2Fimages%2Fyun%2Fphoto_default_62.png.39x39.100.jpg%7Cfalse%7CbTE1MTUyMzQ3Mjc3QDE2My5jb20%3D; usertrack=c+5+hlkgTIMgjwa+EDUGAg==; _ga=GA1.2.690483437.1489583101; Province=025; City=05278; NTES_PASSPORT=aXWcpL4bYTLQnXY4eO888VlwXt.v922HPG1pBkj.vkeDwsISwc4gjpib7gtylUsoCy.yIGuJPZg7Uq2lTWqIo3A5ddE7eIf5DP_mjdHrg7ky2KFIZHP60ge8g; P_INFO=m15152347277@163.com|1500267468|1|blog|11&10|jis&1499527300&mail163#jis&320800#10#0#0|151277&1|study&blog&photo|15152347277@163.com; UM_distinctid=15d4ee58fc9483-032aae6568b355-333f5902-100200-15d4ee58fca912; NTES_SESS=35juNvuVAClEtPfwjy5rP5GVXVpRFMmwg2ItfudhfLmyGTk4G2l_fIFHi_xsOJTWQrUJvW3JwsMFyepEs0SR6z1_QnKjbQFaesBY9ABy0TVFP_KIiXNgb89wCGe.3_hmKR90f2ybdvNPWqPX8_YesVlIQrWdw5Nfg6KF0EcoVXO3DgV09cJHAeiE_; S_INFO=1500623480|1|0&80##|m15152347277; ANTICSRF=dd45f2a4489d303de869d820a0dadf05; playerid=64643457; JSESSIONID-WYYY=oR0Q0Ce%2Bhldid%2FFtfsiobsg%5Cecyra1qnHBuFFPNBUW%2BbZ3%5C2uq5%2Fqz4VrhRll0%5CaVCfY%2Fg0%2BC47vS%5Cv6rsyuD76tlqWN%2BUryVxph9fZeCmVIDtu5so7vdcdp%2B92hI3A0R5Zm%2Besa5l3ND%5Cz59WOYTY%2FCUjG%2B8gFSGVyzTpMquPQIxyIM%3A1500647790286; _iuqxldmzr_=32; MUSIC_U=f5333454d16d0f0ca5e59b3a82afaabcb107f5e73a4504bae87278f38158d65dbef309e3badc0bfac257abd5a88c5d62dc7e2cf554b1b3fc233a987fb3c42671e386323209b86ec1bf122d59fa1ed6a2; __remember_me=true; __csrf=5cd5b19efc6ea479e298487216162acf; __utma=94650624.776578804.1489210725.1500604214.1500644866.50; __utmb=94650624.28.10.1500644866; __utmc=94650624; __utmz=94650624.1499960824.48.42.utmcsr=yukunweb.com|utmccn=(referral)|utmcmd=referral|utmcct=/412.html',
    'DNT': '1',
    'Host': 'music.163.com',
    'Pragma': 'no-cache',
    'Referer': 'http://music.163.com/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'music163.middlewares.Music163SpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'music163.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'music163.pipelines.MongoPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

MONGO_URI = 'localhost'
MONGO_DB = 'music163'