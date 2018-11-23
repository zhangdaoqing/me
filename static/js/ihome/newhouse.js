function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function(){
    // $('.popup_con').fadeIn('fast');
    // $('.popup_con').fadeOut('fast');
})
$(document).ready(function (e) {
    $('#form-house-info').submit(function (e) {
        e.preventDefault();//阻止默认提交
        var csrftoken = $("meta[name=csrf-token]").attr("content");
        alert('提交');
        $(this).ajaxSubmit({
            url:'/house/new_house/',
            dataType:'json',
            type:'POST',
            headers:{'X-CSRFToken':csrftoken},

            success:function(data){

                if(data.code == 200){
                    $('.error-msg text-center').hide();
                    $('#form-house-info').hide();
                    $('#form-house-image').show();
                    alert('提交成功')

                }
            },
            error:function (data) {
                $('.error-msg text-center').html(data.msg);
                alert('提交失败')
            }
        })
    })



    $('#form-house-image').submit(function (e) {
        e.preventDefault();//    阻止默认提交
        var csrftoken = $("meta[name=csrf-token]").attr("content");
        $(this).ajaxSubmit({
            url:'/house/new_picture/',
            type: 'POST',
            dataType: 'json',
            headers:{'X-CSRFToken':csrftoken},
            success:function (data) {
                if(data.code == 200){
                    alert('上传成功');


                }
            },

            error:function (data) {
                alert('上传失败');

            }
        })
    })
})