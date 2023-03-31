var rules = document.getElementById("rules");
      rules.addEventListener("click", function() {
        window.location.href = "rules.html";
      });
var play = document.getElementById("play");
      play.addEventListener("click", function() {
        play.classList.toggle("clicked");
      });
var playWithAFriend = document.getElementById("playWithAFriend");
      playWithAFriend.addEventListener("click", function() {
        playWithAFriend.classList.toggle("clicked");
      });