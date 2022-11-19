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
    first_movie = document.getElementById('firstmovie');
    second_movie = document.getElementById('secondmovie');
    // var detailed = document.querySelector('#detailed');
    var movie1_title = document.getElementById('movie1title');
    var movie2_title = document.getElementById('movie2title');
    var movie1_revenue = document.getElementById('movie1revenue');
    var movie2_revenue = document.getElementById('movie2revenue');
    var movie1_budget = document.getElementById('movie1budget');
    var movie2_budget = document.getElementById('movie2budget');
    var movie1_runtime = document.getElementById('movie1runtime');
    var movie2_runtime = document.getElementById('movie2runtime');

    let url = getAPIBaseURL()+'/comparisonresults/';
    url+='?';
    url+='firstmovie='+first_movie.value+'&secondmovie='+second_movie.value+'&detailed=';
    if (detailed.checked){
        url+=detailed.value;
    }
    fetch(url,{method:'get'})
    .then((response) => response.json())
    .then(function(movies){
        firstmoviedata = movies[0];
        secondmoviedata = movies[1];
        movie1_title.innerHTML='<option>'+firstmoviedata['title']+'</option>';
        movie2_title.innerHTML='<option>'+secondmoviedata['title']+'</option>';
        let dollarUSLocale = Intl.NumberFormat('en-US');
        movie1_revenue.innerHTML = '$'+dollarUSLocale.format(firstmoviedata['revenue']);
        movie2_revenue.innerHTML = '$'+dollarUSLocale.format(secondmoviedata['revenue']);
        movie1_budget.innerHTML = '$'+dollarUSLocale.format(firstmoviedata['budget']);
        movie2_budget.innerHTML = '$'+dollarUSLocale.format(secondmoviedata['budget']);
        movie1_runtime.innerHTML = firstmoviedata['runtime']+' m';
        movie2_runtime.innerHTML = secondmoviedata['runtime']+' m';
    })
    .catch(function(error){
        console.log(error);
    })
}

function initialize(){
    var button = document.getElementById('submission');
    button.onclick = onButtonPress;

    var list1 = document.getElementById('firstmoviedroplist');
    var list2 = document.getElementById('secondmoviedroplist');
    let url = getAPIBaseURL()+'/listload/';

    fetch(url,{method:'get'})
    .then((response) => response.json())
    .then(function(movies){
        let listBody='';
        for(i=0; i<movies.length; i++){
            movie=movies[i];
            //listBody+='<option value=\''+movie['title']+' ('+movie['release_date']+') [id:'+movie['id']+']\'>';
            listBody+='<option value=\''+movie['title']+'\'>'+' ('+movie['release_date']+')</option>';
        }
        list1.innerHTML=listBody;
        list2.innerHTML=listBody;
    })
}

window.onload=initialize;