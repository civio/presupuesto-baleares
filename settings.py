# -*- coding: UTF-8 -*-

from django.conf.urls import patterns, url
from django.conf.urls.i18n import i18n_patterns

MAIN_ENTITY_LEVEL = 'comunidad'
MAIN_ENTITY_NAME = 'Baleares'

BUDGET_LOADER = 'BalearesBudgetLoader'

FEATURED_PROGRAMMES = ['121C', '723A', '722A', '542A', '423B', '413B', '455A', '322D']

# Number of programmes to feature in home page. Default: 3
# NUMBER_OF_FEATURED_PROGRAMMES = 4

OVERVIEW_INCOME_NODES = [
                          {
                            'nodes': '21',
                            'label.ca': 'Impost sobre el valor afegit',
                            'label.es': 'Impuesto sobre el valor añadido',
                          },
                          {
                            'nodes': '10',
                            'label.ca': 'Impost sobre la renda',
                            'label.es': 'Impuesto sobre la renta',
                          },
                          {
                            'nodes': [['22', '220']],
                            'label.ca': 'Imposts especials',
                            'label.es': 'Impuestos especiales',
                            'link_id': '22'
                          },
                          '20',
                          {
                            'nodes': [['11', '110']],
                            'label.ca': 'Impost general sobre successions i donacions',
                            'label.es': 'Impuesto sobre sucesiones y donaciones',
                            'link_id': '11'
                          }
                        ]
OVERVIEW_EXPENSE_NODES = [
                          '41', '42',
                          {
                            'nodes': '91',
                            'label.ca': 'Suport financer a administracions territorials',
                            'label.es': 'Apoyo financiero a administraciones locales',
                          },
                          '31', '56', '01', '32', '52', '45'
                        ]

# How aggresive should the Sankey diagram reorder the nodes. Default: 0.79 (Optional)
# Note: 0.5 usually leaves nodes ordered as defined. 0.95 sorts by size (decreasing).
OVERVIEW_RELAX_FACTOR = 0.5

# Does the data includes a fifth functional classification level, subprogrammes?. Default: False
USE_SUBPROGRAMMES = True

# Show Payments section in menu & home options. Default: False.
# SHOW_PAYMENTS           = True

# Show Tax Receipt section in menu & home options. Default: False.
# SHOW_TAX_RECEIPT        = True

# Show Counties & Towns links in Policies section in menu & home options. Default: False.
SHOW_COUNTIES_AND_TOWNS = False

# Show an extra tab with institutional breakdown. Default: True.
SHOW_INSTITUTIONAL_TAB  = True

# Show an extra treemap in the Policy page, showing institutional breakdown. Default: False.
# Important: insitutional codes must be consistent along the years, see CONSISTENT_INSTITUTIONAL_CODES.
SHOW_GLOBAL_INSTITUTIONAL_TREEMAP  = True

# Are institutional codes consistent along the years. Default: False.
# Important: We need this to be True for the institutional treemap to work properly.
CONSISTENT_INSTITUTIONAL_CODES = True

# Show an extra tab with funding breakdown (only applicable to some budgets). Default: False.
# SHOW_FUNDING_TAB = False

# Adjust inflation in amounts in Overview page. Default: True
ADJUST_INFLATION_IN_OVERVIEW = False

# Show Subtotals panel in Overview. Default: False
SHOW_OVERVIEW_SUBTOTALS = True

# Calculate budget indicators (True), or show/hide the ones hardcoded in HTML (False). Default: True.
# CALCULATE_BUDGET_INDICATORS = False

# Show an extra column with actual revenues/expenses. Default: True.
# Warning: the execution data still gets shown in the summary chart and in downloads.
# SHOW_ACTUAL = False

# Add economic categories codes as a prefix in the breakdown tables. Default: False.
ADD_ECONOMIC_CATEGORIES_PREFIX = True

# Should we group elements at the economic subheading level, or list all of them,
# grouping by uid?. Default: True. (i.e. group by uid, show all elements)
BREAKDOWN_BY_UID = False

# Include financial income/expenditures in overview and global policy breakdowns. Default: False.
# INCLUDE_FINANCIAL_CHAPTERS_IN_BREAKDOWNS = True

# Search in entity names. Default: True.
SEARCH_ENTITIES = False

# Supported languages. Default: ('es', 'Castellano')
LANGUAGES = (
  ('ca', 'Catal&agrave;'),
  ('es', 'Castellano'),
)


# Facebook Aplication ID used in social_sharing temaplate. Default: ''
# In order to get the ID create an app in https://developers.facebook.com/
FACEBOOK_ID             = '135301130284103'

# Google Analytics ID. Default: ''
# In order to get the ID create a Google Analytics Acount in https://analytics.google.com/analytics/web/
ANALYTICS_ID            = 'UA-28946840-16'

# Setup Data Source Budget link
DATA_SOURCE_BUDGET      = 'http://www.caib.es/sacmicrofront/home.do?mkey=M226&lang=ca'

# Setup Data Source Population link
DATA_SOURCE_POPULATION  = 'http://www.ibestat.cat/ibestat/estadistiques/155b5b14-b6cd-4160-80eb-0ca26f7679cd/bdf96a18-098e-4e46-a9b9-6cd430699fa2/es/pad_t4c1.px'

# Setup Data Source Inflation link
DATA_SOURCE_INFLATION   = 'http://www.ibestat.cat/ibestat/estadistiques/208bd66f-fd35-4c2a-9fda-dd764e72ec9b/4d5f7ebb-4daa-4253-81b2-51ec0ea4223a/es/E30138_11001.px'

# Setup Main Entity Web Url
MAIN_ENTITY_WEB_URL     = 'http://www.caib.es/'

# Setup Main Entity Legal Url (if empty we hide the link)
MAIN_ENTITY_LEGAL_URL   = 'http://www.caib.es/govern/external/infoLegal.do'

# External URL for Cookies Policy (if empty we use out template page/cookies.html)
#COOKIES_URL             = 'http://www.santiagodecompostela.gal/avisolegal.php?lg=gal'

# Allow overriding of default treemap color scheme
COLOR_SCALE = [ '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#e7969c', '#bcbd22', '#17becf' ]

# We can define additional URLs applicable only to the theme. These will get added
# to the project URL patterns list.
EXTRA_URLS = (
    url(r'^instituciones$', 'institutions', name="institutions"),
)
