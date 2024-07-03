import csv
import datetime
from collections import defaultdict
from pathlib import Path

# from itemadapter import ItemAdapter

BASE_DIR = Path(__file__).parent.parent
FILE_PATH = BASE_DIR / 'results'
TIME = datetime.datetime.now().strftime('%Y-%m-%dT%H-%M')
FILE_NAME = f'status_summary_{TIME}.csv'


class PepParsePipeline:
    status_sums = defaultdict(int)

    def open_spider(self, spider):
        FILE_PATH.mkdir(exist_ok=True)

    def process_item(self, item, spider):
        self.status_sums[item['status']] += 1
        return item

    def close_spider(self, spider):
        file_output = FILE_PATH / FILE_NAME
        with open(file_output, 'w', encoding='utf-8') as file:
            csv.writer(file, dialect=csv.unix_dialect).writerows(
                [
                    ('Статус', 'Количество'),
                    *self.status_sums.items(),
                    ('Всего', sum(self.status_sums.values())),
                ]
            )
