from pathlib import Path

BOT_NAME = 'pep_parse'

BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = 'results'

RESULT_DIR = BASE_DIR / RESULTS_DIR
RESULT_DIR.mkdir(exist_ok=True)

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = SPIDER_MODULES[0]

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

FEEDS = {
    RESULTS_DIR + '/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    }
}
