
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
        $("#gameState").text(data.state)
        $("#team").text(data.team)
        $("applewood_card").text(data.state.applewood_card)
        $("#applewood_hand").text(data.state.applewood_hand)
        $("#yarg_card").text(data.state.yarg_card)
        $("#yarg_hand").text(data.state.yarg_hand)
        $("#yarg_score").text(data.state.yarg_score)
        $("#applewood_score").text(data.state.applewood_score)
        $("#gameover").text(data.state.gameover)
        $("#game_over").text(data.state.game_winner)
        $("#round_winner").text(data.state.round_winner)
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
        
    });
