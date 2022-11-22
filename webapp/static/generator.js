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
    /*
         Submits the following URL to the API:
            getAPIBaseURL()+'/generatorresults/?filterOne=&inputOne=&filterTwo=&inputTwo=&filterThree=&inputThree=&previoustitle='

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
    let url = getAPIBaseURL()+'/generatorresults/';
    let filterOne = document.getElementById('filterone').value;
    let inputOne = document.getElementById('firstinput').value;
    let filterTwo = document.getElementById('filtertwo').value;
    let inputTwo = document.getElementById('secondinput').value;
    let filterThree = document.getElementById('filterthree').value;
    let inputThree = document.getElementById('thirdinput').value;

    previousTitle = document.getElementById('title');

    url+='?';
    url+='filterOne='+filterOne+'&inputOne='+inputOne+'&filterTwo='+filterTwo+'&inputTwo='+inputTwo+'&filterThree='+filterThree+'&inputThree='+inputThree+'&previoustitle='+previousTitle.innerHTML;

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

        description = document.getElementById('description');
        description.innerHTML = '<p>'+movie['overview']+'</p>';

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

function initialize(){
    var button = document.getElementById('submission');
    button.onclick = onButtonPress;
}

window.onload=initialize;