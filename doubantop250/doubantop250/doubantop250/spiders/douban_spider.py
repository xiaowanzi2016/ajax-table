#coding=utf-8

from scrapy.spiders import Spider
from doubantop250.items import  Doubantop250Item
from scrapy import Request
import re
class doubantop250(Spider):
	name='douban_movie_top250'
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
	}
	def start_requests(self):
		url = 'https://movie.douban.com/top250'
		yield Request(url, headers=self.headers)

	def parse(self,response):
		#命令行调试代码
		#from scrapy.shell import inspect_response
		#inspect_response(response,self)
		
		item=Doubantop250Item()
		movies = response.xpath('//ol[@class="grid_view"]/li')

		for movie in movies:
			#item['actor']=movie.xpath('.//div[@class="bd"]/p[1]/text()').extract_first().encode('utf-8')
			#item['type_movie']=movie.xpath('.//div[@class="bd"]/p[1]/text()').extract_first().encode('utf-8')
			#item['year']=movie.xpath('.//div[@class="bd"]/p[1]/text()').extract_first().encode('utf-8')
			item['ranking']=movie.xpath('.//div[@class="pic"]/em/text()').extract()[0]
			item['name']=movie.xpath('.//div[@class="hd"]/a/span[1]/text()').extract()[0]
			item['score']=movie.xpath('.//div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
			item['score_num']=movie.xpath('.//div[@class="star"]/span/text()').re(ur'(\d+)人评价')[0]
			yield item

		next_url = response.xpath('//span[@class="next"]/a/@href').extract()
		if next_url:
			next_url = 'https://movie.douban.com/top250' + next_url[0]
			yield Request(next_url, headers=self.headers)