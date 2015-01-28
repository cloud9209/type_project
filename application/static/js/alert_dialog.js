var defaultStyle, AlertDialog, AjaxWithAlertDialog;
$(document).ready(function(){
    // TODO : BETTER UI
    defaultStyle = {
        color       :'white',
        display     :'inline-block',
        borderRadius:'.5em',    
        lineHeight  :'1.8em',
        fontWeight  :'bold',
        fontSize    :'1.2em',
        padding     :'0px 10px'
    };
    AlertDialog = function(message, duration) {
        // If a dialog is currently running, show next dialog after the deletion of current one.
        if ($('div#alert_dialog').length > 0) setTimeout('AlertDialog("'+message+'","'+duration+'")');
        else {
            var dialog = '<div id="alert_dialog" style="text-align:center;position:fixed;bottom:20%;width:100%;padding:0px;maring:0px;display:none;z-index:9999;"><span>'+message+'</span></div>';
            $('body').append(dialog);
            $('div#alert_dialog').css(defaultStyle).css('background-color','red').fadeIn(250).delay(duration).fadeOut(250, function(){ $('div#alert_dialog').remove() });
        }
    };

    // TODO : DEFAULT VALUE FOR EACH DATA
    AjaxWithAlertDialog = function(data) {
        $.ajax({
            type : data.type,
            url  : data.url,
            data : data.data,
            error : data.on_error,
            success : function(response) {
                if (response.success) {
                    data.on_success(response);
                } else if (response.action == 'alert') {
                    AlertDialog(response.body, 2000);
                } else {
                    console.log('Unexpected Failure : ' + response);
                }
                if(data.on_finish) data.on_finish();
            }
        })
    };
})
