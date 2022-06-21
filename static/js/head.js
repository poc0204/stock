let address_head = 'https://pocworks.store/'
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
        let signout = document.getElementById("signout")
        signout.style.display='block'
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
  fetch(address_head+'api/all_stock')
  .then(response =>{
    return  response.json()
  })
  .then( data =>{
    var test_list = []
    for(i=0;i<=data['data']['data'].length-1;i++){
      test_list.push(data['data']['data'][i]['stock_id']+' '+data['data']['data'][i]['stock_name'])
    }
  
  function AotoComplete(auto ,search ,mylist){
      var autoNode = $("#" + auto);
      var completeList = new Array();
      var n = 0;
      var old_value = $("#" + search).val();
      for (var i in mylist){
          if (mylist[i].indexOf(old_value) == 0){
              completeList[n++] = mylist[i];
          }
      }
      if (completeList.length == 0){
          autoNode.hide();
          return;
      }
      autoNode.empty();
      for (var i in completeList){
          var wordNode = completeList[i];
          var newDivNode = $("<div>").attr("id",i);
              newDivNode.attr("style","font:14px/25px arial;height:25px;width:170px; padding:0 8px;cursor: pointer ;background-color:white;")
              newDivNode.html(wordNode).appendTo(autoNode);
              newDivNode.mouseover(function(){
                  $(this).css("background-color", "#ebebeb");
              });
              newDivNode.mouseout(function(){
                  $(this).css("background-color", "white");
              });
              newDivNode.click(function(){
                  autoNode.hide();

                  var comtext = $(this).text();

                  $("#" + search).val(comtext);
              });
              autoNode.show()
      }
      document.onclick = function (e) {
          var e = e ? e :document.window.event;
          var tar = e.srcElement || e.target;
          if (tar.id != search){
              if ($("#" + auto).is(":visible")){
                  $("#" + auto).css("display", "none")
              }
          }
      }
    }
    $(function (){
        $("#search_text").focus(function(){
            AotoComplete("auto_div", "search_text", test_list);
        });
        $("#search_text").keyup(function (){
            AotoComplete("auto_div", "search_text", test_list);
        })
})
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
function search_stock(){
  let stock_id = document.getElementById('search_text')
  window.location.href =address_head+"stock_name/"+stock_id.value.slice(0,4)
  }
  