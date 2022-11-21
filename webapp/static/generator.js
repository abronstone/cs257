/* 
    generator.js
    Aaron Bronstone/Jack Owens
    For CS257 Software Design, Carleton College Fall 2022
*/

function getAPIBaseURL(){
    let baseURL=window.location.protocol+'//'+window.location.hostname+':'+window.location.port+'/api';
    return baseURL;
}

function onButtonPress(){
    


    let url = getAPIBaseURL()+'/generatorresults/';

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

        description = document.getElementById('description');
        description.innerHTML = '<p>'+movie['overview']+'</p>';

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

function initialize(){
    var button = document.getElementById('submission');
    button.onclick = onButtonPress;
}

window.onload=initialize;