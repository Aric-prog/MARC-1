const request = require('request')
const config = require('../config/config')
module.exports = function(socket){
  socket.on('listen', function(){
    request.get('http://localhost:8002/listen', function(req, res){
      try{
        const event = JSON.parse(res.body)
        if(event.event === 'note'){
          socket.emit('marciNote', config.marciUUID, event.content)
        } else if(event.event === 'move'){  
          request.post('http://localhost:8001/move', {form : { orientation : event.orientation }}, function(req, res){

          })
        }
        socket.emit('listenStatus', res.statusCode)
      } catch(err){
        console.log(err)
      }

      // Check if event = marciNote, send the content to marc0 endpoint
      
    })
  })
}