let address_member ='http://127.0.0.1:3000/'
document.addEventListener("DOMContentLoaded",function(){

    let amplitude_date =JSON.parse(localStorage.getItem('amplitude_date'))

    if(amplitude_date == null){
        axios.get(address_member+'api/fixt_amplitude').then((res) => {
            localStorage.setItem('amplitude_date', JSON.stringify(res['data']))
        })
    }
    else{ 
        let dt = new Date();
        if(dt.getFullYear()+'-'+(dt.getMonth()+1)+'-'+dt.getDate() != amplitude_date['date']){
            axios.get(address_member+'api/fixt_amplitude').then((res) => {
            localStorage.setItem('amplitude_date', JSON.stringify(res['data']))
            })
        }
    }

    

    $(document).ready(function(){
        var socket = io.connect(); 
        socket.on('api_fitx', function(msg) {
            let LastPrice = document.getElementById("LastPrice");
            let hight_low = document.getElementById("hight_low");
            let now_hight_low = document.getElementById("now_hight_low");
            LastPrice.innerText=msg.LastPrice;
            hight_low.innerText=msg.hight_low;
            now_hight_low.innerText=msg.now_hight_low;
            let fist_level = document.getElementById("fist_level");
            let second_level = document.getElementById("second_level");
            let third_level = document.getElementById("third_level");
            let Four_level = document.getElementById("Four_level");
            let five_level = document.getElementById("five_level");

            if(msg.OpenPrice > msg.LastPrice){
                fist_level.innerText=msg.OpenPrice-amplitude_date['一壘'];
      
                second_level.innerText=msg.OpenPrice-amplitude_date['二壘'];
              
                third_level.innerText=msg.OpenPrice-amplitude_date['三壘'];
           
                Four_level.innerText=msg.OpenPrice-amplitude_date['全壘打'];
              
                five_level.innerText=msg.OpenPrice-amplitude_date['場外全壘打'];
           
                LastPrice.style.color='green'
                if(msg.low < msg.OpenPrice-amplitude_date['一壘']){
                    let fist_level_color = document.getElementById("fist_level_color");
                    fist_level_color.style.backgroundColor='#CCFF99';
                    if(msg.low < msg.OpenPrice-amplitude_date['二壘']){
                        let second_level_color = document.getElementById("second_level_color");
                        second_level_color.style.backgroundColor='#CCFF99';
                        if(msg.low < msg.OpenPrice-amplitude_date['三壘']){
                            let third_level_color = document.getElementById("third_level_color");
                            third_level_color.style.backgroundColor='#CCFF99';
                            if(msg.low < msg.OpenPrice-amplitude_date['全壘打']){
                                let Four_level_color = document.getElementById("Four_level_color");
                                Four_level_color.style.backgroundColor='#CCFF99';
                                if(msg.low < msg.OpenPrice-amplitude_date['場外全壘打']){
                                    let five_level_color = document.getElementById("five_level_color");
                                    five_level_color.style.backgroundColor='#CCFF99';
                                }
                            }
                        }
                    }
                }
                
            }
            else{
                fist_level.innerText=msg.OpenPrice+amplitude_date['一壘'];
              
                second_level.innerText=msg.OpenPrice+amplitude_date['二壘'];
    
                third_level.innerText=msg.OpenPrice+amplitude_date['三壘'];
             
                Four_level.innerText=msg.OpenPrice+amplitude_date['全壘打'];
               
                five_level.innerText=msg.OpenPrice+amplitude_date['場外全壘打'];
               
                LastPrice.style.color='red'
                if(msg.hight > msg.OpenPrice+amplitude_date['一壘']){
                    let fist_level_color = document.getElementById("fist_level_color");
                    fist_level_color.style.backgroundColor='#FFCCCC';
                    if(msg.hight > msg.OpenPrice+amplitude_date['二壘']){
                        let second_level_color = document.getElementById("second_level_color");
                        second_level_color.style.backgroundColor='#FFCCCC';
                        if(msg.hight > msg.OpenPrice+amplitude_date['三壘']){
                            let third_level_color = document.getElementById("third_level_color");
                            third_level_color.style.backgroundColor='#FFCCCC';
                            if(msg.hight > msg.OpenPrice+amplitude_date['全壘打']){
                                let Four_level_color = document.getElementById("Four_level_color");
                                Four_level_color.style.backgroundColor='#FFCCCC';
                                if(msg.hight > msg.OpenPrice+amplitude_date['場外全壘打']){
                                    let five_level_color = document.getElementById("five_level_color");
                                    five_level_color.style.backgroundColor='#FFCCCC';
                                }
                            }
                        }
                    }
                }
               
            }


        });
    });

})