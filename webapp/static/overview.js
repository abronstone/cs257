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
    /*
        Submits the following URL to the API:
            getAPIBaseURL()+'/overviewresults/?id={movie id}'
        
        Updates each result element with its corresponding value returned by the API JSON object, including:
            -Movie Title (large display)
            -Tagline (displayed under title)
            -Overview (displayed in colored paragraph)
            -Director (table)
            -Collection (table, not available for some)
            -Keywords (table)
            -Genres (table)
            -Popularity (table)
            -Link (table)
            -Language (table)
            -Production Company (table)
            -Production Countries (table)
            -Release Date (table)
            -Revenue (table)
            -Budget (table)
            -Status (table)
            -Rating (table, not available for some)
            -Cast (table)
            -Crew (table)
            
    */
    let url = getAPIBaseURL()+'/overviewresults/';
    url+='?';
    var id = document.getElementById("search_text");
    url+='id='+encodeURIComponent(id.value);

    fetch(url,{method:'get'})
    .then((response) => response.json())
    .then(function(movies){
        movie=movies[0];

        title = document.getElementById('title');
        title.innerHTML=movie['title'];

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

        collection = document.getElementById('collection');
        collection.innerHTML = movie['collection'];

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
    })
    .catch(function(error) {
        console.log(error);
    });
}

function updateList(){
     /*
        Calls to API endpoint '/listload/' to dynamically update the datalist for the input
    */
    var list = document.getElementById('droplist');
    var input = document.getElementById('search_text');
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

function initialize() {
    var button = document.getElementById('submission');
    button.onclick = onButtonPress;

    //Each time a key is released in either input, the corresponding datalist is updated
    var input = document.getElementById('search_text');
    input.onkeyup = updateList;
}

// This causes initialization to wait until after the HTML page and its
// resources are all ready to go, which is often what you want. This
// "window.onload" approach is a bit old-fashioned. See
// https://www.dyn-web.com/tutorials/init.php for an interesting and
// brief discussion of problems with this old-fashioned approach that
// can become relevant with more complex web pages than the ones
// we are writing.
window.onload = initialize;