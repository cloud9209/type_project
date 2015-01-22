$(document).ready(function(){
    $('.work_like').click(function(){
        console.log('/work/' + $(this).find('div').attr('data') + '/like');
        $.ajax({
            type : 'POST',
            url  : '/work/' + $(this).find('div').attr('data') + '/like', // inject work id into html via jinja
            data : '',

            success : function(resp) {
                console.log('success : ' + resp);
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