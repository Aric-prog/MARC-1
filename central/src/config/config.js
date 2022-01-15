const dotenv = require('dotenv')
const path = require('path')

dotenv.config({path : path.join(__dirname, '../.env')})

module.exports = {
  serverEndpoint : process.env.SERVER_ENDPOINT,
  marciUUID : process.env.MARCI_UUID
};