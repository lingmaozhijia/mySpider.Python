# coding=UTF-8
import scrapy
from mySpider.items import ItcastItem


# 创建一个爬虫类
class TencentSpider(scrapy.Spider):
    # 爬虫名
    name = "tencent"

    # 允许爬虫作用的范围
    allowed_domains = ["tencent.com"]

    # 爬虫其实的url
    url = "http://hr.tencent.com/position.php?&start="
    offset = 0

    # 因为数据是多页，所以要动态爬取
    start_urls = [url + str(offset)]

    # 此方法不能随便创建，名称一定要是parse
    def parse(self, response):

        # 通过scrapy自带的xpath匹配出所有老师的根节点列表集合
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):

            # Item对象用来保存数据的
            item = ItcastItem()

            item['positionname'] = each.xpath("./td[1]/a/text()").extract()[0]
            # 详情连接
            item['positionlink'] = each.xpath("./td[1]/a/@href").extract()[0]
            # 职位类别
            item['positionType'] = each.xpath("./td[2]/text()").extract()[0]
            # 招聘人数
            item['peopleNum'] = each.xpath("./td[3]/text()").extract()[0]
            # 工作地点
            item['workLocation'] = each.xpath("./td[4]/text()").extract()[0]
            # 发布时间
            item['publishTime'] = each.xpath("./td[5]/text()").extract()[0]

            yield item

            # 当爬到数据少于2438条时，每爬一次加10条
            if self.offset < 2438:
                self.offset += 10

            # 加完10条后，重新爬取数据
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)