/*
    overview.js
    Aaron Bronstone/Jack Owens
    For CS257 Software Design, Carleton College Fall 2022
 */
    function onButtonPress() {
        
    }

    function auto(){
        var title = document.getElementById("title");
        var input = document.getElementById("search");
        title.innerHTML=input.value;
    }

    function random_filters(){
        var filter = document.getElementById("filter");
        var randomizer = document.getElementById("random_checkbox");
        if(randomizer.checked==true){
            filter.innerHTML='<label for="object">Get me a random movie with...</label><br><select id="selector"><option>Genre</option><option>Director</option></select><input type="text" id="random_input">';
            var random_input = document.getElementById("random_input");
            var inputType = "";
            if(random_input.value=="Director"){
                inputType="date";
            }
            random_input.setAttribute("type",inputType);
        }else{
            filter.innerHTML='<label for="search">Movie Title:</label><input name="" type="text" id="search"><button id="submission">Submit</button>';
        }
    }
    
    function initialize() {
        var button = document.getElementById('submission');
        button.onclick = onButtonPress;
        var random = document.getElementById('random_checkbox');
        random.onclick=random_filters;
        var search = document.getElementById('search');
        search.onkeyup= auto;
    }
    
    // This causes initialization to wait until after the HTML page and its
    // resources are all ready to go, which is often what you want. This
    // "window.onload" approach is a bit old-fashioned. See
    // https://www.dyn-web.com/tutorials/init.php for an interesting and
    // brief discussion of problems with this old-fashioned approach that
    // can become relevant with more complex web pages than the ones
    // we are writing.
    window.onload = initialize;