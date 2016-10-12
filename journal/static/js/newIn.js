$.fn.datepicker.defaults.language = 'ru'
$.fn.datepicker.defaults.todayHighlight = true
$.fn.datepicker.defaults.autoclose = true



$('#id_rec_num').on('input', function(event) {
    
    console.log(numarray);

    /*
    if ($.inArray($('#id_rec_num').val(), numarray)) {
	console.log('true');
    }
    else {
	console.log('false');
    }
    */
    console.log($.inArray($('#id_rec_num').val(), numarray));
});
