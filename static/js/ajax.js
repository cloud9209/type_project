$(document).ready(function(){
	console.log("hi")
	$('#search_button').click(function(){

		var query = $('#search_text').val();

		$.ajax({
			url : '/tweepy_query',
			type : 'post',
			data : {"query" : query},

			success : function(datas){
				var json_datas = $.parseJSON(datas);
				var content = "<table><tr><td class='twit_name'>Name</td><td class='twit_name' id='td_right'>Content</td></tr>"

				for(i=0; i < json_datas.length; i++){
					content += "<tr><td class='twit_contents'>" + json_datas[i].user_name + "</td><td class='twit_contents' id='td_right'>" + json_datas[i].text +'</td></tr>';}
				content += "</table>"

				$('#twit_table').append(content);


			},
			error : function(){
				console.log("error");
			},
			complete : function(){
				console.log("complete")
			}
		});

	});
	
});