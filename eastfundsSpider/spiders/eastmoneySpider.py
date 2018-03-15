#coding:utf-8
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from eastfundsSpider.items import EastfundsspiderItem
import datetime
import json

class EmSpider(CrawlSpider):
    name='eastmoney'
    #download_delay = 1 #下载延时
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
            fundtype=response.xpath(".//*[@class='infoOfFund']/table//tr[1]/td[1]/a/text()").extract()[0]
            fundcompany=response.xpath(".//*[@class='infoOfFund']/table//tr[2]/td[2]/a/text()").extract()[0]
            fundsize=response.xpath(".//*[@class='infoOfFund']/table//tr[1]/td[2]/text()").re(r'\d*\.\d{2}[^\x00-\xff]')[0]   #匹配中文字符

            todayestnav = response.xpath(".//*[@id='gz_gsz']/text()").extract()[0]  # 今日估值
            yestnav = response.xpath(".//dl[@class='dataItem02']/dd[@class='dataNums']/span[1]/text()").extract()[0]  # 昨日净值
            accumnav=response.xpath(".//dl[@class='dataItem03']/dd[@class='dataNums']/span[1]/text()").extract()[0] #累计净值

            todayrate=response.xpath(".//*[@id='gz_gszzl']/text()").extract()[0].strip("+").strip('%').replace(' ','0')
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
            hangyeurl=response.xpath(".//*[@class='fundDetail-footer']/ul/li[9]/a/@href").extract()[0]
            item=EastfundsspiderItem(fundname=fundname,fundid=fundid,fundtype=fundtype,fundcompany=fundcompany,fundsize=fundsize,
                                     todayestnav=todayestnav,yestnav=yestnav,accumnav=accumnav,
                                     todayrate=todayrate,weekrate=weekrate,monthrate=monthrate,threemonthrate=threemonthrate,sixmonthrate=sixmonthrate,
                                     fromthisyearrate=fromthisyearrate,yearrate=yearrate,twoyearrate=twoyearrate,threeyearrate=threeyearrate,
                                     category=category,date=date,
                                     )
            indusrtyurl = r"http://fund.eastmoney.com/f10/F10DataApi.aspx?type=hypz&code=%s&year=2017"  # 行业配置
            industryURL = indusrtyurl % fundid
            print industryURL
            print hangyeurl
            request=scrapy.Request(url=industryURL,callback=self.parse_hangye)
            request.meta['item']=item
            yield request
        elif differetiate==u"每万份收益":
            print u"货币基金"

    def parse_hangye(self,response):
        item=response.meta['item']
        try:
            item['industry1'] = response.xpath("/html/body/div[1]/div/table/tbody/tr[1]/td[2]/text()").extract()[0]
            item['industry1ratio'] = response.xpath("/html/body/div[1]/div/table/tbody/tr[1]/td[4]/text()").extract()[0]
            item['industry2'] = response.xpath("/html/body/div[1]/div/table/tbody/tr[2]/td[2]/text()").extract()[0]
            item['industry2ratio'] = response.xpath("/html/body/div[1]/div/table/tbody/tr[2]/td[4]/text()").extract()[0]
        except:
            pass
        print 'ok'
        yield item



