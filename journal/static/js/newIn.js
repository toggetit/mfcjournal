$.fn.datepicker.defaults.language = 'ru'
$.fn.datepicker.defaults.todayHighlight = true
$.fn.datepicker.defaults.autoclose = true

function changeSubmit(data) {
    //console.log(data.data);
    var recNumGroup = $('#rec_num_grp');
    //var glyphicon = $('#rec_num_gicon');
    var submitButton = $('#submitBtn');
    if(data.data == "OK") {
	recNumGroup.addClass('has-success').removeClass('has-error');
	//glyphicon.addClass('glyphicon-ok').removeClass('glyphicon-remove');
	submitButton.prop('disabled', false);
	//submitButton.attr('disabled', 'disabled');
    }
    else {
	recNumGroup.removeClass('has-success').addClass('has-error');
	//glyphicon.removeClass('glyphicon-ok').addClass('glyphicon-remove');
	submitButton.prop('disabled', true);
    }
}

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

//Такие вот костыли, чтобы поймать момент остановки ввода
var timer = null;
$('#id_rec_num').keydown(function(){
    clearTimeout(timer); 
    timer = setTimeout(checkRecNum, 250);
});

$(document).ready(function() {
    $('.selectpicker').selectpicker();
});

