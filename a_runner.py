from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from avitoparse import settings
#from avitoparse.spiders.avito import AvitoSpider
#from avitoparse.spiders.avitoteacher import AvitoteacherSpider
from avitoparse.spiders.headhunter import HeadhunterSpider

if __name__ == '__main__':
    scr_settings = Settings()
    scr_settings.setmodule(settings)
    process = CrawlerProcess(settings=scr_settings)
    #process.crawl(AvitoSpider)
    #process.crawl(AvitoteacherSpider)
    process.crawl(HeadhunterSpider)
    process.start()