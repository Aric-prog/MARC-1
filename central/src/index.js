// This file should launch on start up
// Immediately connects to MARC0 backend server, listens to event such as first time setup and video requests
const http = require('http');
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

server.listen(3000)