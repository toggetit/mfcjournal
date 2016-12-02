// Чистим модальные окна по закрытию
$('body').on('hidden.bs.modal', '.modal', function () {
  $(this).removeData('bs.modal');
});

$('#actorsTable').bootstrapTable({
    onClickRow: function (row, $element, field) {
	$('#id_act_name').val(row.name);
	$('#id_act_surname').val(row.surname);
	$('#id_is_active').prop('checked', row.is_active);
	$('#id_act_pk').val(row.pk);
	
	//console.log("Clicked", row.name);
    },
    onCheck: function (row, $element) {
	console.log("checked");
    },
    onUncheck: function (row, $element) {
    },
    onCheckAll: function (rows) {
    },
    onUncheckAll: function (rows) {
    }
});
