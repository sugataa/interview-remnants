// check version
const version = process.versions.node;
const [majorStr, minorStr, __] = version.split('.');
const major = parseInt(majorStr);
const minor = parseInt(minorStr);

if (major <= 5 || (major === 6 && minor < 5)) {
  throw new Error('Must be using Node 6.5 or greater.');
}

// make sure we can require express
const express = require('express')
const app = express()
app.listen(3265);

// try the postgres connection
const { Pool } = require('pg')
const pool = new Pool({
  database: 'memory_tracker',
  user: 'candidate',
  password: 'giap-quib-fac-wav-mi',
  port: 10131,
  host: 'aws-us-east-1-portal.8.dblayer.com',
});
pool.query('SELECT count(*) FROM reports', (err, pgRes) => {
  if (err) {
    throw new Error(err);
  }

  if (pgRes.rows[0].count !== '20000') {
    throw new Error('Could not connect to Postgres server. Please check your internet connection or the node-postgres library.');
  }

  console.log('Everything working!');
  process.exit();
});
