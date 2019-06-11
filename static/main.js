$(document).ready(function () {
     $.get('/nav', function(nav){
        $('#nav').html(nav)
     });
})
