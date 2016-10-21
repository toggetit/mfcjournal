$.fn.datepicker.defaults.language = 'ru'
$.fn.datepicker.defaults.todayHighlight = true
$.fn.datepicker.defaults.autoclose = true

$("#datepicker").datepicker("setDate", new Date());

function checkRecNum() {
    
    yPrefix = new Date().getFullYear().toString().substr(2,2) + '/';
    var jsoned = { data: yPrefix + $('#id_rec_num').val() };
    var jsondata = JSON.stringify(jsoned);
    //Достаём csrf токен
    var csrftoken = getCookie('csrftoken');
    $.ajaxSetup({
	beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
		xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
	}
    });
    $.ajax({
	type: "POST",
	url: "/journal/checknum/in/",
	data: jsondata,
	dataType: 'json',
	success: changeSubmit,
	error: function (xhr, ajaxOptions, thrownError) {
            console.log(xhr.status);
            console.log(thrownError);
	}
    });
}
