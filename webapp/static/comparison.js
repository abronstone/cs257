/* 
    comparison.js
    Aaron Bronstone/Jack Owens
    For CS257 Software Design, Carleton College Fall 2022
*/

function getAPIBaseURL(){
    let baseURL=window.location.protocol+'//'+window.location.hostname+':'+window.location.port+'/api';
    return baseURL;
}

function colorCompare(firstElementId,firstValue,secondElementId,secondValue){
    /*
        Compares two values of a specific movie metadata, and highlights the larger HTML element in green.

        If either of the values are null, all colors are removed as it is an unfair comparison.
    */
    var elementOne = document.getElementById(firstElementId);
    var elementTwo = document.getElementById(secondElementId);
    if(firstValue!='None' && secondValue!='None'){
        if(firstValue>secondValue){
            elementOne.style.backgroundColor='greenyellow';
            elementTwo.style.backgroundColor='';
        }else if(firstValue<secondValue){
            elementOne.style.backgroundColor='';
            elementTwo.style.backgroundColor='greenyellow';
        }
    }else{
        elementOne.style.backgroundColor='';
        elementTwo.style.backgroundColor='';
    }
}

function onButtonPress(){
    /*
        Submits the following URL:
            getAPIBaseURL()+'/comparisonresults/?firstmovie={first movie id}&secondmovie={second movie id}'
        
        Changes each movies' corresponding popularity, revenue, budget, rating, and runtime elements in 'mockup5.html':COMPARISON

        If the 'detailed' checkbox is checked, adds the director and release date of each
    */
    first_movie = document.getElementById('firstmovie');
    second_movie = document.getElementById('secondmovie');
    var detailed = document.querySelector('#detailed');
    var movie1_title = document.getElementById('movie1title');
    var movie2_title = document.getElementById('movie2title');
    var movie1_popularity = document.getElementById('movie1popularity');
    var movie2_popularity = document.getElementById('movie2popularity');
    var movie1_revenue = document.getElementById('movie1revenue');
    var movie2_revenue = document.getElementById('movie2revenue');
    var movie1_budget = document.getElementById('movie1budget');
    var movie2_budget = document.getElementById('movie2budget');
    var movie1_runtime = document.getElementById('movie1runtime');
    var movie2_runtime = document.getElementById('movie2runtime');
    var movie1_rating=document.getElementById('movie1rating');
    var movie2_rating=document.getElementById('movie2rating');

    let url = getAPIBaseURL()+'/comparisonresults/';
    url+='?';
    url+='firstmovie='+first_movie.value+'&secondmovie='+second_movie.value+'&detailed=';
    if (detailed.checked){
        url+=detailed.value;
    }
    fetch(url,{method:'get'})
    .then((response) => response.json())
    .then(function(movies){

        movieOne = movies[0];
        movieTwo = movies[1];



        movie1_title.innerHTML='<strong>'+movieOne['title']+'</strong>';
        movie2_title.innerHTML='<strong>'+movieTwo['title']+'</strong>';

        colorCompare('movie1popularity',movieOne['popularity'],'movie2popularity',movieTwo['popularity']);
        movie1_popularity.innerHTML = movieOne['popularity'];
        movie2_popularity.innerHTML = movieTwo['popularity'];

        let dollarUSLocale = Intl.NumberFormat('en-US');
        colorCompare('movie1revenue',movieOne['revenue'],'movie2revenue',movieTwo['revenue']);
        movie1_revenue.innerHTML = '$'+dollarUSLocale.format(movieOne['revenue']);
        movie2_revenue.innerHTML = '$'+dollarUSLocale.format(movieTwo['revenue']);

        colorCompare('movie1budget',movieOne['budget'],'movie2budget',movieTwo['budget']);
        movie1_budget.innerHTML = '$'+dollarUSLocale.format(movieOne['budget']);
        movie2_budget.innerHTML = '$'+dollarUSLocale.format(movieTwo['budget']);

        colorCompare('movie1rating',movieOne['rating'],'movie2rating',movieTwo['rating']);
        movie1_rating.innerHTML = movieOne['rating'];
        movie2_rating.innerHTML = movieTwo['rating'];

        movie1_runtime.innerHTML = movieOne['runtime']+' min';
        movie2_runtime.innerHTML = movieTwo['runtime']+' min';

        if(detailed.checked){
            var results = document.getElementById('table');
            if(results.innerHTML.indexOf('Director')==-1){
                results.innerHTML+='<tr><th style="background-color:rgb(204, 165, 204)">Director</th><td>'+movieOne['director']+'</td><td id="movie2runtime">'+movieTwo['director']+'</td></tr>'
                results.innerHTML+='<tr><th style="background-color:rgb(204, 165, 204)">Release Date</th><td>'+movieOne['release-date']+'</td><td id="movie2runtime">'+movieTwo['release-date']+'</td></tr>'
            }
        }
    })
    .catch(function(error){
        console.log(error);
    })
}

function updateFirstList(){
    /*
        Calls to API endpoint '/listload/' to dynamically update the datalist for the first movie's input
    */
    var list = document.getElementById('firstmoviedroplist');
    var input = document.getElementById('firstmovie');
    let url = getAPIBaseURL()+'/listload/';
    url+='?title='+input.value

    fetch(url,{method:'get'})
    .then((response) => response.json())
    .then(function(movies){
        let listBody='';
        for(i=0; i<movies.length; i++){
            movie=movies[i];
            listBody+='<option value=\''+movie['id']+'\'>'+movie['title']+' ('+movie['release_date']+')</option>';
        }
        list.innerHTML=listBody
    })
}

function updateSecondList(){
    /*
        Calls to API endpoint '/listload/' to dynamically update the datalist for the second movie's input
    */
    var list = document.getElementById('secondmoviedroplist');
    var input = document.getElementById('secondmovie');
    let url = getAPIBaseURL()+'/listload/';
    url+='?title='+input.value

    fetch(url,{method:'get'})
    .then((response) => response.json())
    .then(function(movies){
        let listBody='';
        for(i=0; i<movies.length; i++){
            movie=movies[i];
            listBody+='<option value=\''+movie['id']+'\'>'+movie['title']+' ('+movie['release_date']+')</option>';
        }
        list.innerHTML=listBody
    })
}

function initialize(){
    var button = document.getElementById('submission');
    button.onclick = onButtonPress;

    //Each time a key is released in either input, the corresponding datalist is updated
    var input1 = document.getElementById('firstmovie');
    var input2 = document.getElementById('secondmovie');
    input1.onkeyup = updateFirstList;
    input2.onkeyup = updateSecondList;
}

window.onload=initialize;