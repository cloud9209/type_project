$(document).ready(function(){
	$('#hover-act').hide();
	$('#click-act').hide();

	$('#head-hover').hover(
		function(){
			$('#hover-act').show();
		},
		function(){
			$('#hover-act').hide();
		}
		);
	
	$('#head-click').click(
		function(){
			$('#click-act').toggle();		
		});

	$('.popover-dismiss').popover();

});