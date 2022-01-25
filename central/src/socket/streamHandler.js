const config = require('../config/config')
const { spawn } = require('child_process')
module.exports = function(socket) {
  const initializeStreamInput = (socket, streamScript) => {
    socket.once('streamInput', (input) => {
      streamScript.stdin.write(input)
      streamScript.stdin.end()
    })
  }
  socket.on('streamRequest', function(uniqueString, uid){
    const marciUUID = config.marciUUID
    // Do logic here where marci sends in their uuid, and also uniqueString to jason's stream server (on the /on_publish endpoint i think)
    // Pings server back on what happened to stream attempt both failed and not, this will be determine the http response. 
    
    let statusCode = 200;
    // Do ffmpeg shenanigans (bash) here, send in uniqueString sama marciUUID separated by '?'
    const credential = `${uniqueString}?${marciUUID}?${uid}`
    const streamScript = spawn(`startStream.sh`, [credential])
  
    streamScript.stderr.on('data', (data) => {
      socket.emit('streamStatus', 401)
    })
    streamScript.stdout.on('data', (data) => {
      const output = data.toString()
      
      if(/(Press \[q\] to stop)/gm.test(output)){
        socket.emit('streamStatus', 200)
        initializeStreamInput(socket, streamScript)
      }
    })

    // https://github.com/bentlyedyson/HEARTY-HEARTY/blob/main/backendweb/src/index.js#L54
    console.log('Stream request happened')

    // This stream status echoes back to resolve frontend request
    socket.emit('streamStatus', statusCode)
  })
}