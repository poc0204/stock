
let address_member ='https://pocworks.store/'


document.addEventListener("DOMContentLoaded",function(){
    axios.get(address_member+'api/member').then((res) => {
        let member_name = document.getElementById('name');
        let member_mail = document.getElementById('member_mail');
        member_name.innerText=res['data']['data']['member_name']
        member_mail.innerText=res['data']['data']['e-mail']

        console.log(res['data']['data']['member_name'])
    })
    let img = document.getElementById("member_img") 
    let url = address_member+'member_get_image'
    axios.get(url).then((res) => {
        img.src=''
        img.src='https://stock-member-image.s3.amazonaws.com/'+res['data']['data']
        img.style.width='300px'
    })


    let inputFile = document.getElementById('file-upload');
    inputFile.addEventListener('change', function(event) {
        const file_data = event.target.files[0]; // 檔案資訊
        const file_max = 1024*1024*3
        if (file_data.size > file_max){
            alert('檔案不能超過3M')
        }
        else{
        document.getElementById('member_img').src = URL.createObjectURL(file_data);
        
        }
    }, false);

    let password_new_check = document.getElementById('password_new_check');
    password_new_check.addEventListener('mouseout', function(){
        let password_new = document.getElementById('password_new').value;
       if(password_new != password_new_check.value){
        let password_error = document.getElementById('password_error').innerText="密碼不一致"
       }
       else if(password_new != "" && password_new_check.value =="" ){
        let password_error = document.getElementById('password_error').innerText="密碼不能空"
       }
       else{
        let password_error = document.getElementById('password_error').innerText=""
       }
    })

    let password_new = document.getElementById('password_new');
    password_new.addEventListener('mouseout', function(){
        
        if(password_new.value.length == 0){
            let password_new_error = document.getElementById('password_new_error').innerText="";      
        }
        else if(password_new.value.length < 6){
            let password_new_error = document.getElementById('password_new_error').innerText="密碼長度須超過六位數";      
        }
        else{
            let password_new_error = document.getElementById('password_new_error').innerText="";      
        }
    })

   

})



function member_update_image(){
    var formData = new FormData();
    var fileField = document.querySelector("input[type='file']");
    if(fileField.files[0] == undefined){
        alert('尚未選擇檔案')

    }
    else{
        formData.append('image_data', fileField.files[0]);
    
        let image_update = document.getElementById('image_update');
        image_update.innerHTML="上傳中";
        let image_update_loading = document.createElement('img')
        image_update_loading.style.margin="-3px";
        image_update_loading.style.padding="0px 4px";
        image_update_loading.src="/static/images/loading.gif";
        image_update.append(image_update_loading)
        formData.append('image_data', fileField.files[0]);
        axios.post(address_member+'member_put_image',formData).then((res) => {
            if (res['data']['data']['massage'] === 'success') {
                let image_update = document.getElementById('image_update').innerText="";     
                alert('上傳成功')
            }
        })
    }
}

function member_update_password(){
 
    let password_old = document.getElementById('password_old');
    let password_new = document.getElementById('password_new');
    let password_new_error = document.getElementById('password_new_error');
    let password_error = document.getElementById('password_error');
    console.log(password_error.innerText == '')
    if(password_old.value == '' | password_new.value == '' ){
        alert('請輸入密碼')
    }
    else if(password_new_error.innerText != '' | password_error.innerText != ''){
        alert('密碼格式有問題')
    }
    else{
        let password_update = document.getElementById('password_update');
        password_update.innerHTML="更新中";
        let password_update_loading = document.createElement('img')
        password_update_loading.id='password_update_loading_image'
        password_update_loading.style.margin="-3px";
        password_update_loading.style.padding="0px 4px";
        password_update_loading.src="/static/images/loading.gif";
        password_update.append(password_update_loading)
        axios.post(address_member+'check_member_password',{
            password_old: password_old.value,
            password_new:password_new.value

        })
        .then((res)=> {
            if(res['data']['data']['success'] == false){
                alert('密哪錯誤')
                password_update.innerHTML="";
                let password_update_loading_image = document.getElementById('password_update_loading_image');
                password_update_loading_image.src=""
            }
            else{
                alert('更新成功')

                document.location.href='/'+'login'
            }
        })
    }

}