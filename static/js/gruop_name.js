let gruop_name = location.href
gruop_name = gruop_name.substring(33,100)


document.addEventListener("DOMContentLoaded",function(){
    
fetch(`/api/gruop_name/${gruop_name}`, {method: 'GET'})
.then(response =>{
  return  response.json()
})
.then( data =>{

    console.log(data)

    let group_name = document.getElementById("group_name");
    group_name.innerText=data['data'][0]['group_name'];
    let group_name_third = document.getElementById("group_name_third");
    group_name_third.innerText=data['data'][0]['group_name'];
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
    td_stock_name.innerText=data['data'][i]['stock_name'];
    tr_input.appendChild(td_stock_name)

    let td_stock_close = document.createElement("td");
    td_stock_close.className=color_value;
    td_stock_close.innerText=data['data'][i]['close'];
    tr_input.appendChild(td_stock_close)

    let td_stock_spread = document.createElement("td");
    td_stock_spread.className=color_value;
    td_stock_spread.innerText=data['data'][i]['spread'];
    tr_input.appendChild(td_stock_spread)

    
    let td_stock_spread_point = document.createElement("td");
    td_stock_spread_point.className=color_value;
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
  }

})
})
function isInteger(obj) {
  return obj%1 === 0
}