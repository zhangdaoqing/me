function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function(){
    $('#form-avatar').submit(function(e){
        e.preventDefault();// 阻止默认提交
        var csrftoken = $("meta[name=csrf-token]").attr("content");
        $(this).ajaxSubmit({
            url:'/user/profile/',
            dataType:'json',
            type:'PATCH',
            headers:{'X-CSRFToken':csrftoken},

            success:function (data) {

                if(data.code == 200){

                    $('#user-avatar').attr('src','/static/media/'+ data.user_info.avatar);
                }
            },
            error:function () {
                alert('上传失败');
            }
        })
    })

    $('#form-name').submit(function (e) {
        e.preventDefault();// 阻止默认提交
        var csrftoken = $("meta[name=csrf-token]").attr("content");
        var username = $('#user-name').val()
        $.ajax({
            url:'/user/user_name/',
            dataType: 'json',
            type: 'PATCH',
            headers:{'X-CSRFToken':csrftoken},
            data:{'username':username},
            success:function(data){
                if(data.code == 200){
                alert('保存成功')
                }
            },
            error:function () {
                alert('保存失败')
            }
        })
    })

})