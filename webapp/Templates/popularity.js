/*
    search.js
    Aaron Bronstone and Jack Owens
    For CS257 Software Design, Carleton College
 */
    function onButtonPress() {
        var results = document.getElementById("results");
        results.innerHTML='pooopy';
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