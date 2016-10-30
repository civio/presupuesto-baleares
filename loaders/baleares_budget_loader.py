# -*- coding: UTF-8 -*-

from budget_app.models import *
from budget_app.loaders.budget_loader import BudgetLoader
import csv
import os.path
import re


class BalearesBudgetLoader(BudgetLoader):

    def map_to_new_functional_structure(self, fc_code):
        programme_mapping = {
            '112B': '131A',
            '112C': '131B',
            '112E': '121C',
            '112F': '151C',
            '121E': '131B',
            '121J': '761B',
            '121K': '121H',
            '124A': '912B',
            '126A': '121B',
            '126C': '151A',
            '131A': '231A',
            '131B': '231B',
            '134A': '232A',
            '141A': '211A',
            '313A': '313D',
            '315B': '324A',
            '315C': '322C',
            '315D': '121I',
            '323D': '131C',
            '441A': '562A',
            '441B': '562B',
            '443B': '571B',
            '443C': '571A',
            '443E': '441A',
            '443K': '572A',
            '443L': '571C',
            '443M': '571B',
            '443Q': '572A',
            '457A': '461A',
            '463B': '151C',
            '463C': '151B',
            '463D': '132A',
            '463E': '151C',
            '511C': '531A',
            '511E': '522B',
            '512A': '561A',
            '513C': '521B',
            '513D': '521A',
            '514A': '531A',
            '514B': '522A',
            '521A': '551A',
            '521B': '551B',
            '533A': '571D',
            '533B': '571E',
            '533D': '571C',
            '533F': '571F',
            '533G': '571G',
            '551A': '591A',
            '611A': '141A',
            '612A': '141D',
            '612B': '141B',
            '612C': '141C',
            '612E': '141E',
            '612G': '141F',
            '612H': '141G',
            '613A': '142A',
            '613B': '142B',
            '634A': '811A',
            '731C': '731A',
            '763A': '761A',
        }

        # We got the higher levels of the new functional classification from the client,
        # so they're correct already.
        if len(fc_code)<=4:
            return fc_code
        # But if we get a subprogramme code (either when loading the functional classification,
        # or when loading data) we need to map the old subprogramme to the new codes.
        else:
            programme_id = fc_code[0:4]
            subprogramme_extension_id = fc_code[4:6]
            new_fc_code = programme_mapping.get(programme_id, programme_id) + subprogramme_extension_id
            return new_fc_code

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

    def add_institutional_category(self, items, line):
        description = self._escape_unicode(line[2])
        ic_code = self._amend_institutional_code(line[1])

        items.append({
                'institution': ic_code[0:3],
                'section': (ic_code[0:5] if len(ic_code)>3 else None),
                'department': (ic_code if len(ic_code)>5 else None),
                'description': description
            })

    def add_functional_category(self, items, line):
        fc_code = line[1]
        description = line[2]

        items.append({
                'area': (fc_code[0:1] if len(fc_code)>=1 else None),
                'policy': (fc_code[0:2] if len(fc_code)>=2 else None),
                'function': (fc_code[0:3] if len(fc_code)>=3 else None),
                'programme': (fc_code[0:4] if len(fc_code)>=4 else None),
                'subprogramme': (fc_code if len(fc_code)>=5 else None),
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
            # Functional codes: keep only the final part of the code...
            fc_code = self._get_trailing_code(line[4])
            # ...and map it to the new classification
            if line[0]!='2017':
                fc_code = self.map_to_new_functional_structure(fc_code)

            fc_area = fc_code[0:1]
            fc_policy = fc_code[0:2]
            fc_function = fc_code[0:3]
            fc_programme = fc_code[0:4]
            fc_subprogramme = fc_code
        else:
            fc_area = 'X'
            fc_policy = 'XX'
            fc_function = 'XXX'
            fc_programme = 'XXXX'
            fc_subprogramme = 'XXXXX'

        # Institutional and economic codes: keep only the final part of the code also.
        ic_code = self._amend_institutional_code(self._get_trailing_code(line[3]))
        ec_code = self._get_trailing_code(line[5])

        # Gather all the relevant bits and store them to be processed
        items.append({
                'ic_institution': ic_code[0:3],
                'ic_section': ic_code[0:5],
                'ic_department': ic_code,
                'ic_code': ic_code,
                'fc_area': fc_area,
                'fc_policy': fc_policy,
                'fc_function': fc_function,
                'fc_programme': fc_programme,
                'fc_subprogramme': fc_subprogramme,
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

    # The original codes are not well organised because the first digit doesn't reflect
    # the different public bodies taking part. We fix that by adding a leading digit that does.
    def _amend_institutional_code(self, ic_code):
        if len(ic_code)==1:     # Let the top-level codes go through unmodified
            return ic_code

        if ic_code.startswith('50'):
            return '1'+ic_code  # ATIB, Agencia Tributaria
        elif ic_code.startswith('60'):
            return '2'+ic_code  # SSIB, Seguridad Social
        else:
            return '0'+ic_code

    def _get_trailing_code(self, full_code):
        # Check for complex code format, since sometimes (2017 so far) is not there
        if full_code.find('/')==-1:
            return full_code
        else:
            match = re.search('/([A-Z0-9]*)$', full_code)
            return match.group(1)

    def _get_delimiter(self):
        return ','

