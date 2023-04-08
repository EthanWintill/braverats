var rules = document.getElementById("rules");
      rules.addEventListener("click", function() {
        window.location.href = "rules";
      });
var play = document.getElementById("play");
      play.addEventListener("click", function() {
        play.classList.toggle("clicked");
      });