# -*- coding: UTF-8 -*-

from coffin.shortcuts import render_to_response
from budget_app.models import Budget, BudgetBreakdown, EconomicCategory
from budget_app.views.helpers import *
import json

# Object used to define data as literal. See http://stackoverflow.com/a/2466207
class DataPoint(object):
    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])

data = [
    [2016, '001', True, 2960000000],
    [2016, '002', True, 1990000000],
    [2016, '003', True, 9311172200],
    [2016, '004', True, 1856037600],
    [2016, '005', True, 2462971500],
    [2016, '006', True, 7453890400],
    [2016, '007', True, 467832100],
    [2016, '008', True, 2364585200],
    [2016, '010', True, 6653310800],
    [2016, '011', True, 2104795100],
    [2016, '017', True, 287757300],
    [2016, '018', True, 1049612000],
    [2016, '019', True, 81990000],
    [2016, '001', False, 2960000000],
    [2016, '002', False, 1990000000],
    [2016, '003', False, 9311172200],
    [2016, '004', False, 1856037600],
    [2016, '005', False, 2462971500],
    [2016, '006', False, 7453890400],
    [2016, '007', False, 467832100],
    [2016, '008', False, 2364585200],
    [2016, '010', False, 6653310800],
    [2016, '011', False, 2104795100],
    [2016, '017', False, 287757300],
    [2016, '018', False, 1049612000],
    [2016, '019', False, 81990000],
    [2016, '110', True, 444500000],
    [2016, '111', True, 430413000],
    [2016, '110', False, 444500000],
    [2016, '111', False, 430413000],
    [2016, '201', True, 655810900],
    [2016, '202', True, 260507100],
    [2016, '203', True, 882283200],
    [2016, '209', True, 25209600],
    [2016, '210', True, 33100000],
    [2016, '212', True, 935406500],
    [2016, '213', True, 68416200],
    [2016, '214', True, 220085400],
    [2016, '215', True, 2312572300],
    [2016, '216', True, 9500000],
    [2016, '222', True, 1309361800],
    [2016, '201', False, 655810900],
    [2016, '202', False, 260507100],
    [2016, '203', False, 882283200],
    [2016, '209', False, 25209600],
    [2016, '210', False, 33100000],
    [2016, '212', False, 935406500],
    [2016, '213', False, 68416200],
    [2016, '214', False, 220085400],
    [2016, '215', False, 2312572300],
    [2016, '216', False, 9500000],
    [2016, '222', False, 1309361800],
    [2016, '301', True, 122466200],
    [2016, '302', True, 390000000],
    [2016, '303', True, 103919100],
    [2016, '304', True, 582046400],
    [2016, '305', True, 1311650500],
    [2016, '306', True, 543445000],
    [2016, '307', True, 77373500],
    [2016, '308', True, 351338800],
    [2016, '309', True, 59570000],
    [2016, '310', True, 48447000],
    [2016, '311', True, 3372015800],
    [2016, '312', True, 128800000],
    [2016, '313', True, 29392200],
    [2016, '314', True, 316816700],
    [2016, '315', True, 20285100],
    [2016, '301', False, 122466200],
    [2016, '302', False, 390000000],
    [2016, '303', False, 103919100],
    [2016, '304', False, 582046400],
    [2016, '305', False, 1311650500],
    [2016, '306', False, 543445000],
    [2016, '307', False, 77373500],
    [2016, '308', False, 351338800],
    [2016, '309', False, 59570000],
    [2016, '310', False, 48447000],
    [2016, '311', False, 3372015800],
    [2016, '312', False, 128800000],
    [2016, '313', False, 29392200],
    [2016, '314', False, 316816700],
    [2016, '315', False, 20285100],

    [2015, '001', True, 3410000000],
    [2015, '002', True, 2148111800],
    [2015, '003', True, 9208782000],
    [2015, '004', True, 1755746500],
    [2015, '005', True, 2247715600],
    [2015, '006', True, 7849307600],
    [2015, '007', True, 467832100],
    [2015, '008', True, 2189792800],
    [2015, '010', True, 6527082500],
    [2015, '011', True, 1923119200],
    [2015, '017', True, 239686000],
    [2015, '018', True, 1199139300],
    [2015, '019', True, 79980000],
    [2015, '001', False, 3410000000],
    [2015, '002', False, 2148111800],
    [2015, '003', False, 9208782000],
    [2015, '004', False, 1755746500],
    [2015, '005', False, 2247715600],
    [2015, '006', False, 7849307600],
    [2015, '007', False, 467832100],
    [2015, '008', False, 2189792800],
    [2015, '010', False, 6527082500],
    [2015, '011', False, 1923119200],
    [2015, '017', False, 239686000],
    [2015, '018', False, 1199139300],
    [2015, '019', False, 79980000],
    [2015, '110', True, 430000000],
    [2015, '111', True, 402956200],
    [2015, '110', False, 430000000],
    [2015, '111', False, 402956200],
    [2015, '201', True, 670881200],
    [2015, '202', True, 250850000],
    [2015, '203', True, 805276600],
    [2015, '209', True, 25795000],
    [2015, '210', True, 275062400],
    [2015, '212', True, 950433800],
    [2015, '213', True, 65395600],
    [2015, '214', True, 519468400],
    [2015, '215', True, 2229622500],
    [2015, '216', True, 9500000],
    [2015, '222', True, 1270078000],
    [2015, '201', False, 670881200],
    [2015, '202', False, 250850000],
    [2015, '203', False, 805276600],
    [2015, '209', False, 25795000],
    [2015, '210', False, 275062400],
    [2015, '212', False, 950433800],
    [2015, '213', False, 65395600],
    [2015, '214', False, 519468400],
    [2015, '215', False, 2229622500],
    [2015, '216', False, 9500000],
    [2015, '222', False, 1270078000],
    [2015, '301', True, 121631800],
    [2015, '302', True, 390000000],
    [2015, '303', True, 104763900],
    [2015, '304', True, 591019600],
    [2015, '305', True, 1406079100],
    [2015, '306', True, 538445000],
    [2015, '307', True, 106824700],
    [2015, '308', True, 303179300],
    [2015, '309', True, 54145800],
    [2015, '310', True, 50953200],
    [2015, '311', True, 3362807000],
    [2015, '312', True, 131500000],
    [2015, '313', True, 27235100],
    [2015, '314', True, 299799900],
    [2015, '315', True, 17399000],
    [2015, '301', False, 121631800],
    [2015, '302', False, 390000000],
    [2015, '303', False, 104763900],
    [2015, '304', False, 591019600],
    [2015, '305', False, 1406079100],
    [2015, '306', False, 538445000],
    [2015, '307', False, 106824700],
    [2015, '308', False, 303179300],
    [2015, '309', False, 54145800],
    [2015, '310', False, 50953200],
    [2015, '311', False, 3362807000],
    [2015, '312', False, 131500000],
    [2015, '313', False, 27235100],
    [2015, '314', False, 299799900],
    [2015, '315', False, 17399000],

    [2014, '001', True, 3260000000],
    [2014, '002', True, 1842308000],
    [2014, '003', True, 8044523200],
    [2014, '004', True, 1755746500],
    [2014, '005', True, 2259959600],
    [2014, '006', True, 7457614400],
    [2014, '007', True, 492832100],
    [2014, '008', True, 1539868200],
    [2014, '010', True, 5543331600],
    [2014, '011', True, 2078856700],
    [2014, '017', True, 231133700],
    [2014, '001', False, 3260000000],
    [2014, '002', False, 1842308000],
    [2014, '003', False, 8044523200],
    [2014, '004', False, 1755746500],
    [2014, '005', False, 2259959600],
    [2014, '006', False, 7457614400],
    [2014, '007', False, 492832100],
    [2014, '008', False, 1539868200],
    [2014, '010', False, 5543331600],
    [2014, '011', False, 2078856700],
    [2014, '017', False, 231133700],
    [2014, '104', True, 1323428400],
    [2014, '105', True, 79980000],
    [2014, '108', True, 320000000],
    [2014, '109', True, 2555000000],
    [2014, '110', True, 430000000],
    [2014, '111', True, 356693100],
    [2014, '104', False, 1323428400],
    [2014, '105', False, 79980000],
    [2014, '108', False, 320000000],
    [2014, '109', False, 2555000000],
    [2014, '110', False, 430000000],
    [2014, '111', False, 356693100],
    [2014, '201', True, 762166200],
    [2014, '202', True, 253560000],
    [2014, '203', True, 812965300],
    [2014, '209', True, 25655900],
    [2014, '210', True, 203400000],
    [2014, '212', True, 913518000],
    [2014, '213', True, 65100000],
    [2014, '214', True, 406932900],
    [2014, '215', True, 1472902500],
    [2014, '216', True, 9500000],
    [2014, '222', True, 1258988500],
    [2014, '201', False, 762166200],
    [2014, '202', False, 253560000],
    [2014, '203', False, 812965300],
    [2014, '209', False, 25655900],
    [2014, '210', False, 203400000],
    [2014, '212', False, 913518000],
    [2014, '213', False, 65100000],
    [2014, '214', False, 406932900],
    [2014, '215', False, 1472902500],
    [2014, '216', False, 9500000],
    [2014, '222', False, 1258988500],
    [2014, '301', True, 124409200],
    [2014, '302', True, 380000000],
    [2014, '303', True, 75775200],
    [2014, '304', True, 600863400],
    [2014, '305', True, 1471042800],
    [2014, '306', True, 486217800],
    [2014, '307', True, 85168900],
    [2014, '308', True, 301949300],
    [2014, '309', True, 42102200],
    [2014, '310', True, 56584700],
    [2014, '311', True, 3318573300],
    [2014, '312', True, 140875000],
    [2014, '313', True, 36769100],
    [2014, '314', True, 356362300],
    [2014, '315', True, 15599000],
    [2014, '301', False, 124409200],
    [2014, '302', False, 380000000],
    [2014, '303', False, 75775200],
    [2014, '304', False, 600863400],
    [2014, '305', False, 1471042800],
    [2014, '306', False, 486217800],
    [2014, '307', False, 85168900],
    [2014, '308', False, 301949300],
    [2014, '309', False, 42102200],
    [2014, '310', False, 56584700],
    [2014, '311', False, 3318573300],
    [2014, '312', False, 140875000],
    [2014, '313', False, 36769100],
    [2014, '314', False, 356362300],
    [2014, '315', False, 15599000],
]

