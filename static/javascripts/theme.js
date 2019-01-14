// Theme custom js methods
$(document).ready(function(){
  var addYearSelectorCustomLabels = function(){
    var str = {
      'es': 'proyecto',
      'ca': 'projecte',
    };

    $('.data-controllers .layout-slider .slider .slider-tick-label').each(function(){
      var val = $(this).html();
      if (val === '2019'){
        $(this).html(val + '<br/><small><i> ('+ str[ $('html').attr('lang') ] +')</i></small>');
      }
    });
  };

  // addYearSelectorCustomLabels();
});


