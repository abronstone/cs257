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
    const criteria = ["title","director","keyword","collection","cast","crew","productioncompany","genre","language","rating","country","releasedate"];
    var results = document.getElementById("result-list");
    let url = getAPIBaseURL() + '/searchresults/';
    //var first = document.getElementById(criteria[0]);
    //results.innerHTML=criteria[1];
    results.innerHTML='';
    url+='?';
    for(let i=0; i<criteria.length; i++){
        var current = document.getElementById(criteria[i]);
        /*var name = current.getAttribute("name");
        if(current.value!=""){
            results.innerHTML+='<li>'+name+": "+current.value+'</li>\n';
        }
        */
        url+=criteria[i]+'=';
        if(current){
            url+=current.value;
        }
        url+='&';
    }
    var released = document.querySelector('#released');
    //results.innerHTML+='<li>Released: '+released.checked+"</li>";
    if(released){
        url+='released='+released.value+'&';
    }
    var adult = document.querySelector("#adult");
    if(adult){
        url+='adult='+adult.value;
    }
    //results.innerHTML+='<li>Adult: '+adult.checked+"</li>";



    /*var title = document.getElementById('title')
    if(title){
        url+='?title='+title.value;
    }
    */
   results.innerHTML='Loading...';

    fetch(url,{method:'get'})
    .then((response) => response.json())
    .then(function(movies){
        let listBody = '';
        results.innerHTML+='test';
        for(let i=0; i<movies.length; i++){
            let movie = movies[i];
            listBody += '<li><a href='+movie['link']+'/ target="_blank">ID: '+movie['id']+', title: '+movie['title']+', release date: '+movie['release_date']+'</a></li>';
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
}

// This causes initialization to wait until after the HTML page and its
// resources are all ready to go, which is often what you want. This
// "window.onload" approach is a bit old-fashioned. See
// https://www.dyn-web.com/tutorials/init.php for an interesting and
// brief discussion of problems with this old-fashioned approach that
// can become relevant with more complex web pages than the ones
// we are writing.
window.onload = initialize;