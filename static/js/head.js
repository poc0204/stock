let address_head = 'http://127.0.0.1:3000/'
document.addEventListener("DOMContentLoaded",function(){
  fetch(address_head+'api/member')
  .then(response =>{
    return  response.json()
  })
  .then( data =>{
      if(data['data']['member'] == false){
        let member_name = document.getElementById("member_name")
        member_name.style.display='none'
        let signout = document.getElementById("signout")
        signout.style.display='none'
      }
      else{
        let login = document.getElementById("login")
        login.style.display='none'
        let signup = document.getElementById("signup")
        signup.style.display='none'
        let member_name = document.getElementById("member_name")
        member_name.innerText='Hi! '+data['data']['member_name']
      }

  })
  setTimeout(function(){
    let spinner_size = document.getElementById("spinner_size")
    fadeOut(spinner_size,50);
    spinner_size.style.display='none'
    document.body.style.display = 'contents' ;
    
  },1500);

      
    })
    
    
    function fadeIn(element,speed){
        if(element.style.opacity !=1){
            var speed = speed || 50 ;
            var num = 0;
            var st = setInterval(function(){
            num++;
            element.style.opacity = num/10;
            if(num>=10)  {  clearInterval(st);  }
            },speed);
        }
      }
      
      function fadeOut(element,speed){
        if(element.style.opacity !=0){
            var speed = speed || 50 ;
            var num = 10;
            var st = setInterval(function(){
            num--;
            element.style.opacity = num / 10 ;
            if(num<=0)  {   clearInterval(st);  }
            },speed);
        }
      
      }
    
    function login_click(){
      window.location.href =address_head+"login"
    }
    
    function signup_click(){
      window.location.href =address_head+"signup"
    }
    
    function member_stock(){
      window.location.href =address_head+"member_stock"
      console.log("member_stock")
    }
    
    function signout_click(){
      window.location.href =address_head+"signout"
    }
    