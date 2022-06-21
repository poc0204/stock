let gruop_name = location.href
gruop_name = gruop_name.substring(33,100)


document.addEventListener("DOMContentLoaded",function(){
  fetch(`/api/gruop/${gruop_name}`, {method: 'GET'})
  .then(response =>{
    return  response.json()
  })
  .then( data =>{
    if(data['data']['up_or_down_point'][0] =='+'){
      stock_color = 'red';
    }
    else
    stock_color ='green';
    let stock = document.getElementById("group");
    let stock_data = document.createElement("span");
    stock_data.innerText=data['data']['group_price']
    stock_data.style.color=stock_color;
    stock.appendChild(stock_data)

    let up_or_down = document.getElementById("group_up_or_down");
    let up_or_down_data = document.createElement("span");
    up_or_down_data.innerText=data['data']['up_or_down']
    up_or_down_data.style.color=stock_color;
    up_or_down.appendChild(up_or_down_data)

    let up_or_down_point = document.getElementById("group_up_or_down_point");
    let up_or_down_point_data = document.createElement("span");
    up_or_down_point_data.innerText=data['data']['up_or_down_point']
    up_or_down_point_data.style.color=stock_color;
    up_or_down_point.appendChild(up_or_down_point_data)

    let stock_money = document.getElementById("group_money");
    let stock_money_data = document.createElement("span");
    stock_money_data.innerText=data['data']['group_money']
    stock_money.appendChild(stock_money_data)
  })
fetch(`/api/gruop_name/${gruop_name}`, {method: 'GET'})
.then(response =>{
  return  response.json()
})
.then( data =>{
    let group_name = document.getElementById("group_name");
    group_name.innerText='上市'+data['data'][0]['group_name'];
    let group_name_third = document.getElementById("group_name_third");
    group_name_third.innerText='上市'+data['data'][0]['group_name'];
    for(var i = 0 ; i<=data['data'].length-1;i++){
    let color_value;
    if( isInteger(i/2)){
      color_value = `stock_money_value1`;
    }
    else
      color_value = `stock_money_value2`;
    let input_group_name = document.getElementById("input_group_name");
    let tr_data = document.createElement("tr");
    tr_data.id='tr'+i;
    input_group_name.appendChild(tr_data);
    let tr_input = document.getElementById("tr"+i);
    let td_stock_id = document.createElement("td");
    td_stock_id.className=color_value;
    td_stock_id.innerText=data['data'][i]['stock_id'];
    tr_input.appendChild(td_stock_id)

    let td_stock_name = document.createElement("td");
    td_stock_name.className=color_value;
    td_stock_name.id='a_herf'+i

    tr_input.appendChild(td_stock_name)

    let a_herf = document.getElementById("a_herf"+i);
    let a_herf_data = document.createElement("a");
    a_herf_data.innerText=data['data'][i]['stock_name'];
    a_herf_data.href='/stock_name/'+data['data'][i]['stock_id'];
    a_herf_data.style.color='#448899';
    a_herf.appendChild(a_herf_data)

    let vs_color
    if(data['data'][i]['spread'] <= 0.00){
      vs_color ='green';
      }
    else
      vs_color = 'red';

    let td_stock_close = document.createElement("td");
    td_stock_close.className=color_value;
    td_stock_close.style.color=vs_color;
    td_stock_close.innerText=data['data'][i]['close'];
    tr_input.appendChild(td_stock_close)

    let td_stock_spread = document.createElement("td");
    td_stock_spread.className=color_value;
    td_stock_spread.style.color=vs_color;
    td_stock_spread.innerText=data['data'][i]['spread'];
    tr_input.appendChild(td_stock_spread)

    
    let td_stock_spread_point = document.createElement("td");
    td_stock_spread_point.className=color_value;
    td_stock_spread_point.style.color=vs_color;
    td_stock_spread_point.innerText=data['data'][i]['spread_point'];
    tr_input.appendChild(td_stock_spread_point)
 
    let td_stock_open = document.createElement("td");
    td_stock_open.className=color_value;
    td_stock_open.innerText=data['data'][i]['open'];
    tr_input.appendChild(td_stock_open)
    
    let td_stock_hight = document.createElement("td");
    td_stock_hight.className=color_value;
    td_stock_hight.innerText=data['data'][i]['hight'];
    tr_input.appendChild(td_stock_hight)

    let td_stock_low = document.createElement("td");
    td_stock_low.className=color_value;
    td_stock_low.innerText=data['data'][i]['low'];
    tr_input.appendChild(td_stock_low)

    let td_stock_yestday = document.createElement("td");
    td_stock_yestday.className=color_value;
    td_stock_yestday.innerText=data['data'][i]['td_stock_yestday']
    tr_input.appendChild(td_stock_yestday)

    let td_stock_Trading_Volume = document.createElement("td");
    td_stock_Trading_Volume.className=color_value;
    td_stock_Trading_Volume.innerText=data['data'][i]['Trading_Volume'];
    tr_input.appendChild(td_stock_Trading_Volume)

    let add_data = document.createElement("td");
    add_data.className=color_value;
    add_data.id='add_stock_a'+i
    tr_input.appendChild(add_data)

    let add_data_a = document.getElementById('add_stock_a'+i);

    let a_herf_add = document.createElement("a");
    a_herf_add.href="/api/add_stock/"+data['data'][i]['stock_id'];
    a_herf_add.id='add_data_a_image'+i;
    a_herf_add.innerText='立即追蹤'
    a_herf_add.style.color='#448899';
    add_data_a.appendChild(a_herf_add)

  }

})
})
function isInteger(obj) {
  return obj%1 === 0
}