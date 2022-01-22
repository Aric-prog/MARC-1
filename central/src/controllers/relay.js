const express = require('express')
const router = express.Router()

module.exports = function(socket){
  router.post('/relay', function(){
    socket.emit('listenStatus', 200)
  })
  return router;
}