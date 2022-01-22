const request = require('request')

module.exports = function(socket){
  socket.on('listen', function(){
    request.get('http://localhost:8002/listen', function(req, res){
      socket.emit('listenStatus', res.statusCode)
    })
  })
}