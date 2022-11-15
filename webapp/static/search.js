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
    const criteria = ["title","director","keyword","collection","cast","crew","productioncompany","genre","languagedroplist","country","releasedate"];
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
    var rating_box = document.querySelector('#rating-box');
    url+='ratingbox=';
    if(rating_box.checked){
        url+=rating_box.value;
        var rating = document.getElementById('rating');
        url+='&rating='+rating.value;
    }
    var released = document.querySelector('#released');
    //results.innerHTML+='<li>Released: '+released.checked+"</li>";
    url+='&released='
    if(released.checked){
        url+=released.value;
    }
    url+='&adult='
    var adult = document.querySelector("#adult");
    if(adult.checked){
        url+=adult.value;
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
            //let url = 'http://127.0.0.1/api/overviewresults?search_text='+movie['id']+'&randomizer=False&selector=';
            listBody += '<li><a href='+movie['imdb_link']+'/ target="_blank">'+movie['title']+'....ID: '+movie['id']+', release year: '+movie['release_date']+'</a></li>';
            //listBody += '<li><a href="'+url+'" target="_blank">ID: '+movie['id']+', title: '+movie['title']+', release date: '+movie['release_date']+'</a></li>';
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

    var list = document.getElementById('droplist');
        let url = getAPIBaseURL()+'/searchlanguageload/';

        fetch(url,{method:'get'})
        .then((response) => response.json())
        .then(function(languages){
            let listBody='';
            for(i=0; i<languages.length; i++){
                language=languages[i];
                //listBody+='<option value=\''+movie['title']+' ('+movie['release_date']+') [id:'+movie['id']+']\'>';
                listBody+='<option value=\''+language['id']+'\'>'+language['name']+'</option>';
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