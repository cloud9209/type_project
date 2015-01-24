$(document).ready(function() {
    $('#comment_on_proj_submit').on('click', function(){
        var _this_ = $(this);
        var input = $(_this_.parent().parent().children()[1]).find('input');
        if (input.val() == "") return;
        console.log( { body : input.val() } );
        $.ajax({
            type : 'POST',
            url  : _this_.parent().parent().attr('target'),
            data : { body : input.val() },
            success : function(response) {
                if ( response.success ) {
                    console.log('success');
                    // clear input box
                    input.val('');
                    // append new comment
                    _this_.parent().parent().before( response.body );
                } else {
                    console.log('not authenticated');
                }
            },
            error : function() {
                console.log('error : ' + _this_);
            },
            complete : function() {
                console.log('completed : ' + _this_);
            }
        });
    });
});