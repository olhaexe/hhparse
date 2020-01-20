# -*- coding: utf-8 -*-

# Ресурс: HH.ru. Регион не важен.
# Ваша задача перейти список любой из вакансий пройти этот список, пройти пагинацию зайди на страницу с вакансией и извлечь следующие данные
# Заголовок, URL, Предлагаемая ЗП, Список ключевых навыков, Название организации разместившей вакансию,
# Ссылка на страницу организации разместившей вакансию, Ссылку на логотип организации

import scrapy
from scrapy.http import HtmlResponse
from avitoparse.items import HeadhunterItem
from scrapy.loader import ItemLoader

class HeadhunterSpider(scrapy.Spider):
    name = 'headhunter'
    allowed_domains = ['hh.ru']
    start_urls = [f'https://hh.ru/search/vacancy?L_is_autosearch=false&area=1&clusters=true&enable_snippets=true&text=%D0%90%D0%BD%D0%B0%D0%BB%D0%B8%D1%82%D0%B8%D0%BA+big+data&page={idx}' for idx in range(3)]

    def parse(self, response: HtmlResponse):
        for url in response.xpath('//span[@class="g-user-content"]/a[@href]'):
            yield response.follow(url, callback=self.vac_parse)

    def vac_parse(self, response: HtmlResponse):
        item = ItemLoader(HeadhunterItem(), response)
        item.add_xpath('title', '//h1[@data-qa="vacancy-title"]/span/text()')
        item.add_xpath('title', '//h1[contains(@data-qa, "vacancy-title")]/text()')
        item.add_value('url', response.url.split('?')[0])
        item.add_xpath('salary', '//p[@class="vacancy-salary"]/text()')
        item.add_xpath('skills', '//div[contains(@data-qa, "skills-element")]/span[@data-qa="bloko-tag__text"]/text()')
        item.add_xpath('enterprise', '//a[@itemprop="hiringOrganization"]/span[@itemprop="name"]/span/text()')
        item.add_xpath('enterprise', '//a[@itemprop="hiringOrganization"]/span[contains(@itemprop, "name")]/text()')
        item.add_xpath('enterprise_url', '//a[contains(@itemprop, "hiringOrganization")]/@href')
        item.add_xpath('enterprise_logo', '//meta[contains(@itemprop, "logo")]/@content')
        yield item.load_item()
