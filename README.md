# Проект асинхронного парсера страниц pep.
Простой парсер, предназначенный для получения информации с ресурса https://peps.python.org/ с помощью фреймворка **Scrapy**. 
В частности:
- получает ссылки на все документы PEP.
- формирует пул задач в рамках которого переходит на страницы каждого документа и собирает следующие данные:
  - номер документа;
  - название документа;
  - статус документа.
- в результате работы формирует 2 отчета в формате csv:
  - отчет по документам PEP(_Python Enhancement Proposal_) содержащий их номера, название и статусы;
  - сводный отчет, сожержащий информацию по количеству докуентов с тем или иным статусом.

## Технологии
- [**Python**](https://docs.python.org/3.12/)
- [**Scrapy**](https://pypi.org/project/Scrapy/2.5.1/)


## Использование

### Клонирование проекта
Выполните команду для клонирования и перехода в проект:
```bash
git clone https://github.com/4its/scrapy_parser_pep.git && cd scrapy_parser_pep
```

### Виртуальное окружение
Для создания и активации окружения:
```bash
python -m venv vevn %% source venv/bin/activate
```

### Установка зависимостей
Для установки зависимостей, выполните команду:
```bash
pip install -r requirements.txt
```

### Запуск парсера
```bash
scrapy crawl pep       
```

### Зачем разработали этот проект?
Данный проект разработан в рамках финального задания "Финальный проект спринта: асинхронный парсер PEP" в [Яндекс.Практикум](https://practicum.yandex.ru/python-developer-plus/)

## Разработчик проекта

- [**Georgii Egiazarian**](https://github.com/4its)
 