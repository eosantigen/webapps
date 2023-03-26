var express = require('express');
var router = express.Router();

const mongodb = require('../db/mongo')


/* GET home page. */
router.get('/', mongodb, function(req, res, next) {
  res.render('index', { title: 'Express' });
});

module.exports = router;
