/* 
    popularity.js
    Aaron Bronstone/Jack Owens
    For CS257 Software Design, Carleton College Fall 2022
*/

function getAPIBaseURL(){
    let baseURL=window.location.protocol+'//'+window.location.hostname+':'+window.location.port+'/api';
    return baseURL;
}

function onButtonPress(){
    variable = document.getElementById('variable');
    val = document.getElementById('value');
    quantity = document.getElementById('quantity');
    var descending = document.querySelector('#descending');
    var results = document.getElementById('results-list');
    let url = getAPIBaseURL()+'/popularityresults/';
    url+='?';
    url+='variable='+variable.value+'&value='+val.value+'&quantity='+quantity.value+'&descending=';
    if (descending.checked){
        url+=descending.value;
    }
    let dollarUSLocale = Intl.NumberFormat('en-US');
    results.innerHTML='Loading...';
    fetch(url,{method:'get'})
    .then((response) => response.json())
    .then(function(entities){
        let listBody='';
        results.innerHTML+='test';
        for(let i=0; i<quantity.value; i++){
            let listString = '';
            let entity=entities[i];
            if (entity['criteria']){
                listString='<li>'+entity['title']+'   '+entity['criteria']+'</li>';
            }
            else {
                listString+='<li>'+entity['title']+'</li>';
            }
            if ((val.value.localeCompare('budget') == 0 || val.value.localeCompare('revenue') == 0) && (entity['criteria'])) {
                listString='<li>'+entity['title']+'  $'+dollarUSLocale.format(entity['criteria'])+'</li>';
            }
            listBody+=listString;
                
        }
        results.innerHTML=listBody;
    })
    .catch(function(error){
        console.log(error);
    })
}

function initialize(){
    var button = document.getElementById('submission');
    button.onclick = onButtonPress;
}

window.onload=initialize;