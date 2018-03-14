#coding:utf-8
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from eastfundsSpider.items import EastfundsspiderItem
import datetime


class EmSpider(CrawlSpider):
    name='eastmoney'
    #download_delay = 1
    allowed_domains=["fund.eastmoney.com"]
    start_urls=[
        "http://fund.eastmoney.com/allfund.html"
    ]
    rules=(
        Rule(SgmlLinkExtractor(allow=("fund.eastmoney.com/\d*\.html",)),
             follow=True,
             callback='parse_item'
             ),
    )
    def parse_item(self,response):
        differetiate=response.xpath(".//dl[@class='dataItem01']//span[@class='sp01']//text()").extract()[0]
        print differetiate
        if differetiate==u"净值估算":
            fundname = response.xpath(".//div[@class='fundDetail-tit']/div/text()").extract()[0]
            fundid=response.xpath(".//div[@class='fundDetail-tit']/div//span[@class='ui-num'][1]/text()").extract()[0]
            todayestnav = response.xpath(".//*[@id='gz_gsz']/text()").extract()[0]  # 今日估值
            yestnav = response.xpath(".//dl[@class='dataItem02']/dd[@class='dataNums']/span[1]/text()").extract()[0]  # 昨日净值
            accumnav=response.xpath(".//dl[@class='dataItem03']/dd[@class='dataNums']/span[1]/text()").extract()[0] #累计净值
            weekrate=response.xpath(".//*[@id='increaseAmount_stage']/table//tr[2]/td[2]/div/text()").extract()[0]
            monthrate=response.xpath(".//*[@id='increaseAmount_stage']/table//tr[2]/td[3]/div/text()").extract()[0]
            threemonthrate=response.xpath(".//*[@id='increaseAmount_stage']/table//tr[2]/td[4]/div/text()").extract()[0]
            sixmonthrate=response.xpath(".//*[@id='increaseAmount_stage']/table//tr[2]/td[5]/div/text()").extract()[0]
            fromthisyearrate=response.xpath(".//*[@id='increaseAmount_stage']/table//tr[2]/td[6]/div/text()").extract()[0]
            yearrate=response.xpath(".//*[@id='increaseAmount_stage']/table//tr[2]/td[7]/div/text()").extract()[0]
            twoyearrate=response.xpath(".//*[@id='increaseAmount_stage']/table//tr[2]/td[8]/div/text()").extract()[0]
            threeyearrate=response.xpath(".//*[@id='increaseAmount_stage']/table//tr[2]/td[9]/div/text()").extract()[0]
            category=u'净值型'
            date=datetime.datetime.now().strftime("%Y-%m-%d")
            print fundname, todayestnav,yestnav,accumnav
            item=EastfundsspiderItem(fundname=fundname,fundid=fundid,todayestnav=todayestnav,yestnav=yestnav,accumnav=accumnav,category=category,
                                     date=date,weekrate=weekrate,monthrate=monthrate,threemonthrate=threemonthrate,sixmonthrate=sixmonthrate,
                                     fromthisyearrate=fromthisyearrate,yearrate=yearrate,twoyearrate=twoyearrate,threeyearrate=threeyearrate)
            yield item
        elif differetiate==u"每万份收益":
            print u"货币基金"





