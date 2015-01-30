$(document).on("click", '.like', function(event) { 
    var _this_ = $(this);
    console.log( _this_.attr('target') );
    _this_.attr('disabled', true);
    $.ajaxWithAlert({
        type : 'POST',
        url  : _this_.attr('target'),
        data : { 'project_id' : _this_.attr('target').split('/')[2] },
        on_success : function(response) {
            _this_.text( response.count );
            if (response.like) {
                _this_.addClass('user-like');
            } else {
                _this_.removeClass('user-like');
            }
        },
        on_finish : function() {
            _this_.attr('disabled', false);
        },
        on_error : function() {
            console.log('error : ' + _this_);
            _this_.attr('disabled', false);
        }
    });
});