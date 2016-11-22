# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

def dbHandle():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        passwd='123456@qwe',
        db='longkang',
        charset='utf8',
        use_unicode=False
    )
    return conn

class TutorialPipeline(object):
    def process_item(self, item, spider):
        dbObject = dbHandle()
        cursor = dbObject.cursor()
        sql = 'insert into scrapy(title,link,`desc`) values (%s,%s,%s)'

        try:
            cursor.execute(sql,(item['title'],item['link'],item['desc']))
            dbObject.commit()
        except Exception as ex:
            print(ex)
            dbObject.rollback()

        return item

