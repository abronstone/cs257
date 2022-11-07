/*
    search.js
    Aaron Bronstone and Jack Owens
    For CS257 Software Design, Carleton College
 */
    function onButtonPress() {
        const criteria = ["title","director","keyword","collection","cast","crew","productioncompany","genre","language","rating","country","releasedate"];
        var results = document.getElementById("result-list");
        //var first = document.getElementById(criteria[0]);
        //results.innerHTML=criteria[1];
        results.innerHTML='';
        for(let i=0; i<criteria.length; i++){
            var current = document.getElementById(criteria[i]);
            var name = current.getAttribute("name");
            if(current.value!=""){
                results.innerHTML+='<li>'+name+": "+current.value+'</li>\n';
            }
        }
        var released = document.querySelector('#released');
        results.innerHTML+='<li>Released: '+released.checked+"</li>";
        var adult = document.querySelector("#adult");
        results.innerHTML+='<li>Adult: '+adult.checked+"</li>";
        
    }
    
    function initialize() {
        var button = document.getElementById('submission');
        button.onclick = onButtonPress;
    }
    
    // This causes initialization to wait until after the HTML page and its
    // resources are all ready to go, which is often what you want. This
    // "window.onload" approach is a bit old-fashioned. See
    // https://www.dyn-web.com/tutorials/init.php for an interesting and
    // brief discussion of problems with this old-fashioned approach that
    // can become relevant with more complex web pages than the ones
    // we are writing.
    window.onload = initialize;