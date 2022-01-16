const config = require('../config/config')
module.exports = function(socket) {
  socket.on('streamRequest', function(token){
    const marciUUID = config.marciUUID
    // Do logic here where marci sends in their uuid, and also token to jason's stream server (on the /on_publish endpoint i think)
    // Pings server back on what happened to stream attempt both failed and not, this will be determine the http response. 

    // Do ffmpeg shenanigans (bash) here 
    
    console.log('stream request happened')
    let statusCode = 200;

    // This stream status echoes back to resolve frontend request
    socket.emit('streamStatus', statusCode)
  })
}