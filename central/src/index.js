// This file should launch on start up
// Immediately connects to MARC0 backend server, listens to event such as first time setup and video requests
const http = require('http');
const request = require('request')
const cors = require('cors');
const express = require('express');
const io = require('socket.io-client');
const config = require('./config/config.js')
const registerConnectionHandler = require('./socket/connectionHandler')
const registerStreamHandler = require('./socket/streamHandler')
const registerListenHandler = require('./socket/listenHandler')
const registerMovementHandler = require('./socket/movementHandler')


const app = express();
const server = http.createServer(app);
const socket = io.connect(config.serverEndpoint);
const listener = require('./controllers/listener')(socket)

// let sendPictures = true;

app.use(cors())
app.use('/', listener)

socket.on('connect', function(){
  registerConnectionHandler(socket)
  registerStreamHandler(socket) 
  registerListenHandler(socket) 
  registerMovementHandler(socket) 
})

// Initiate routine that will send pictures constantly
// (function startStreaming() {
//   if (sendPictures) {
//     setTimeout(() => {
//       fetch("http://localhost:8001/image").then((data) => data.text()).then((img) => {
//         socket.emit("image", {
//           img,
//           marciUUID: config.marciUUID,
//         });
//         startStreaming();
//       })
//     }, 100);
//   }
// })();

server.listen(8000)