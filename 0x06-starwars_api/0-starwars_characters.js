#!/usr/bin/node
const { argv } = require('process');
const request = require('request');



function GetAllStarWarMovieChar (){
  return new Promise((resolve, reject) =>{
    const baseUrl = "https://swapi-api.alx-tools.com/api/films/";
    const film_id = argv[2];
    const url = baseUrl.concat(film_id);
    request.get(url, (error, res, body) =>{
      if (error){
        return
      }
      if (res.statusCode == 200){ 
        resolve(JSON.parse(body)['characters']);
      }
    })
  });
}

const printStarWarChar = (links, index) =>  {
  if (links.length <= index){
    return
  }
  const url = links[index]
  request.get(url, (error, res, body) => {
    console.log(JSON.parse(body).name);
    printStarWarChar(links, index + 1);
  }) 
}


GetAllStarWarMovieChar().then((res) => printStarWarChar(res, 0))
