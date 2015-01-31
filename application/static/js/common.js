$(document).ready(function(){
    // Loading Sprite
    var sprite_image = $('<img src="/static/res/images/loading.gif"></img>')
    sprite_image
    .css('width', '200px')
    .css('height', '200px')
    sprite_image
    .css('left', ($(window).width() - sprite_image.width())/2)
    .css('top', ($(window).height() - sprite_image.height())/2)
    .css('padding', '0px')
    .css('margin', '0px')
    .css('position', 'fixed')
    
    $.sprite = $('<div id="loading" position="absolute"></div>');
    $.sprite
    .width($(window).width())
    .height($(window).height())
    .css('background-color', 'rgba(255,255,255,0.5)')
    .css('z-index', '9999')
    .css('padding', '0px')
    .css('margin', '0px')
    .css('position', 'fixed')
    .css('left', '0')
    .css('top', '0')
    .append(sprite_image);

    $.sprite_on = function(src_url) {
        $('body').append($.sprite);
    }
    $.sprite_off = function(Src_url) {
        if($('#loading').length > 0) $('#loading').remove();
    }

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
        $.sprite_on();
        $.ajax({
            type : data.type,
            url  : data.url,
            data : data.data,
            error : function() {
                data.on_error();
                $.sprite_off();
            },
            success : function(response) {
                if (response.success) {
                    data.on_success(response);
                } else if (response.action == 'alert') {
                    $.alert(response.body, 1500);
                } else {
                    console.log('Unexpected Failure : ' + response);
                }
                if(data.on_finish) data.on_finish();
                $.sprite_off();
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
});
$(document).on('change', 'input[type="file"]', function(){
    if (this.files && this.files[0]) {
        var reader = new FileReader();
        reader.onload = function(e) {
            $('#thumbnail').attr('src', e.target.result);
        }
        reader.readAsDataURL(this.files[0])
    }
});