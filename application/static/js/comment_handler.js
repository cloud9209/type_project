$(document).on("click", '.new-comment', function(event) { 
    var _this_ = $(this);
    var input = $(_this_.parent().parent().children()[1]).find('input');
    if (input.val() == "") return; // TODO : client empty message handling
    console.log( { body : input.val() } );
    _this_.attr('disabled', true);
    $.ajax({
        type : 'POST',
        url  : _this_.attr('target'),
        data : { body : input.val() },
        success : function(response) {
            if ( response.success ) {
                // Clear InputBox & Append New Comment
                input.val('');
                _this_.parent().parent().before( response.body );
            } else {
                console.log('not authorized');
            }
            _this_.attr('disabled', false);
        },
        error : function() {
            console.log('error : ' + _this_);
            _this_.attr('disabled', false);
        }
    });
});

$(document).on("click", '.remove-comment', function(event) { 
    var _this_ = $(this);
    _this_.attr('disabled', true);
    $.ajax({
        type : 'POST',
        url  : _this_.attr('target'),
        data : { 'comment_id' : _this_.attr('target').split('/')[2] },
        success : function(response) {
            if ( response.success ) {
                _this_.parent().parent().remove();
            } else {
                console.log('not authorized');
            }
        },
        error : function() {
            console.log('error : ' + _this_);
            _this_.attr('disabled', false);
        }
    });
});

$(document).on("click", '.modify-comment', function(event) { 
    var _this_ = $(this);
    _this_.attr('disabled', true);
    $.ajax({
        type : 'POST',
        url  : _this_.attr('target'),
        data : { 'comment_id' : _this_.attr('target').split('/')[2] },
        success : function(response){
            if ( response.success ) {
                _this_.parent().parent().replaceWith(response.body);
            } else {
                console.log('not authorized');
            }
        },
        error : function() {
            console.log('error : ' + _this_);
            _this_.attr('disabled', false);
        }
    });
});

$(document).on("click", '.submit-modified-comment', function(event) {
    var _this_ = $(this);
    var body = $(_this_.parent().parent().children()[1]).find('input').val();
    _this_.attr('disabled', true);
    $.ajax({
        type : 'POST',
        url  : _this_.attr('target'),
        data : { 'comment_id' : _this_.attr('target').split('/')[2] , 'body' : body },
        success : function(response){
            if ( response.success ) {
                _this_.parent().parent().replaceWith(response.body);
            } else {
                console.log('not authorized');
            }
        },
        error : function() {
            console.log('error : ' + _this_);
            _this_.attr('disabled', false);
        }
    });
});