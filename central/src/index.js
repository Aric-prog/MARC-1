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

app.use(cors())
app.use('/', listener)

socket.on('connect', function(){
  registerConnectionHandler(socket)
  registerStreamHandler(socket) 
  registerListenHandler(socket) 
  registerMovementHandler(socket) 
})

server.listen(8000)