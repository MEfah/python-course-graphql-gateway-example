import json
import os

from models.news import NewsModel


class NewsService:
    """
    Сервис для работы с данными о новостях.
    """

    @staticmethod
    def get_news(alpha2codes: list[str]) -> dict[str, list[NewsModel]]:
        """
        Получение списка новостей.
        
        :param alpha2codes: Список ISO Alpha2-кодов стран
        :return:
        """

        base_path = "fixtures/news/"
        existing_files = os.listdir(base_path)
        result = {}
        for alpha2code in alpha2codes:
            if not alpha2code:
                continue
            
            code = alpha2code.lower()
            if f"{code}.json" in existing_files:
                with open(base_path + f"{code}.json", encoding="utf-8") as file:
                    if data := json.load(file):
                        result[alpha2code] = [
                            NewsModel(
                                author=news_item.get("author"),
                                source=news_item.get("source").get("name"),
                                title=news_item.get("title"),
                                description=news_item.get("description"),
                                url=news_item.get("url"),
                                url_to_image=news_item.get("urlToImage"),
                                published_at=news_item.get("publishedAt"),
                                content=news_item.get("content"),
                            )
                            for news_item in data
                        ]

        return result