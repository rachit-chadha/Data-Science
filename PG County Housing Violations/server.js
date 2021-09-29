const express = require('express');
const fetch = require('node-fetch');

const app = express();
const port = process.env.PORT;

app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(express.static('build'));

app.get('/api', (req, res) => {
  const baseURL = 'https://data.princegeorgescountymd.gov/resource/ymzn-mdrc.json';
  fetch(baseURL)
    .then((r) => r.json())
    .then( res => {
      for (let i = 0; i < res.length; i += 1){
        res[i]["address"] = res[i].street_number + " " + res[i].street_name + " "+ res[i].street_type +", " +res[i].city + ", " + res[i].state;
    }
      return res;})
    .then((data) => {
      console.log(data);
      res.send({ data: data });
    })
    .catch((err) => {
      console.log(err);
      res.redirect('/error');
    });
});

app.listen(port, () => console.log(`Example app listening on port ${port}!`));