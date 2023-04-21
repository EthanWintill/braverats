var rules = document.getElementById("rules");
      rules.addEventListener("click", function() {
        window.location.href = "rules";
      });


var account = document.getElementById("account");
      account.addEventListener("click", function() {
        window.location.href = "account";
      });
var play = document.getElementById("play");
      play.addEventListener("click", function() {
        play.classList.toggle("clicked");
      });

$(document).ready(function () {
  var link = $("#game_link").attr("value")
  $("#game_link").attr("value", window.location.origin + link)
})