
$.get("/user/my_info/", function(data){

    if (data.code = 200) {

        $('#user-name').html(data.user_info.phone);
        $('#user-mobile').html(data.user_info.name);
        $('#user-avatar').attr('src','/static/media/'+ data.user_info.avatar);
    }
})


$(document).ready(function(){
})