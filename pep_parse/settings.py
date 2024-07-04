from pathlib import Path

BOT_NAME = 'pep_parse'

BASE_DIR = Path(__file__).parent.parent
RESULTS = 'results'

FILE_NAME = 'pep_%(time)s.csv'
FILE_PATH = f'{RESULTS}/{FILE_NAME}'

RESULT_DIR = BASE_DIR / RESULTS

SPIDER_MODULES = ['pep_parse.spiders']

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

FEEDS = {
    FILE_PATH: {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    }
}
