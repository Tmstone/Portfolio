$(document).ready(function () {
  $.get("/nav", function (nav) {
    $("#nav").html(nav);
  });
  /*
  $.get("/footer", function (footer) {
    $("#footer").html(footer);
  });*/
  /*
  On click for function button goes here
  id is work
  */
});
