$(document).on("click", '.like', function(event) { 
    var _this_ = $(this);
    console.log( _this_.attr('target') );
    _this_.attr('disabled', true);
    $.ajax({
        type : 'POST',
        url  : _this_.attr('target'),
        data : { 'project_id' : _this_.attr('target').split('/')[2] },
        success : function(response) {
            if ( response.success ) {
                _this_.text( response.count );
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