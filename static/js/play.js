
// basic game loop:

// client recieves game state from socket.on("gstate"),
// client updates view for user,
// user chooses a card,
// client sends choice to server with socket.emit("chooseCard")
// server calculates game state,
// server sends game state,
// repeat...

//CONSTANTS

const OPP_CLASS = ".row.opponent"
const PLYR_CLASS = ".row.player"

const NEW_OPP_CLASS = "row opponent"
const NEW_PLYR_CLASS = "row player"

const NEW_ROUND_CLASS = "col-sm round"

function faceDownCard() {
  el = document.createElement("div")
  el.className = "card"

  el2 = document.createElement("div")
  el2.className = "face-down"

  el.appendChild(el2)

  return el

}

function generateCard(cardkey) { // example: A-3 (applewood 3)
  el = document.createElement("div")
  el.className = "card card-" + cardkey

  el2 = document.createElement("div")
  el2.className = "face-up"

  el.appendChild(el2)
  return el
}

function renderKnownHand(userCls, handArr, team) {
  userHand = $(userCls)
  for (i in handArr){
    key = team + "-" + handArr[i]
    userHand.append(generateCard(key))
  }
}

function renderUnknownHand(userCls, handSize){
  userHand = $(userCls)
  counter = 0
  while (counter < handSize){
    userHand.append(faceDownCard())
    counter += 1
  }
}








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
        //$("#gameState").text(data.debugstate)
        
        console.log(data)
        // from this data i need to generate the board...
        // it is 3 AM god please help me

        //first render the team:
        //change classes for team colors, if spectator put apple on bottom
        //render hands, player face up
        //render history
        //render player card, or opp card, depending who played first
        // gucci

        var playerTeamName = data.state.team == -1 ? "yarg" : "applewood"
        var oppTeamName = playerTeamName == "yarg" ? "applewood" : "yarg"
        $(PLYR_CLASS).attr("class",NEW_PLYR_CLASS + " " + playerTeamName)
        $(OPP_CLASS).attr("class",NEW_OPP_CLASS + " " + oppTeamName)
        //done setting team colors

        if (playerTeamName == "applewood"){
          renderKnownHand(PLYR_CLASS, data.state.applewood_hand, "A")
          renderUnknownHand(OPP_CLASS, data.state.yarg_hand.length)
        } else {
          renderKnownHand(PLYR_CLASS, data.state.yarg_hand, "Y")
          renderUnknownHand(OPP_CLASS, data.state.applewood_hand.length)
        }
    
        


        /*$("#team").text(data.state.team)
        $("#applewood_card").text(data.state.applewood_card)
        $("#applewood_hand").text(data.state.applewood_hand)
        $("#yarg_card").text(data.state.yarg_card)
        $("#yarg_hand").text(data.state.yarg_hand)
        $("#yarg_score").text(data.state.yarg_score)
        $("#applewood_score").text(data.state.applewood_score)
        $("#gameover").text(data.state.gameover)
        $("#game_over").text(data.state.game_winner)
        $("#round_winner").text(data.state.round_winner)
        $("#history").text(data.state.history)*/
      });

      /*
      $('#send-button').click(function() {
        const pickedCard = $('#cardToPlay').val()
        data = {
          gid:window.location.pathname.slice(6),
          sid:$('#sid').text(),
          card:pickedCard,
        }
        
        socket.emit('chooseCard', data)
    });*/

    socket.on('gameover', function () {
      window.location.href = 'gameover'
    });

    });


    