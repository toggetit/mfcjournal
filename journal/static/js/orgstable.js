// Чистим модальные окна по закрытию
$('body').on('hidden.bs.modal', '.modal', function () {
  $(this).removeData('bs.modal');
});

$('#orgTable').bootstrapTable({
    onClickRow: function (row, $element, field) {

	console.log("Clicked row:", row.org_name, row.pk);
	
	$('#id_org_name').val(row.org_name);
	$('#id_pk').val(row.pk);	
	
    }

});

