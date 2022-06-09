let address_index = 'https://pocworks.store/'
document.addEventListener("DOMContentLoaded",function(){

  fetch(address_index+`api/stock_money`, {method: 'get'})
  .then(response =>{
    return  response.json()
  })
  .then( data =>{
    if(data['data']['tws']['up_or_down_point'][0] =='+'){
      tws_color = 'red';
    }
    else
      tws_color ='green';
    let tws = document.getElementById("tws");
    let tws_data = document.createElement("span");
    tws_data.innerText=data['data']['tws']['tws']
    tws_data.style.color=tws_color;
    tws.appendChild(tws_data)

    let up_or_down = document.getElementById("up_or_down");
    let up_or_down_data = document.createElement("span");
    up_or_down_data.innerText=data['data']['tws']['up_or_down']
    up_or_down_data.style.color=tws_color;
    up_or_down.appendChild(up_or_down_data)

    let up_or_down_point = document.getElementById("up_or_down_point");
    let up_or_down_point_data = document.createElement("span");
    up_or_down_point_data.innerText=data['data']['tws']['up_or_down_point']
    up_or_down_point_data.style.color=tws_color;
    up_or_down_point.appendChild(up_or_down_point_data)

    let tws_money = document.getElementById("tws_money");
    let tws_money_data = document.createElement("span");
    tws_money_data.innerText=data['data']['tws']['tws_money']
    tws_money.appendChild(tws_money_data)
    function isInteger(obj) {
      return obj%1 === 0
    }
    for(var i = 0 ; i<=data['data']['data'].length-1;i++){
      let color_value;
      if( isInteger(i/2)){
        color_value = `stock_money_value1`;
      }
      else
        color_value = `stock_money_value2`;
      let input_stock_money = document.getElementById("input_stock_money");
      let tr_data = document.createElement("tr");
      tr_data.id='tr'+i;
      input_stock_money.appendChild(tr_data);
      let tr_input = document.getElementById("tr"+i);
      let td_name = document.createElement("td");
      td_name.className=color_value;
      td_name.id='a_herf'+i;
      tr_input.appendChild(td_name)
      let a_herf = document.getElementById("a_herf"+i);
      let a_herf_data = document.createElement("a");
      a_herf_data.innerText=data['data']['data'][i]['name']
      a_herf_data.style.color='#448899'
      a_herf_data.href='/gruop_name/'+data['data']['data'][i]['name']
      a_herf.appendChild(a_herf_data)

      let td_today = document.createElement("td");
      td_today.className=color_value;
      td_today.innerText=data['data']['data'][i]['today']+'%';
      tr_input.appendChild(td_today)

      let td_yestday = document.createElement("td");
      td_yestday.className=color_value;
      td_yestday.innerText=data['data']['data'][i]['yestday']+'%';
      tr_input.appendChild(td_yestday)

      let vs_color
      if(data['data']['data'][i]['vs'] < 0.00 ){
        vs_color='green'
      }
      else
      vs_color='red'
      let td_vs = document.createElement("td");
      td_vs.className=color_value;
      td_vs.innerText=data['data']['data'][i]['vs']+'%';
      td_vs.style.color=vs_color
      tr_input.appendChild(td_vs)

    }
  })

})

