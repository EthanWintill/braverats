var rules = document.getElementById("rules");
      rules.addEventListener("click", function() {
        window.location.href = "rules";
      });


var play = document.getElementById("play");
      play.addEventListener("click", function() {
        play.classList.toggle("clicked");
      });

      
      $(document).ready(function() {
        var link = $("#game_link").text();
        $("#game_link").text( window.location.origin + link);
        $("#game_link").attr('hidden',false)
        $("#game_link").attr('href', window.location.origin + link)
        $("#gameLinkModal").modal("show");

        $("#copy_link_btn").on("click", function() {
          var link = $("#game_link").attr('href');
      
          if (navigator.clipboard) {
            navigator.clipboard.writeText(link).then(function() {
              console.log("Link copied to clipboard!");
              $("#copy_link_btn").hide();
              $("#copynotif").attr("hidden",false)        
            }, function() {
              console.log("Failed to copy link to clipboard!");
            });
          } else {
            // fallback code for older browsers
            var copyTextArea = document.createElement("textarea");
            copyTextArea.value = link;
            document.body.appendChild(copyTextArea);
            copyTextArea.select();
            document.execCommand("copy");
            document.body.removeChild(copyTextArea);
          }
        
        });

      });
      
      
    
      
      