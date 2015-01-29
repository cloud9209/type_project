// Auth Check, replace with textarea
$(document).on('click', '#btn-description', function(event){
    var _this_ = $(this);
    var is_modifying = $('#description-textarea').length;
    console.log('to '+ (is_modifying? 'submit' : 'modify'));
    if(is_modifying && $('#description-textarea').val() == "") return;

    _this_.attr('disabled', true);
    $.ajaxWithAlert({
        type : 'POST',
        url  : _this_.attr('target'),
        data : is_modifying? {body : $('#description-textarea').val()} : '',
        on_success : function(response) {
            $('#description').replaceWith(response.body);
            $('#btn-description').val(is_modifying? '수정' : '등록');
        },
        on_finish : function() {
            _this_.attr('disabled', false);
        },
        on_error : function() {
            _this_.attr('disabled', false);
        }
    });
});