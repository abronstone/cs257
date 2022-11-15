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
        url+='search_text='+encodeURIComponent(search_text.value)+'&';
        url+='randomizer=True&';
        url+='selector=';//+selector.selectedOptions[0].value;
    }else{
        var search_text = document.getElementById("search_text");
        url+='search_text='+encodeURIComponent(search_text.value)+'&';
        url+='randomizer=False&';
        url+='selector=';
    }
    

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
        title = document.getElementById('title');
        title.innerHTML=movie['title'];
        //console.log(movie['tagline']);
        tagline = document.getElementById('tagline');
        if(movie['tagline']!=null){
            tagline.innerHTML='<h4><center>'+movie['tagline']+'</center></h4>';
        }else{
            tagline.innerHTML='';
        }

        overview = document.getElementById('overview');
        overview.innerHTML = '<p>'+movie['overview']+'</p>';

        director = document.getElementById('director');
        director.innerHTML = movie['director'];

        cast = document.getElementById('cast');
        cast.innerHTML = movie['actors'];

        popularity = document.getElementById('popularity');
        popularity.innerHTML = movie['popularity'];

        production_company = document.getElementById('productioncompany');
        production_company.innerHTML = movie['companies'];

        production_countries = document.getElementById('productioncountries');
        production_countries.innerHTML = movie['countries'];

        crew = document.getElementById('crew');
        crew.innerHTML = movie['crew'];

        keywords = document.getElementById('keywords');
        keywords.innerHTML = movie['keywords'];

        genres = document.getElementById('genres');
        genres.innerHTML = movie['genres'];

        link = document.getElementById('link');
        link.innerHTML = '<a href="'+movie['link']+'" target="_blank">'+movie['link']+'</a>';

        language = document.getElementById('language');
        language.innerHTML = movie['language'];

        release_date = document.getElementById('releasedate');
        release_date.innerHTML = movie['release_date'];

        revenue = document.getElementById('revenue');
        let dollarUSLocale = Intl.NumberFormat('en-US');
        revenue.innerHTML='$'+dollarUSLocale.format(movie['revenue']);

        budget = document.getElementById('budget');
        budget.innerHTML='$'+dollarUSLocale.format(movie['budget']);

        movie_status = document.getElementById('status');
        movie_status.innerHTML=movie['status'];

        rating = document.getElementById('rating');
        rating.innerHTML=parseFloat(movie['rating']);



        //results.innerHTML=listBody;
    })
    .catch(function(error) {
        console.log(error);
    });
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
            //listBody+='<option value=\''+movie['title']+' ('+movie['release_date']+') [id:'+movie['id']+']\'>';
            listBody+='<option value=\''+movie['id']+'\'>'+movie['title']+' ('+movie['release_date']+')</option>';
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