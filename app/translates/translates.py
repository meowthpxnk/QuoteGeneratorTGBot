import asyncio

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TranslateParams:
    def __init__(self, source_lang, target_lang, text):
        self.source_lang = source_lang
        self.target_lang = target_lang
        self.text = text
    
    def to_dict(self):
        return {
            "source_lang": self.source_lang,
            "target_lang": self.target_lang,
            "text": self.text,
        }
    
    def to_string(self):
        params_dict = self.to_dict()

        text = "?" + "&".join([
            f"{key}={params_dict[key]}"
            for key
            in params_dict
        ])

        return text

class Translator:

    def __init__(self, base_url="https://translate.yandex.ru"):
        self.base_url = base_url
        self.browser = self.generate_browser()

    @staticmethod
    def generate_browser():
        options = Options()
        # options.add_argument('--headless=new')
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        # service = Service(executable_path="/usr/bin/chromedriver")
        return webdriver.Chrome(options=options)

    @classmethod
    async def force_translate_text(cls, text, source_lang="en", target_lang="ru"):
        self = cls()
        return await self.translate_text(text, source_lang, target_lang)

    async def translate_text(self, text, source_lang="en", target_lang="ru"):
        params = TranslateParams(source_lang, target_lang, text)

        self.browser.get(
            self.base_url + params.to_string()
        )

        await asyncio.sleep(1)

        return self.extract_text()
    
    def extract_text(self):
        spans = self.browser.find_elements(
            By.XPATH,
            "//span[@data-complaint-type='fullTextTranslation']/span"
        )

        text = "".join(
            span.text
            for span
            in spans
        )

        return text
