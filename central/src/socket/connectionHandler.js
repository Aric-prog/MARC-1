const config = require('../config/config')
module.exports = function(socket) {
  // Do post requests here to either server or firebase itself
  socket.emit('marciActivate', config.marciUUID)
  socket.on('marciDetected', function(){
    console.log('Marci is now detected by server')
  })
}