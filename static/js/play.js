
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
                socket.send($('#cardToPlay').val());
		            $('#cardToPlay').val('');

                currentHand = $('#player1_card').text()
                $('#player1_card').text(currentHand.replace(pickedCard + " ", ""))

            });*/
        
    });
