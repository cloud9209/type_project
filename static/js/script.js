$(document).ready(function(){
	$('#profile-div').hide();
	$('#works-whole').hide();
	$('#contact-div').hide();

	$('#intro').hover(
    function(){
        $('#profile-div').show();
    },
    function(){
        $('#profile-div').hide();
    });

	$('#works').click(function(){
		$('#works-whole').toggle();
	});

	$('#contact').click(function(){
		$('#contact-div').toggle();
	});

	
});