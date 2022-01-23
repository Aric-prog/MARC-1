const request = require('request')

module.exports = function(socket){
  socket.on('listen', function(){
    request.get('http://localhost:8002/listen', function(req, res){
      socket.emit('listenStatus', res.statusCode)

      // Check if event = marciNote, send the content to marc0 endpoint
      if(false){

      }
    })
  })
}