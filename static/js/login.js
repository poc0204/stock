let address_login = 'http://pocworks.store/'

function login_click(){
    let email = document.getElementById("member_email")
    let password = document.getElementById("member_password")
    let error_massage = document.getElementById("error_massage")
    if(IsEmail(email.value) === false){
        error_massage.style.display='block';
        error_massage.innerHTML = "信箱格式錯誤"
        }
    else if(email.value === "" || password.value === "" ){
        error_massage.style.display='block';
        error_massage.innerHTML = "信箱、密碼不能為空"
    }
    else if(password.value.length < 6){
        error_massage.style.display='block';
        error_massage.innerHTML = "密碼長度須超過六位數";
    }
    else{
        error_massage.style.display= "none" ;
        let member_data = {
            'email':email.value,
            'password':password.value,
        }
        let url = address_login+`api/login`;
        fetch(url, 
        {
          method: 'PATCH',
          body:JSON.stringify(member_data),  
          headers:{
          'Content-Type': 'application/json'
          }
        })

        .then(response =>{
            return  response.json()
        })
        .then( data =>{
            if(data['data']['success'] == false){
                error_massage.style.display='block';
                error_massage.innerHTML = data['data']['massage'];
            }
            else{
                alert("登入成功")
                document.location.href='/'
            }
        })
    }
}
function IsEmail(email) {
    let regex =  /^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$/; 
    if(!regex.test(email)) {
        return false;
    }else{
        return true;
    }
}