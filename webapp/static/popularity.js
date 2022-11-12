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
    descending = document.getElementById('descending');
    results = document.getElementById('results-list');

    let url = getAPIBaseURL()+'/popularityresults/';
    url+='?';
    url+='variable='+variable.value+'&value='+val.value+'&quantity='+quantity.value+'&descending='+descending.value;

    fetch(url,{method:'get'})
    .then((response) => response.json())
    .then(function(movies){
        let listBody='';
        results.innerHTML+='test';
        for(let i=0; i<movies.length; i++){
            let movie=movies[i];
            listBody+='<li><a href='+movie['imdb_link']+'/ target="_blank">ID: '+movie['id']+', title: '+movie['title']+', release date: '+movie['release_date']+'</a></li>';
        }
        results.innerHTML+=listBody;
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