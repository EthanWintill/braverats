
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

const MIDDLE_CLASS = '.row.middle'

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
  el2.className = "face-up hand"

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

function clearHandsAndHistory() {
  $(PLYR_CLASS).empty()
  $(OPP_CLASS).empty()
  $(MIDDLE_CLASS).empty()
}

function generateRound(round, team){
  console.log(round)
  const winner = round.winner
  const aCard = round.aCard
  const yCard = round.yCard
  var roundClass = NEW_ROUND_CLASS
  if (winner > 0){
    roundClass += " a-win"
  } else if (winner < 0){
    roundClass += " y-win"
  } else{
    roundClass += " hold-win"
  }
  var roundEl = document.createElement("div")
  roundEl.className = roundClass

  var topEl = document.createElement("div")
  var bottomEl = document.createElement("div")

  var face = document.createElement("div")
    face.className = "face-up"
    var face2 = document.createElement("div")
    face2.className = "face-up"

  if (team == -1) {
    
    bottomEl.className = "row card card-Y-" + yCard
    bottomEl.appendChild(face)

    topEl.className = "row card card-A-" + aCard
    topEl.appendChild(face2)
  } else{
    bottomEl.className = "row card card-A-" + aCard
    bottomEl.appendChild(face)

    topEl.className = "row card card-Y-" + yCard
    topEl.appendChild(face2)
  }

  roundEl.appendChild(topEl)
  roundEl.appendChild(bottomEl)

  return roundEl

}

function generateFriendlyCardPreview(card, team) {
  var roundEl = document.createElement("div")
  roundEl.className = NEW_ROUND_CLASS
  var topEl = document.createElement("div")
  var bottomEl = document.createElement("div")
  topEl.className = "row card"
  bottomEl.className = "row card"
  var face = document.createElement("div")
  face.className = "face-up"

  if (team == -1) {
    
    bottomEl.className = "row card card-Y-" + card
    bottomEl.appendChild(face)

  } else{
    bottomEl.className = "row card card-A-" + card
    bottomEl.appendChild(face)


  }
  roundEl.appendChild(topEl)
  roundEl.appendChild(bottomEl)
  return roundEl
}

function generateEnemyCardPreview() {
  var roundEl = document.createElement("div")
  roundEl.className = NEW_ROUND_CLASS
  var topEl = document.createElement("div")
  var bottomEl = document.createElement("div")
  topEl.className = "row card"
  bottomEl.className = "row card"
  var face = document.createElement("div")
  face.className = "face-down"

  topEl.appendChild(face)
  roundEl.appendChild(topEl)
  roundEl.appendChild(bottomEl)
  return roundEl
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

        clearHandsAndHistory()

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
        
        const prevRounds = data.state.history
        const middleEl = $(MIDDLE_CLASS)

        for (i in prevRounds){
          var thisRound = prevRounds[i]
          console.log(thisRound)
          var roundEl = generateRound(JSON.parse(thisRound), data.state.team)
          middleEl.append(roundEl)
        }
        
        const aCard = data.state.applewood_card
        const yCard = data.state.yarg_card
        console.log(data)
        if (aCard != null){
          if (data.state.team == 1){
          var previewEl = generateFriendlyCardPreview(aCard, data.state.team)
          middleEl.append(previewEl)
          } else {
            var previewEl = generateEnemyCardPreview()
          middleEl.append(previewEl)
          }
        } else if (yCard != null){
          
          if (data.state.team == -1){
          var previewEl = generateFriendlyCardPreview(yCard, data.state.team)
          middleEl.append(previewEl)
          } else{
            var previewEl = generateEnemyCardPreview()
          middleEl.append(previewEl)
          }
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

   
      $(PLYR_CLASS).on('click', '.face-up.hand', function() {
        console.log("picker")
      const pickedCard = $(this).parent().attr('class').split(' ')[1].split('-')[2]
      data = {
        gid:window.location.pathname.slice(6),
        sid:$('#sid').text(),
        card:pickedCard,
      }

      socket.emit('chooseCard', data)
      })
      
    

    socket.on('gameover', function () {
      window.location.href = 'gameover'
    });

    });


    