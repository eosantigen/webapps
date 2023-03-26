const mongodb = require('mongoose');
const mongooseURI = 'mongodb://localhost/tarot_app'
const mongooseOptions = {
  serverSelectionTimeoutMS: 3000,
  heartbeatFrequencyMS: 3000,
  family: 4,
}

// If your app uses only one database, you should use mongoose.connect.

async function mongoDBConnection() {

  try {
    await mongodb.connect(mongooseURI, mongooseOptions)

    mongodb.connection.on('error', err => {
      console.log(err)
    })
  } catch (error) {
    console.log(error);
  }
}

module.exports = mongoDBConnection