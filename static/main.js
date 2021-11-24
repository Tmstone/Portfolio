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
      $.get("/project", function (data) {
        console.log("button clicked");
        //window.open(this.href);
        $("#nav").html(nav);
      });
      return false;
    });
  });
});
