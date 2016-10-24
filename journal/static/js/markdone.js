$.fn.datepicker.defaults.language = 'ru'
$.fn.datepicker.defaults.todayHighlight = true
$.fn.datepicker.defaults.autoclose = true
$("#id_action_date").datepicker("setDate", new Date());

//$("#datepicker").datepicker("setDate", new Date());

$('#markDoneSubmit').on('click', function(event) {
    event.preventDefault(); // To prevent following the link (optional)
    console.log('markdone called');
    arr = $('#inRecTable').bootstrapTable('getSelections');
    var pks = arr.map(function(item) {
	return item.pk;
    });
    var jsoned = { data: pks, doneDate : $('#id_action_date').datepicker('getDate') };
    var jsondata = JSON.stringify(jsoned);
    console.log(jsondata);
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
	url: "/journal/markdone/",
	data: jsondata,
	dataType: 'json',
	success: refreshPageData,
	error: function (xhr, ajaxOptions, thrownError) {
            console.log(xhr.status);
            console.log(thrownError);
	}
    });
});
