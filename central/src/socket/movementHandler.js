const request = require('request')

module.exports = function(socket){
  socket.on('move', function(orientation){
    console.log(orientation)
    request.post('http://localhost:8001/move', { form : { orientation : i}}, function(req, res){
      socket.emit('moveStatus', res.statusCode)
    })
  })
}