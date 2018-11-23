function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}
$(document).ready(function () {
    $('#form-auth').submit(function(e) {
        e.preventDefault();// 阻止默认提交
        var csrftoken = $("meta[name=csrf-token]").attr("content");
        var real_name = $('#real-name').val()
        var id_card = $('#id-card').val()
        $.ajax({
            url: '/user/user_auth/',
            data: {'real_name': real_name, 'id_card': id_card},
            dataType: 'json',
            type: 'PATCH',
            headers: {'X-CSRFToken': csrftoken},
            success: function (data) {
                if (data.code == 200) {
                    $('.btn-success').hide()
                }
                if (data.code == 500) {
                    $('.error-msg').html(data.msg)
                    $('.error-msg').show()
                }

            }
        })
    })
})
