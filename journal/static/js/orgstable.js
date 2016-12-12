// Чистим модальные окна по закрытию
$('body').on('hidden.bs.modal', '.modal', function () {
  $(this).removeData('bs.modal');
});

$('#actorsTable').bootstrapTable({
    onClickRow: function (row, $element, field) {

	console.log("Clicked row:", row.org_name, row.pk);
	
	$('#id_name').val(row.org_name);
	$('#id_pk').val(row.pk);	
	
    },

    // Ниже сделать посылалку чек/анчеков на сервер сразу
    onCheck: function (row, $element) {

	console.log("Checked row", row.surname, row.name, row.pk);

	var jsoned = { data: { 'org_name': row.org_name, 'pk': row.pk } };
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
	    url: "/journal//",
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

