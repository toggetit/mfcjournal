$(document).ready(function(){
     $("#addNewIn").validate({
	 rules:{
             id_rec_num:{
		 required:true,
		 minlength:8
             },
             pass:"required"
	 },
	 messages:{
             id_rec_num:{
		 required:"Please provide your Login",
		 minlength:"Your Login must be at least 8 characters"
             },
             pass:"Please provide your password"
	 }
     });


$('.datepicker').datepicker();
