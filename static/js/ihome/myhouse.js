$(document).ready(function(){
    // $(".auth-warn").show();
    // $(".page-title").show();

    $.get('/user/user_user_auth/',function (data) {
        if(data.code == 200){
             // alert('hmp')
             $(".auth-warn").hide();
             $("#houses-list").show();
             $.get('/house/new_user_picture/',function (data) {
                 if (data.code == 200) {
                     // $('.house-title').html('<h3>' + data.to_dict.to_dict.id + '--' + data.to_dict.to_dict.title + '</h3>');
                     var html=template('house_list',{hlist:data.to_dict});
                     $('#houses-list').append(html)
             }
         })
        }
        else{
            // alert('mmp')
            $(".auth-warn").show();
             $("#houses-list").hide();
        }
    })
})
// $.get('/house/new_user_picture/',function (data) {
    //     if(data.code==200){
    //         $('.house-title').html('<h3>'+data.to_dict.id + '--' + data.to_dict.title + '</h3>');
            // $(.).html(data.to_dict.title);
            // $(.).html(data.to_dict.price);
            // $(.).html(data.to_dict.create_time);
            // $(.).html(data.to_dict.area);
            // $(.).html(data.house_url);
            // $(.).html(data.house_url);
            // $('#house-title').append(html);
    //     }
    //
    // })


