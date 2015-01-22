$(document).ready(function(){
    $('.project_like').click(function(){
        var event_target = $(this);
        $.ajax({
            type : 'POST',
            url  : '/project/' + $(this).find('div').attr('data') + '/like',
            data : '',

            success : function(response) {
                if(response.is_success) {
                    event_target.contents().last()[0].textContent = response.like_count;
                }
            },
            error   : function() {
                console.log('error')
            },
            complete: function() {
                console.log('completed.')
            }
        });
    });
});