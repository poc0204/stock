let address = 'http://127.0.0.1:3000/'
document.addEventListener("DOMContentLoaded",function(){
    setTimeout(function(){
        let spinner_size = document.getElementById("spinner_size")
        fadeOut(spinner_size,50);
        spinner_size.style.display='none'
        document.body.style.display = 'contents' ;
        
      },2500);
    
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
      window.location.href =address+"login"
      console.log("login_click")
    }
    
    function signup_click(){
      window.location.href =address+"signup"
      console.log("signup_click")
    }
    
    function member_stock(){
      window.location.href =address+"member"
      console.log("member_stock")
    }
    
