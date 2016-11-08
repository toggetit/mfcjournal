$.fn.datepicker.defaults.language = 'ru';
$.fn.datepicker.defaults.todayHighlight = true;
$.fn.datepicker.defaults.autoclose = true;

var timer = null;
$('#id_rec_num').keydown(function(){
    clearTimeout(timer); 
    timer = setTimeout(checkRecNum, 250);
});
