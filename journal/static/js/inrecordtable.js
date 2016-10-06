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

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
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
    console.log(pks)
    var jsoned = { data: pks };
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
	data: JSON.stringify(jsoned),
	/*
	success: function() {
	    $inRecTable.refresh( { silent: true} );
	},
	*/
	//success: $('#inRecTable').refresh(),
	dataType: 'json',
    });
    $('#inRecTable').refresh({ silent: true });
    $('#deleteButton').addClass('disabled');
});

/*
$('#searchButton').on('click', function(event) {
    var $table = $('#inRecTable');
    $(function () {
	$('#searchButton').click(function () {
            $table.bootstrapTable('refresh', {
                silent: true
            });
	    console.log('refreshed');
	});
    });
});
*/
