$(document).on("click", '.new-comment', function(event) { 
    var _this_ = $(this);
    var input = $(_this_.parent().parent().children()[1]).find('input');
    if (input.val() == "") return;
    _this_.attr('disabled', true);
    $.ajaxWithAlert({
        type : 'POST',
        url  : _this_.attr('target'),
        data : { body : input.val() },
        on_success : function(response) {
            input.val('');
            _this_.parent().parent().before( response.body );
        },
        on_finish : function() {
            _this_.attr('disabled', false);
        },
        on_error : function() {
            _this_.attr('disabled', false);
        }
    });
});
$(document).on("click", '.remove-comment', function(event) { 
    var _this_ = $(this);
    _this_.attr('disabled', true);
    $.ajaxWithAlert ({
        type : 'POST',
        url  : _this_.attr('target'),
        data : { 'comment_id' : _this_.attr('target').split('/')[2] },
        on_success : function(response) {
            _this_.parent().parent().remove();
        },
        on_error : function() {
            _this_.attr('disabled', false);
        }
    });
});

$(document).on("click", '.modify-comment', function(event) { 
    var _this_ = $(this);
    _this_.attr('disabled', true);
    $.ajaxWithAlert({
        type : 'POST',
        url  : _this_.attr('target'),
        data : { 'comment_id' : _this_.attr('target').split('/')[2] },
        on_success : function(response){
            _this_.parent().parent().replaceWith(response.body);
        },
        on_error : function() {
            _this_.attr('disabled', false);
        }
    });
});

$(document).on("click", '.submit-modified-comment', function(event) {
    var _this_ = $(this);
    var body = $(_this_.parent().parent().children()[1]).find('input').val();
    _this_.attr('disabled', true);
    $.ajaxWithAlert({
        type : 'POST',
        url  : _this_.attr('target'),
        data : { 'comment_id' : _this_.attr('target').split('/')[2] , 'body' : body },
        on_success : function(response){
            _this_.parent().parent().replaceWith(response.body);
        },
        on_error : function() {
            _this_.attr('disabled', false);
        }
    });
});