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

//Цвет в зависимости от дат контроля/исполнения
function rowStyle(row, index) {
    console.log(row, row.control_date, row.action_date);
    var classes = ['active', 'success', 'info', 'warning', 'danger'];
    if(row.control_date) {
	cdate = new Date(row.control_date);
	if(row.action_date) {
	    adate = new Date(row.action_date);
	    if(adate > cdate) {
		return {classes: "danger"}
	    }
	    else {
		return {classes: "success"}
	    }
	}
	else {
	    if(cdate >= new Date())
	    {
		return {classes: "info"}
	    }
	    return {classes: "danger"}
	}
        
    }
    
    return {};
}

function refreshPageData() {
    $('#inRecTable').bootstrapTable('refresh');
    $('#deleteButton').prop('disabled', true);
    $('#appointActorBtn').addClass('disabled');
    $('#markDoneBtn').prop('disabled', true);
}

$('#inRecTable').bootstrapTable({
    onCheckAll: function (rows) {
	$('#deleteButton').prop('disabled', false);
	$('#markDoneButton').prop('disabled', false);
	$('#appointActorBtn').removeClass('disabled')
	$('#markDoneBtn').prop('disabled', false);;
    },
    onCheck: function(row, $element) {
	$('#deleteButton').prop('disabled', false);
	$('#markDoneButton').prop('disabled', false);
	$('#appointActorBtn').removeClass('disabled');
	$('#markDoneBtn').prop('disabled', false);
    },
    onUncheckAll: function (rows) {
	$('#deleteButton').prop('disabled', true);
	$('#markDoneButton').prop('disabled', true);
	$('#appointActorBtn').addClass('disabled');
	$('#markDoneBtn').prop('disabled', true);
    },
    onUncheck: function(row, $element) {
	if ( $('#inRecTable').bootstrapTable('getSelections').length == 0 ){
	    $('#deleteButton').prop('disabled', true);
	    $('#markDoneButton').prop('disabled', true);
	    $('#appointActorBtn').addClass('disabled');
	    $('#markDoneBtn').prop('disabled', true);
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
	url: "/journal/delrec/in/",
	data: jsondata,
	dataType: 'json',
	success: refreshPageData,
	error: function (xhr, ajaxOptions, thrownError) {
            console.log(xhr.status);
            console.log(thrownError);
	}
    });
});

function appointActor(act_pk) {
    arr = $('#inRecTable').bootstrapTable('getSelections');
    var pks = arr.map(function(item) {
	return item.pk;
    });
    //console.log(pks)
    var jsoned = { data: pks, actor: act_pk };
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
	url: "/journal/appoint/",
	data: jsondata,
	dataType: 'json',
	success: refreshPageData,
	error: function (xhr, ajaxOptions, thrownError) {
            console.log(xhr.status);
            console.log(thrownError);
	}
    });
}