entity_descriptions = [
    ['001', 'Ens públic Radiotelevisió de les Illes Balears', 'Ente público Radiotelevisión de las Illes Balears'],
    ['002', 'Agència del Turisme de les Illes Balears', 'Agencia del Turismo de las Illes Balears'],
    ['003', "Agència Balear de l'Aigua i de la Qualitat Ambiental", 'Agencia Balear del Agua y de la Calidad Ambiental'],
    ['004', 'Institut Balear de la Natura', 'Instituto Balear de la Naturaleza'],
    ['005', "Institut Balear de l'Habitatge", 'Instituto Balear de la Vivienda'],
    ['006', 'Serveis Ferroviaris de Mallorca', 'Servicios Ferroviarios de Mallorca'],
    ['007', "Institut d'Innovació Empresarial de les Illes Balears", 'Instituto de Innovación Empresarial de las Illes Balears'],
    ['008', "Institut Balear d'Infraestructures i Serveis Educatius i Culturals", 'Instituto Balear de Infraestructuras y Servicios Educativos y Culturales'],
    ['010', 'Fons de Garantia Agrària i Pesquera de les Illes Balears', 'Fondo de Garantía Agraria y Pesquera de las Illes Balears'],
    ['011', 'Ports de les Illes Balears', 'Puertos de las Illes Balears'],
    ['017', 'Institut Balear de la Joventut', 'Instituto Balear de la Juventud'],
    ['018', 'Serveis de Millora Agrària i Pesquera', 'Servicios de Mejora Agraria y Pesquera'],
    ['019', "Serveis d'Informació Territorial de les Illes Balears", 'Servicios de Información Territorial de las Illes Balears'],
    ['104', "Serveis de Millora Agrària, SA", 'Servicios de Mejora Agraria, SA'],
    ['105', "Serveis d'Informació Territorial de les Illes Balears, SA", 'Servicios de Información Territorial de las Illes Balears, SA'],
    ['108', "Ràdio de les Illes Balears, SA", 'Radio de las Illes Balears, SA'],
    ['109', "Televisió de les Illes Balears, SA", 'Televisión de las Illes Balears, SA'],
    ['110', "Gestió d'Emergències de les Illes Balears, SA", 'Gestión de Emergencias de las Illes Balears, SA'],
    ['111', 'Multimèdia de les Illes Balears, SA', 'Multimedia de las Illes Balears, SA'],
    ['201', "Fundació per a l'Esport Balear", 'Fundación para el  Deporte Balear'],
    ['202', 'Fundació Conservatori de Música i Dansa de les Illes Balears', 'Fundación para el Conservatorio de Música y Danza de las Illes Balears'],
    ['203', "Fundació Institut Socioeducatiu s'Estel", "Fundación Instituto Socioeducativo s'Estel"],
    ['209', 'Fundació Robert Graves', 'Fundación Robert Graves'],
    ['210', "Fundació Teatre Principal d'Inca", 'Fundación Teatro Principal de Inca'],
    ['212', 'Fundació Banc de Sang i Teixits de les Illes Balears', 'Fundación Banco de Sangre y Tejidos de las Illes Balears'],
    ['213', "Fundació Escola Superior d'Art Dramàtic de les Illes Balears", 'Fundación para la Escuela Superior de Arte Dramático de las Illes Balears'],
    ['214', "Fundació d'Investigació Sanitària de les Illes Balears Ramon Llull", 'Fundación de Investigación Sanitaria de las Illes Balears Ramon Llull'],
    ['215', "Fundació d'Atenció i Suport a la Dependència", 'Fundación Atención y Apoyo a la Dependencia'],
    ['216', 'Fundació Santuari de Lluc', 'Fundación Santuario de Lluc'],
    ['222', "Fundació Balear d'Innovació i Tecnologia", 'Fundación Balear de Innovación y Tecnología'],
    ['301', 'Centre Balears Europa', 'Centro Baleares Europa'],
    ['302', 'Escola d’Hoteleria', 'Escuela de Hostelería'],
    ['303', 'Consorci Desestacionalització de l’Oferta a l’Illa de Mallorca', 'Consorcio Desestacionalitzación de la Oferta en la isla de Mallorca'],
    ['304', 'Velòdrom Palma Arena', 'Consorcio Velódromo Palma Arena'],
    ['305', 'Consorci d’Infraestructures de les Illes Balears', 'Consorcio de Infraestructuras de las Illes Balears'],
    ['306', 'Consorci Orquestra Simfònica Illes Balears “Ciutat de Palma”', 'Consorcio Orquesta Sinfònica de las Illes Balears “Ciutat de Palma”'],
    ['307', 'Consorci Foment d’Infraestructures Universitàries (COFIU)', 'Consorcio para el Fomento de Infraestructuras Universitarias (COFIU)'],
    ['308', "Institut d'Estudis Baleàrics", 'Instituto de Estudios Baleáricos'],
    ['309', 'Consorci Recuperació de la Fauna de les Illes Balears (COFIB)', 'Consorcio para la Recuperación de la Fauna de las Illes Balears (COFIB)'],
    ['310', "Consorci d'Aigües de les Illes Balears", 'Consorcio de Aguas de las Illes Balears'],
    ['311', 'Consorci de Transports de Mallorca', 'Consorcio de Transportes de Mallorca'],
    ['312', 'Consorci Formentera Desenvolupament', 'Consorcio Desarrollo Formentera'],
    ['313', 'Consorci Infraestructures ELM Palmanyola', 'Consorcio para el Desarrollo de Actuaciones en Palmanyola'],
    ['314', 'Consorci de Recursos Sociosanitaris i Assistencials IB', 'Consorcio de Recursos Sociosanitarios y Asistenciales IB'],
    ['315', 'Agència de Qualitat Universitària', 'Agencia de Calidad Universitaria'],
]

