module.exports = function(socket) {
  socket.on('streamRequest', function(token){
    const marciUUID = config.marciUUID
    // Do logic here where marci sends in their uuid, and also token to jason's stream server
    
    // Pings server back when stream attempt failed, 
    // TODO : figure out how to talk to frontend when stream failed
    let failedToStream = false;
    if(failedToStream){
      socket.emit('streamFailed')
    }
  })
}