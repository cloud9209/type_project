//var defaultStyle, $.alert, $.ajaxWithAlert;
$(document).ready(function(){
    // TODO : BETTER UI
    var defaultStyle = {
        color       :'white',
        display     :'inline-block',
        borderRadius:'.5em',    
        lineHeight  :'1.8em',
        fontWeight  :'bold',
        fontSize    :'1.2em',
        padding     :'0px 10px'
    };
    $.alert = function(message, duration) {
        // If a dialog is currently running, show next dialog after the deletion of current one.
        if ($('div#alert_dialog').length > 0) setTimeout('$.alert("'+message+'","'+duration+'")');
        else {
            var dialog = '<div id="alert_dialog" style="text-align:center;position:fixed;bottom:20%;width:100%;padding:0px;maring:0px;display:none;z-index:9999;"><span>'+message+'</span></div>';
            $('body').append(dialog);
            $('div#alert_dialog').css(defaultStyle).css('background-color','red').fadeIn(250).delay(duration).fadeOut(250, function(){ $('div#alert_dialog').remove() });
        }
    };

    // TODO : DEFAULT VALUE FOR EACH DATA
    $.ajaxWithAlert = function(data) {
        $.ajax({
            type : data.type,
            url  : data.url,
            data : data.data,
            error : data.on_error,
            success : function(response) {
                if (response.success) {
                    data.on_success(response);
                } else if (response.action == 'alert') {
                    $.alert(response.body, 1500);
                } else {
                    console.log('Unexpected Failure : ' + response);
                }
                if(data.on_finish) data.on_finish();
            }
        })
    };

    $("form").submit(function(e){
        var form = $(this);
        var submit_btn = $(this).find('[type="submit"]');
        submit_btn.attr('disabled', true);
        $.ajaxWithAlert({
            url   : form.attr('action'),
            type  : form.attr('method'),
            data  : form.serialize(),
            on_success: function(response){
                if (response.action == 'redirect') {
                    window.location.href = response.body;
                }
            },
            on_finish : function(){
                submit_btn.attr('disabled', false)
            },
            on_error  : function(){
                submit_btn.attr('disabled', false)
            }
        });
        return false;
    });
})
