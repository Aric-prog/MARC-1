// This file should launch on start up
// Immediately connects to MARC0 backend server, listens to event such as first time setup and video requests
const http = require('http');
const request = require()
const cors = require('cors');
const express = require('express');
const io = require('socket.io-client');
const config = require('./config/config.js')
const registerConnectionHandler = require('./socket/connectionHandler')
const registerStreamHandler = require('./socket/streamHandler')

const app = express();
app.use(cors())
const server = http.createServer(app);
const socket = io.connect(config.serverEndpoint);

socket.on('connect', function(){
  registerConnectionHandler(socket)
  registerStreamHandler(socket) 
})

for (const i of ['left', 'right', 'forward', 'back']){
  socket.on('move' + i, function(){
    request('http://localhost:8001/move' + i, function(req, res){
      
    })
  })
}


server.listen(8000)