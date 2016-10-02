# -*- coding: UTF-8 -*-

from budget_app.models import *
from budget_app.loaders.budget_loader import BudgetLoader
import csv
import os.path
import re


class BalearesBudgetLoader(BudgetLoader):

    # We don't have funding categories, so create a dummy one and assign everything to it
    def get_default_funding_categories(self):
        categories = BudgetLoader.get_default_funding_categories(self)
        categories.append({ 
                        'expense': True, 
                        'source': 'X',
                        'fund_class': 'XX',
                        'fund': 'XXX',
                        'description': 'Gastos'
                    })
        categories.append({ 
                        'expense': False, 
                        'source': 'X',
                        'fund_class': 'XX',
                        'fund': 'XXX',
                        'description': 'Ingresos'
                    })
        return categories

    def add_functional_category(self, items, line):
        description = line[2]

        # Ignore subprogrammes for now
        if ( len(line[1])>4 ):
            return

        items.append({
                'area': (line[1][0:1] if len(line[1])>=1 else None),
                'policy': (line[1][0:2] if len(line[1])>=2 else None),
                'function': (line[1][0:3] if len(line[1])>=3 else None),
                'programme': (line[1][0:4] if len(line[1])>=4 else None),
                'description': description
            })


    def add_economic_category(self, items, line):
        description = line[3]

        items.append({
                'expense': (line[1].upper() == 'G'),
                'chapter': (line[2][0:1] if len(line[2])>=1 else None),
                'article': (line[2][0:2] if len(line[2])>=2 else None),
                'heading': (line[2][0:3] if len(line[2])>=3 else None),
                'subheading': (line[2][0:5] if len(line[2])>=5 else None),
                'description': description
            })

    #
    def add_data_item(self, items, line, is_expense, is_actual):
        # First, check whether it's an internal transfer. If so, do nothing
        if line[9]=='No':
            return

        # Parse functional code
        if is_expense:
            # Functional codes: keep only the final part of the code
            match = re.search('/([A-Z0-9]*)$', line[4])
            fc_code = match.group(1)

            fc_area = fc_code[0:1]
            fc_policy = fc_code[0:2]
            fc_function = fc_code[0:3]
            fc_programme = fc_code[0:4]
        else:
            fc_area = 'X'
            fc_policy = 'XX'
            fc_function = 'XXX'
            fc_programme = 'XXXX'

        # Institutional and economic codes: keep only the final part of the code also.
        ic_code = self._get_trailing_code(line[3])
        ec_code = self._get_trailing_code(line[5])

        # Gather all the relevant bits and store them to be processed
        items.append({
                'ic_code': ic_code,
                'fc_area': fc_area,
                'fc_policy': fc_policy,
                'fc_function': fc_function,
                'fc_programme': fc_programme,
                'ec_chapter': ec_code[0],
                'ec_article': (ec_code[0:2] if len(ec_code)>=2 else None),
                'ec_heading': (ec_code[0:3] if len(ec_code)>=3 else None),
                'ec_subheading': (ec_code if len(ec_code)>=4 else None),
                'ec_code': ec_code, # Redundant, but convenient
                'fdc_code': 'XXX',  # Not used
                'item_number': '',
                # We leave it blank, so the base loader will fill it in using the economica category
                'description': None,
                'amount': self._read_english_number(line[10])
            })

    def _get_trailing_code(self, full_code):
        match = re.search('/([A-Z0-9]*)$', full_code)
        return match.group(1)

    def _get_delimiter(self):
        return ','

