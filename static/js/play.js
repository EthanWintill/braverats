
// basic game loop:

// client recieves game state from socket.on("gstate"),
// client updates view for user,
// user chooses a card,
// client sends choice to server with socket.emit("chooseCard")
// server calculates game state,
// server sends game state,
// repeat...

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

      /*socket.on('result', function(data) {
                $('#player1_card').text(data.player1_card);
                $('#player2_card').text(data.player2_card);
                $('#result').text(data.winner);
            });

      socket.on('played', function(data) {
          pickedCard = data["cardValue"]
          playedCards = $('#player2played_cards').text()
          playedCards += " " + pickedCard
          $('#player2played_cards').text(playedCards)

          currentHand = $('#player2_card').text()
          $('#player2_card').text(currentHand.replace(pickedCard + " ", ""))

          $('#winners').text(data['result'])
        })


      $('#send-button').click(function() {
                pickedCard = $('#cardToPlay').val()
                playedCards = $('#player1played_cards').text()
                playedCards += " " + pickedCard
                $('#player1played_cards').text(playedCards)
                let gid = window.location.pathname.slice(6)
                let sid = $('#sid').text()
                socket.emit('playedCard', { gid: gid, sid: sid, card: pickedCard});
		            $('#cardToPlay').val('');

                currentHand = $('#player1_card').text()
                $('#player1_card').text(currentHand.replace(pickedCard + " ", ""))

            });
       */ 
    });
