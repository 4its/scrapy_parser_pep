import csv
import datetime
from collections import defaultdict

from pep_parse.settings import RESULTS_DIR


class PepParsePipeline:

    def open_spider(self, spider):
        self.status_sums = defaultdict(int)

    def process_item(self, item, spider):
        self.status_sums[item['status']] += 1
        return item

    def close_spider(self, spider):
        time = datetime.datetime.now().strftime('%Y-%m-%dT%H-%M')
        # file_output =
        with open(
                f'{RESULTS_DIR}/status_summary_{time}.csv', 'w',
                encoding='utf-8'
        ) as file:
            csv.writer(
                file,
                dialect=csv.unix_dialect,
                quoting=csv.QUOTE_NONE
            ).writerows(
                (('Статус', 'Количество'),
                 *self.status_sums.items(),
                 ('Всего', sum(self.status_sums.values())))
            )
