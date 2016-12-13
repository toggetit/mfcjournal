// Чистим модальные окна по закрытию
$('body').on('hidden.bs.modal', '.modal', function () {
  $(this).removeData('bs.modal');
});

function editCheckedActor(row) {
    
    console.log("Checked row", row.surname, row.name, row.pk);

    var jsoned = { data: { 'name': row.name, 'surname': row.surname, 'is_active': row.is_active, 'pk': row.pk } };
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
	url: "/journal/edit/act/" + row.pk + "/",
	data: jsondata,
	dataType: 'json',
	error: function (xhr, ajaxOptions, thrownError) {
	    console.log(xhr.status);
	    console.log(thrownError);
	}
    });
}

$('#actorsTable').bootstrapTable({
    onClickRow: function (row, $element, field) {

	console.log("Clicked row:", row.surname, row.name, row.pk);
	
	$('#id_name').val(row.name);
	$('#id_surname').val(row.surname);
	$('#id_is_active').prop('checked', row.is_active);
	$('#id_pk').val(row.pk);	
	
    },

    // Ниже сделать посылалку чек/анчеков на сервер сразу
    onCheck: editCheckedActor,
    onUncheck: editCheckedActor,
    onCheckAll: function (rows) {
	console.log("Checked All");
    },
    onUncheckAll: function (rows) {
	console.log("Unchecked All");
    }
});

