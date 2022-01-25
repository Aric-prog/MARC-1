const express = require('express')
const router = express.Router()

module.exports = function(socket){
  router.post('/listenStatus', function(req,res){
    socket.emit('listenStatus', 200)
    return res.sendStatus(201)
  })
  return router;
}