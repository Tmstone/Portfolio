$(document).ready(function () {
  $.get("/nav", function (nav) {
    $("#nav").html(nav);
  });

  $.get("/footer", function (footer) {
    $("#footer").html(footer);
  });
  /*
  On click for function button goes here
  id is work
  
  $(".work[href=/projects]").click(function () {
    console.log("button clicked");
    window.open(this.href);
    return false;
  });
   */
  $(function () {
    $("#work").click(function (event) {
      $.get("/projects", function (data) {
        console.log("button clicked");
        //this opens a new window with no data
        //window.open(this.href);
        //when button is clicked, the navigation disappears
        //$("#nav").html(nav);
      });
      return false;
    });
  });
});