area_descriptions = [
    ['0', 'Entitats p&uacute;bliques empresarials', 'Entidades p&uacute;blicas empresariales'],
    ['1', 'Societats mercantils p&uacute;bliques', 'Sociedades mercantiles p&uacute;blicas'],
    ['2', 'Fundacions', 'Fundaciones'],
    ['3', 'Consorcis', 'Consorcios'],
]

def _get_area(item):
    return item.name[0]

def institutions(request, render_callback=None):
    # Get request context
    c = get_context(request, css_class='body-entities', title='')

    # Retrieve the entity to display
    main_entity = get_main_entity(c)
    set_title(c, main_entity.name)

    # Prepare the budget breakdowns
    c['economic_breakdown'] = BudgetBreakdown(['name'])
    c['economic_breakdown_by_area'] = BudgetBreakdown([_get_area, 'name'])
    for item in data:
        item = DataPoint(year=item[0], name=item[1], expense=item[2], amount=item[3])
        c['economic_breakdown'].add_item(item.year, item)
        c['economic_breakdown_by_area'].add_item(item.year, item)

    # Additional data needed by the view
    populate_level(c, main_entity.level)
    populate_entity_stats(c, main_entity)
    populate_years(c, 'economic_breakdown')
    populate_budget_statuses(c, main_entity.id)
    c['entity'] = main_entity

    # Add our custom descriptions
    descriptions_position = 1 if c['LANGUAGE_CODE']=='ca' else 2
    c['descriptions'] = { 'income': {}, 'expense': {} }
    for item in entity_descriptions:
        description = item[descriptions_position]
        c['descriptions']['income'][item[0]] = description
        c['descriptions']['expense'][item[0]] = description

    c['income_areas'] = {}
    c['expense_areas'] = {}
    for item in area_descriptions:
        description = item[descriptions_position]
        c['income_areas'][item[0]] = description
        c['expense_areas'][item[0]] = description
        c['descriptions']['income'][item[0]] = description
        c['descriptions']['expense'][item[0]] = description

    # if parameter widget defined use policies/widget template instead of policies/show
    template = 'institutions/index.html'

    return render(c, render_callback, template)
