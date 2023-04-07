
// basic game loop:

// client recieves game state from socket.on("gstate"),
// client updates view for user,
// user chooses a card,
// client sends choice to server with socket.emit("chooseCard")
// server calculates game state,
// server sends game state,
// repeat...

//CONSTANTS

const OPP_CLASS = "row opponent"
const PLYR_CLASS = "row player"

const ROUND_CLASS = "col-sm round"



function generateCard(cardkey) { // example: A-3 (applewood 3)

}


/*
    $(document).ready(function () {
      console.log(io.version)
      var socket = io.connect('http://127.0.0.1:3000');

      socket.on('connect', function () {
        let gid = window.location.pathname.slice(6)
        let sid = $('#sid').text()

        socket.emit('connection', { gid: gid, sid: sid});
        console.log("connected")
      });
    
      socket.on("gstate", (data) => {
        // TODO: update client view based on recieved state instead of just printing it
        $("#gameState").text(data.debugstate)
        
        console.log(data)
        $("#team").text(data.state.team)
        $("#applewood_card").text(data.state.applewood_card)
        $("#applewood_hand").text(data.state.applewood_hand)
        $("#yarg_card").text(data.state.yarg_card)
        $("#yarg_hand").text(data.state.yarg_hand)
        $("#yarg_score").text(data.state.yarg_score)
        $("#applewood_score").text(data.state.applewood_score)
        $("#gameover").text(data.state.gameover)
        $("#game_over").text(data.state.game_winner)
        $("#round_winner").text(data.state.round_winner)
        $("#history").text(data.state.history)
      });

      $('#send-button').click(function() {
        const pickedCard = $('#cardToPlay').val()
        data = {
          gid:window.location.pathname.slice(6),
          sid:$('#sid').text(),
          card:pickedCard,
        }
        
        socket.emit('chooseCard', data)
    });

    socket.on('gameover', function () {
      window.location.href = 'gameover'
    });

    });
*/

    