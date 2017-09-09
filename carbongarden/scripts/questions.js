function check() {
  points=0;
  if( document.getElementById("Carpool").checked == true){
    points+=1;
  }
  if( document.getElementById("Public Transit").checked == true){
    points+=1;
  }
  if( document.getElementById("Walk").checked == true){
    points+=1;
  }
  if( document.getElementById("Bike").checked == true){
    points+=1;
  }
  if( document.getElementById("Turned off all lights").checked == true){
    points+=1;
  }
  if( document.getElementById("Turned off faucet").checked == true){
    points+=1;
  }
  if( document.getElementById("Did a full load of laundry").checked == true){
    points+=1;
  }
  if( document.getElementById("Thermostat reads 68 in the winter or 75 in the summer").checked == true){
    points+=1;
  }
  if( document.getElementById("Used a reusable water bottle").checked == true){
    points+=1;
  }

  if( document.getElementById("Recycled all bottles and cans").check == true){
    points+=1;
  }

  if( document.getElementById("Composted").checked == true){
    points+=1;
  }
  if( document.getElementById("Recycled paper").checked == true){
    points+=1;
  }
  if( document.getElementById("Chose local food products").checked == true){
    points+=1;
  }
  if( document.getElementById("Used your own dishes").checked == true){
    points+=1;
  }
  if( document.getElementById("Organic").checked == true){
    points+=1;
  }
  if( document.getElementById("Reduced packaged meat consumption").checked == true){
    points+=1;
  }
  return points;
}
document.getElementById("submit").onclick=function() {
var score= check();
console.log(score);
document.getElementById("score").innerHTML= "Score: "  + score.toString();}




Read more: http://javarevisited.blogspot.com/2013/02/disable-submit-button-in-html-javascript-avoid-multiple-form-submission.html#ixzz4sCdnfZ3s
