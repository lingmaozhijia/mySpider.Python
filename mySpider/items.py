# coding=UTF-8
import scrapy

class ItcastItem(scrapy.Item):
    # 姓名
    positionname = scrapy.Field()
    # 详情连接
    positionlink = scrapy.Field()
    # 职位类别
    positionType = scrapy.Field()
    # 招聘人数
    peopleNum = scrapy.Field()
    # 工作地点
    workLocation = scrapy.Field()
    # 发布时间
    publishTime = scrapy.Field()