let address_member_sigin = 'http://pocworks.store/'
function create_new_member_click(){
    let new_member_name = document.getElementById("new_member_name")
    let new_member_email = document.getElementById("new_member_email")
    let new_member_password = document.getElementById("new_member_password")
    let new_member_password_confirm = document.getElementById("new_member_password_confirm")
    let new_member_error_massage = document.getElementById("new_member_error_massage")
    if(new_member_name.value === "" || new_member_email.value === ""  || new_member_password.value ===""){
        new_member_error_massage.style.display='block';
        new_member_error_massage.innerHTML = "姓名、信箱、密碼不能為空"
      }
    else if(new_member_password.value.length < 6){
    new_member_error_massage.style.display='block';
    new_member_error_massage.innerHTML = "密碼長度須超過六位數";
    }
    else if(IsEmail(new_member_email.value) === false){
        new_member_error_massage.style.display='block';
        new_member_error_massage.innerHTML = "信箱格式錯誤";
      }
    else if(new_member_password_confirm.value != new_member_password.value){
    new_member_error_massage.style.display='block';
    new_member_error_massage.innerHTML = "密碼不符";
    }
    else{
        let member_data = {
            'name':new_member_name.value,
            'email':new_member_email.value,
            'password':new_member_password.value,
        }
        let url =address_member_sigin+'api/signup';
        fetch(url, 
        {
            method: 'POST',
            body:JSON.stringify(member_data),  
            headers:{
            'Content-Type': 'application/json'
        }
        })
        .then(response =>{
            return  response.json()
        })
        .then(data =>{
            console.log(data['data'])
            console.log(data['data']['success'] === true)
            if(data['data']['success']  === true){
                alert("註冊成功，請重新登入")
                document.location.href=address_member_sigin+'login';
            }
            else{
                if(data['data']['massage']==='帳號重複'){
                    alert("e-mail重複，請重新輸入")
                }
                else{
                    alert("註冊失敗")
                document.location.href=address_member_sigin;
                }
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