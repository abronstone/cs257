/*
    overview.js
    Aaron Bronstone/Jack Owens
    For CS257 Software Design, Carleton College Fall 2022
 */

function getAPIBaseURL(){
    let baseURL=window.location.protocol+'//'+window.location.hostname+':'+window.location.port+'/api';
    return baseURL;
}

function onButtonPress() {
    let url = getAPIBaseURL()+'/overviewresults/';
    var randomizer = document.getElementById("random_checkbox");
    url+='?';
    if(randomizer){
        var selector = document.getElementById("selector");
        var search_text = document.getElementById("search_text");
        url+='search_text='+search_text.value+'&';
        url+='randomizer=True&';
        url+='selector=';//+selector.selectedOptions[0].value;
    }else{
        var search_text = document.getElementById("search_text");
        url+='search_text='+search_text.value+'&';
        url+='randomizer=False&';
        url+='selector=';
    }

    title = document.getElementById('title');
    overview = document.getElementById('overview');
    table = document.getElementById('table');
    popularity = document.getElementById('popularity');
    tagline = document.getElementById('tagline');
    rating = document.getElementById('rating');

    const tableList = ["collection","director","genre","releasedate"];

    fetch(url,{method:'get'})
    .then((response) => response.json())
    .then(function(movies){
        let listBody = '';
        movie=movies[0];
        /*for(let i=0; i<movies.length; i++){
            let movie = movies[i];
            title.innerHTML=movie['title'];
        }
        */
        title.innerHTML=movie['title'];
        if(movie['tagline']!=''){
            tagline.innerHTML='<h4><center>'+movie['tagline']+'</center></h4>';
        }

       overview.innerHTML='<p>'+movie['overview']+'</p>';
       popularity.innerHTML=movie['popularity'];
       rating.innerHTML=parseFloat(movie['rating']);

        //results.innerHTML=listBody;
    })
    .catch(function(error) {
        console.log(error);
    });
}
/*
function random_filters(){
    var filter = document.getElementById("filter");
    var randomizer = document.getElementById("random_checkbox");
    if(randomizer.checked==true){
        filter.innerHTML= '<label for="object">Get me a random movie with...</label><br><select id="selector"><option></option><option>language</option></selector><input type="text" id="random_input"><button id="submission">Submit</button> ';
        //<option>director</option></select><input type="text" id="random_input">';
        var random_input = document.getElementById("random_input");
        var inputType = "";
        if(random_input.value=="Director"){
            inputType="date";
        }
        random_input.setAttribute("type",inputType);
    }else{
        filter.innerHTML='<label for="search">Movie Title:</label><input name="" type="text" id="search_text"><button id="submission">Submit</button>';
    }
}
*/

function loadlist(){
    var list = document.getElementById('droplist');
    let url = getAPIBaseURL()+'/overviewlistload/';

    fetch(url,{method:'get'})
    .then((response) => response.json())
    .then(function(movies){
        let listBody='';
        for(i=0; i<movies.length; i++){
            movie=movies[i];
            listBody+='<option value=\''+movie['title']+'\'>';
        }
        list.innerHTML=listBody
    })

}

function initialize() {
    var button = document.getElementById('submission');
    button.onclick = onButtonPress;
    
    
    var list = document.getElementById('droplist');
    let url = getAPIBaseURL()+'/overviewlistload/';

    fetch(url,{method:'get'})
    .then((response) => response.json())
    .then(function(movies){
        let listBody='';
        for(i=0; i<movies.length; i++){
            movie=movies[i];
            listBody+='<option value=\''+movie['title']+'\'>';
        }
        list.innerHTML=listBody
    })
    //var list = document.getElementById('droplist');
    //list.addEventListener('click',loadlist);
    //list.onclick = loadlist;
    //var random = document.getElementById('random_checkbox');
    //random.onclick=random_filters;
    //var search = document.getElementById('search_text');
    //search.onkeyup= droplist;
}

// This causes initialization to wait until after the HTML page and its
// resources are all ready to go, which is often what you want. This
// "window.onload" approach is a bit old-fashioned. See
// https://www.dyn-web.com/tutorials/init.php for an interesting and
// brief discussion of problems with this old-fashioned approach that
// can become relevant with more complex web pages than the ones
// we are writing.
window.onload = initialize;