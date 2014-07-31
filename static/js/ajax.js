$(document).ready(function(){
	$('#search_button').click(function(){
		var query = $('#search_text').val();
		$('#search_text').val(""); 
		$('#twit_div').empty();
		
		$.ajax({
			url : '/tweepy_query',
			type : 'post',
			data : {"query" : query},

			success : function(datas){
				var json_datas = $.parseJSON(datas);
				var content = "<table id = 'twit_table'><tr><td class='twit_name'>Name</td><td class='twit_name td_right'>Content</td></tr>";

				for(i=0; i < json_datas.length; i++){
					content += "<tr class='twit_table_tr'><td class='twit_contents td_left'>" + json_datas[i].user_name + "</td><td class='twit_contents td_right td_right_contents'>" + json_datas[i].text + "</td></tr>";
				}
				content += "</table>";

				$('#twit_div').append(content);
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