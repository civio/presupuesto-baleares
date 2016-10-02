# -*- coding: UTF-8 -*-
from coffin.shortcuts import render_to_response
from django.utils.translation import ugettext as _
from budget_app.models import Budget, BudgetBreakdown, EconomicCategory
from budget_app.views.helpers import *
import json

def _get_institution(item):
    institution = getattr(item, 'institution') if getattr(item, 'institution') else ''
    if institution == '50':
        institution = 'ATIB'
    elif institution == '60':
        institution = 'SSIB'
    else:
        institution = 'AGIB'

    return institution

def institutions(request, render_callback=None):
    # Get request context
    c = get_context(request, css_class='body-entities', title='')

    # Retrieve the entity to display
    main_entity = get_main_entity(c)
    set_title(c, main_entity.name)

    # Prepare the budget breakdowns
    c['economic_breakdown'] = BudgetBreakdown([_get_institution, 'chapter'])

    get_budget_breakdown(   "e.id = %s", [ main_entity.id ],
                            [c['economic_breakdown']] )

    # Additional data needed by the view
    populate_level(c, main_entity.level)
    populate_entity_stats(c, main_entity)
    populate_entity_descriptions(c, main_entity)
    populate_years(c, 'economic_breakdown')
    populate_budget_statuses(c, main_entity.id)
    populate_area_descriptions(c, ['income', 'expense'])
    c['entity'] = main_entity

    c['descriptions']['expense']['AGIB'] = _('Gobierno de las Islas Baleares')
    c['descriptions']['expense']['SSIB'] = _('Servicio de Salud')
    c['descriptions']['expense']['ATIB'] = _('Agencia Tributaria')
    c['descriptions']['income']['AGIB'] = _('Gobierno de las Islas Baleares')
    c['descriptions']['income']['SSIB'] = _('Servicio de Salud')
    c['descriptions']['income']['ATIB'] = _('Agencia Tributaria')

    return render(c, render_callback, 'institutions/index.html')
