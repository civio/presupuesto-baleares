// Theme custom js methods
$(document).ready(function(){

  var addProjects = function(){
    var projects = {
      "412D01": [
        {
          "name": "INFRAESTRUCTURES PROJECTES BEI  (VARIS)",
          "description": "Obres per continuar amb projecte aprovat  del contracte de préstec del BEI amb la CAIB",
          "budget": "4.358.803"
        },
        {
          "name": "Obres menors",
          "description": "Obres de reforma i manteniment dels centres educatius de les Illes Balears",
          "budget": "4.981.158"
        },
        {
          "name": "IES STA MARIA",
          "description": "Nou IES Santa Maria.  Previsió cost obra + llicència + possible  liquidació",
          "budget": "2.437.424"
        },
        {
          "name": "CEIP Miquel Duran i Saurina",
          "description": "Reforma Previsió cost obra + llicència + possible  liquidació",
          "budget": 28.1
        },
        {
          "name": "IES Puig de Sa Font",
          "description": "Ampliació del centre Inclou externalització projecte+llicència+ Obra + possible liquidació",
          "budget": 23.154
        },
        {
          "name": "CEIP Miquel Costa i Llobera",
          "description": "Reforma del CEIP Miquel Costa i Llobera",
          "budget": 95.508
        },
        {
          "name": "CEPA Arenal",
          "description": "Reforma del CEPA Arenal",
          "budget": 515.434
        },
        {
          "name": "CEIP S. Ballester (Manacor)",
          "description": "Ampliació del centre Inclou externalització projecte+llicència+ Obra + possible liquidació",
          "budget": 33.72
        },
        {
          "name": "IES Binissalem",
          "description": "Ampliació del centre Previsió cost obra + llicència + possible  liquidació",
          "budget": 39.34
        }
      ]
    };
    var str = {
      'es': 'Proyectos',
      'ca': 'Projectes',
    };
    var paths = window.location.pathname.split('/');
    var code = paths[paths.length-2];

    if (code && projects[code] && projects[code].length > 0) {
      var el = '<div id="projects-panel" class="data-panel">\
        <div id="main-total" class="panel">\
          <div class="panel-title"><span class="main-label">'+str[ $('html').attr('lang') ]+'<b> '+$('.section-header .page-title').html()+'</b></span><span id="totals-year">2017</span></div>\
          <div class="panel-content">';
      projects[code].forEach(function(project){
        el += '<p class="total-budgeted"><span>'+project.name+'</span> <b class="total-amount total-budgeted-amount">'+project.budget+' €</b></p>';
        el += '<p class="total-budgeted"><span class="project-description">'+project.description+'</span></p>';
      });
      el += '</div></div></div>';
      $('.policies .policies-content > .container').append(el);
    }
  };

  var addYearSelectorCustomLabels = function(){
    var str2016 = {
      'es': 'proyecto',
      'ca': 'projecte',
    };

    $('.data-controllers .layout-slider .slider .slider-tick-label').each(function(){
      var val = $(this).html();
      if (val === '2018'){
        $(this).html(val + '<br/><small><i> ('+ str2016[ $('html').attr('lang') ] +')</i></small>');
      }
    });
  };

  addYearSelectorCustomLabels();

  // if ($('body').hasClass('body-subprogrammes')) {
  //   addProjects();
  // }
});


