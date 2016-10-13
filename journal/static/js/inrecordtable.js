//Конвертим даты в наш формат. Вроде как распространённая практика
function dateFormatter(value) {
    if(value == null) {
	return value;
    }
    var dateConvert = new Date(value).toLocaleDateString('ru-RU');
    return dateConvert;
}

//Отображаем правильно поля "Без исполнителя"
function actorFormatter(value) {
    if(value == "None") {
	return "б/и";
    }
    return value;
}

function refreshPageData() {
    $('#inRecTable').bootstrapTable('refresh');
    $('#deleteButton').addClass('disabled');
}

$('#inRecTable').bootstrapTable({
    onCheckAll: function (rows) {
	$('#deleteButton').removeClass('disabled');
    },
    onCheck: function(row, $element) {
	$('#deleteButton').removeClass('disabled');
    },
    onUncheckAll: function (rows) {
	$('#deleteButton').addClass('disabled');
    },
    onUncheck: function(row, $element) {
	if ( $('#inRecTable').bootstrapTable('getSelections').length == 0 ){
	    $('#deleteButton').addClass('disabled');
	}
    }
});



$('#deleteButton').on('click', function(event) {
    arr = $('#inRecTable').bootstrapTable('getSelections');
    var pks = arr.map(function(item) {
	return item.pk;
    });
    //console.log(pks)
    var jsoned = { data: pks };
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
	url: "/journal/delrec/in",
	data: jsondata,
	dataType: 'json',
	success: refreshPageData,
	error: function (xhr, ajaxOptions, thrownError) {
            console.log(xhr.status);
            console.log(thrownError);
	}
    });
});

