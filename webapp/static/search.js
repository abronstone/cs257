/*
    search.js
    Aaron Bronstone and Jack Owens
    For CS257 Software Design, Carleton College
 */

window.onload = initialize;

function getAPIBaseURL(){
    let baseURL=window.location.protocol+'//'+window.location.hostname+':'+window.location.port+'/api';
    return baseURL;
}


function onSubmitPress() {
    /*
        Submits the following URL to the API:
            getAPIBaseURL()+'/searchresults/?title=&director=&keyword=&collection=&cast=&crew=&productioncompany=&genre=&languagedroplist=&country=&release-date-before=&release-date-after=&ratingbox=&released=&adult='

        Updates the 'results' HTML element with a list of IMDB links, with text changed to the movie title and release year, all of which returned by the API.
    */
    const criteria = ["title","director","keyword","collection","cast","crew","productioncompany","genre","languagedroplist","country","release-date-before","release-date-after"];
    var results = document.getElementById("result-list");
    let url = getAPIBaseURL() + '/searchresults/';
    results.innerHTML='';
    url+='?';
    for(let i=0; i<criteria.length; i++){
        var currentCriteria = document.getElementById(criteria[i]);
        
        url+=criteria[i]+'=';
        if(currentCriteria){
            url+=currentCriteria.value;
        }
        url+='&';
    }
    var rating_box = document.querySelector('#rating-box');
    url+='ratingbox=';
    if(rating_box.checked){
        url+=rating_box.value;
        var rating = document.getElementById('rating');
        url+='&rating='+rating.value;
    }
    var released = document.querySelector('#released');
    url+='&released='
    if(released.checked){
        url+=released.value;
    }
    url+='&adult='
    var adult = document.querySelector("#adult");
    if(adult.checked){
        url+=adult.value;
    }
   results.innerHTML='Loading...';

    fetch(url,{method:'get'})
    .then((response) => response.json())
    .then(function(movies){
        let listBody = '';
        results.innerHTML+='test';
        for(let i=0; i<movies.length; i++){
            let movie = movies[i];
            listBody += '<li><a href='+movie['imdb_link']+'/ target="_blank">'+movie['title']+' ('+movie['release_date']+')</a></li>';
        }
        results.innerHTML=listBody;
    })
    .catch(function(error) {
        console.log(error);
    });
}

function initialize() {
    var button = document.getElementById('submission');
    button.onclick = onSubmitPress;

    /*
        The languages provided in the original dataset are only two letters long. Therefore, we thought it would be best to have a droplist of every language
        so the user does not type the full language name 
    */
    var list = document.getElementById('droplist');
        let url = getAPIBaseURL()+'/searchlanguageload/';

        fetch(url,{method:'get'})
        .then((response) => response.json())
        .then(function(languages){
            let listBody='';
            for(i=0; i<languages.length; i++){
                language=languages[i];
                listBody+='<option value=\''+language['name']+'\'>'+language['name']+'</option>';
            }
            list.innerHTML=listBody
        })
}

// This causes initialization to wait until after the HTML page and its
// resources are all ready to go, which is often what you want. This
// "window.onload" approach is a bit old-fashioned. See
// https://www.dyn-web.com/tutorials/init.php for an interesting and
// brief discussion of problems with this old-fashioned approach that
// can become relevant with more complex web pages than the ones
// we are writing.
window.onload = initialize;