let address_member_stock ='https://pocworks.store/'
document.addEventListener("DOMContentLoaded",function(){
    fetch(address_member_stock+'api/member_stock_data')
    .then(response =>{
      return  response.json()
    })
    .then( data =>{
        console.log(data)
        for( i = 0; i<=data['data'].length-1;i++ ){
        let color_value;
         color_value = `stock_money_value1`;
        
         let input_group_name = document.getElementById("input_stock_name");
         let tr_data = document.createElement("tr");
         tr_data.id='tr'+i;
         input_group_name.appendChild(tr_data);
         let tr_input = document.getElementById("tr"+i);
         let td_stock_id = document.createElement("td");
         td_stock_id.className=color_value;
         td_stock_id.id='stock_id'+i;
         td_stock_id.innerText=data['data'][i]['stock_id'];
         tr_input.appendChild(td_stock_id)
     
         let td_stock_name = document.createElement("td");
         td_stock_name.className=color_value;
         td_stock_name.id='a_herf'+i
     
         tr_input.appendChild(td_stock_name)
     
         let a_herf = document.getElementById("a_herf"+i);
         let a_herf_data = document.createElement("a");
         a_herf_data.innerText=data['data'][i]['stock_name'];
         a_herf_data.href='/stock_name/'+data['data'][i]['stock_name'];
         a_herf_data.style.color='#448899';
         a_herf.appendChild(a_herf_data)
     
        
        
         let vs_color
        if( isInteger(i/2)){
          vs_color='green'
        }
        else
        vs_color='red'
    
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

        let td_gruop_name = document.createElement("td");
        td_gruop_name.className=color_value;
        td_gruop_name.innerText=data['data'][i]['group_name'];
        tr_input.appendChild(td_gruop_name)

        let delete_data = document.createElement("td");
        delete_data.className=color_value;
        delete_data.id='delete_a'+i
        tr_input.appendChild(delete_data)

        let delete_a = document.getElementById('delete_a'+i);

        let a_herf_delete = document.createElement("a");
        a_herf_delete.href="/api/delete_stock/"+data['data'][i]['stock_id'];
        a_herf_delete.id='delelt_a_img'+i;
        delete_a.appendChild(a_herf_delete)

        let delete_a_img = document.getElementById('delelt_a_img'+i);
        let delete_img = document.createElement("img");
        delete_img.src='/static/images/delete.png';
        delete_img.style.width='30px';
        delete_img.style.hight='30px';
        delete_a_img.appendChild(delete_img)


    }
    })
})

function isInteger(obj) {
    return obj%1 === 0
  }