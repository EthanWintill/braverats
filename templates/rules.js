var backButton = document.getElementById("backButton");
      backButton.addEventListener("click", function() {
        window.location.href = "home.html";
      });
function toggleText(id) {
        var x = document.getElementById(id);
        if (x.style.display === "none") {
          x.style.display = "block";
        } else {
          x.style.display = "none";
        }
      }
function toggleImage() {
        var x = document.getElementById("resultsTable");
        if (x.style.display === "none") {
          x.style.display = "block";
        } else {
          x.style.display = "none";
        }
      }