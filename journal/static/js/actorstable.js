// Чистим модальные окна по закрытию
$('body').on('hidden.bs.modal', '.modal', function () {
  $(this).removeData('bs.modal');
});

$('#actorsTable').bootstrapTable({
    onClickRow: function (row, $element, field) {

	console.log("Clicked row:", row.surname, row.name, row.pk);
	
	$('#id_name').val(row.name);
	$('#id_surname').val(row.surname);
	$('#id_is_active').prop('checked', row.is_active);
	$('#id_pk').val(row.pk);	
	
    },

    // Ниже сделать посылалку чек/анчеков на сервер сразу
    onCheck: function (row, $element) {

	console.log("Checked row", row.surname, row.name, row.pk);

	
	event.preventDefault(); // To prevent following the link (optional)

	arr = $('#inRecTable').bootstrapTable('getSelections');
	var pks = arr.map(function(item) {
	    return item.pk;
	});
	var jsoned = { data: pks, doneDate : $('#id_action_date').val() };
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
	    success: function() {
		$('#markDoneModal').modal('hide');
		refreshPageData();
	    },
	    error: function (xhr, ajaxOptions, thrownError) {
		console.log(xhr.status);
		console.log(thrownError);
	    }
	});
	*/	
    },
    onUncheck: function (row, $element) {
	console.log("Unchecked");
    },
    onCheckAll: function (rows) {
	console.log("Checked All");
    },
    onUncheckAll: function (rows) {
	console.log("Unchecked All");
    }
});

