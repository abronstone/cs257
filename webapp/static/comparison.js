/* 
    comparison.js
    Aaron Bronstone/Jack Owens
    For CS257 Software Design, Carleton College Fall 2022
*/

function getAPIBaseURL(){
    let baseURL=window.location.protocol+'//'+window.location.hostname+':'+window.location.port+'/api';
    return baseURL;
}

function onButtonPress(){
    first_movie = document.getElementById('movie1');
    second_movie = document.getElementById('movie2');
    // var detailed = document.querySelector('#detailed');
    var results = document.getElementById('criteria1a');

    let url = getAPIBaseURL()+'/popularityresults/';
    results.innerHTML = 'Loading...'
    url+='?';
    url+='firstmovie='+first_movie.value+'&secondmovie='+second_movie.value+'&detailed=';
    if (detailed.checked){
        url+=detailed.value;
    }
    results.innerHTML='Loading...'
    // fetch(url,{method:'get'})
    // .then((response) => response.json())
    // .then(function(entities){
    //     let listBody='';
    //     results.innerHTML+='test';
    //     for(let i=0; i<quantity.value; i++){
    //         let entity=entities[i];
    //         listBody+='<li>'+entity['title']+'</li>';
    //     }
    //     results.innerHTML=listBody;
    // })
    // .catch(function(error){
    //     console.log(error);
    // })
}

function initialize(){
    var button = document.getElementById('submission');
    button.onclick = onButtonPress;
}

window.onload=initialize;