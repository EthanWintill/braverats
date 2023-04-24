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

      
      $(document).ready(function() {
        var link = $("#game_link").attr("value");
        $("#game_link").attr("value", window.location.origin + link);
      
        $("#copy_link_btn").on("click", function() {
          var link = $("#game_link").val();
      
          if (navigator.clipboard) {
            navigator.clipboard.writeText(link).then(function() {
              alert("Link copied to clipboard!");
            }, function() {
              alert("Failed to copy link to clipboard!");
            });
          } else {
            // fallback code for older browsers
            var copyTextArea = document.createElement("textarea");
            copyTextArea.value = link;
            document.body.appendChild(copyTextArea);
            copyTextArea.select();
            document.execCommand("copy");
            document.body.removeChild(copyTextArea);
      
            // Display the link in a pop-up
            var tooltip = document.getElementById("tooltip");
            tooltip.innerHTML = "Click to enter game: <a href='" + link + "' target='_blank'>" + link + "</a>";
            tooltip.style.display = "block";
          }
        });
      });
      
    
      
      