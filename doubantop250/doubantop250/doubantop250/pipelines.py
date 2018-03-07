# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
import MySQLdb.cursors
from twisted.enterprise import adbapi
class Doubantop250Pipeline(object):
    def __init__(self,dbpool):
        self.dbpool = dbpool

    '''保存到数据库中对应的class
       1、在settings.py文件中配置
       2、在自己实现的爬虫类中yield item,会自动执行'''
    @classmethod
    def from_settings(cls,settings):#名称固定 会被scrapy调用 直接可用setting的值
        adbparams=dict(
            host=settings['MYSQL_HOST'],
            db = settings['MYSQL_DBNAME'],
            user = settings['MYSQL_USER'],
            passwd = settings['MYSQL_PASSWORD'],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
            )
        #这是链接数据库的另一种方法，在settings中写入参数
        dbpool=adbapi.ConnectionPool('MySQLdb',**adbparams)
        return cls(dbpool)


    def process_item(self, item, spider):
        #使用twiest将mysql插入变成异步
        query=self.dbpool.runInteraction(self.do_insert,item)
        #因为异步 可能有些错误不能及时爆出
        query.addErrback(self.handle_error,item,spider)
    #处理异步的异常
    def handle_error(self,failure,item,spider):
        print(failure)


    def do_insert(self, cursor, item):
        insert_sql="""replace into doubantop250(name,ranking,score,score_num) VALUES (%s,%s,%s,%s)"""
        cursor.execute(insert_sql,(item['name'],item['ranking'],item['score'],item['score_num']))
    

