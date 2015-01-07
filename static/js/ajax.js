$(document).ready(function(){
	var n = 0;

	$('.into_the_proj').click(function(){
		if(n == 0){	
			$.ajax({
				type : 'POST',
				url : '/inside_proj',
				data : '',

				success : function(datas){
					$('#proj_papers').append(datas);
				},

				error : function(){
					console.log("error");
				},
				complete : function(){
					console.log("complete")
				}
			});
			n = 1;
		};
	});
});