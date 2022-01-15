// This file should launch on start up
// Immediately connects to MARC0 backend server, listens to event such as first time setup and video requests
const http = require('http');
const cors = require('cors');
const express = require('express');
const io = require('socket.io-client');
const config = require('./config/config.js')

const app = express();
const server = http.createServer(app);

app.use(cors())
const socket = io.connect(config.marciUUID);

