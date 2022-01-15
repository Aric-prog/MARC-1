// This file should launch on start up
// Immediately connects to MARC0 backend server, listens to event such as first time setup and video requests
const http = require('http');
const express = require('express');

const app = express();
const server = http.createServer(app); 