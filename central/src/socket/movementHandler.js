const request = require('request')

const ROTATE_STEP = 0.1;

module.exports = function(socket){
  socket.on('move', function(orientation){
    console.log(orientation)
    request.post('http://localhost:8001/move', { form : { orientation : i}}, function(req, res){
      socket.emit('moveStatus', res.statusCode)
    })
  })

  /**
   * Rotate camera. Direction is either 1 or -1. 1 is clockwise and so on.
   */
  socket.on("rotatecam", function(dir) {
    console.log(`Rotate ${dir}`);

    request.post('http://localhost:8001/rotate', { form : { rotate : dir*ROTATE_STEP}}, function(req, res){
      socket.emit('rotateStatus', res.statusCode);
    })

  });
}