var c = document.getElementById("myCanvas");
var ctx = c.getContext("2d");
var totalpts = 100;
var increm = 5;
var cols = ["#7ABAF9","#C489FF","#DB7474","#E570E5","#FC80BE","#8686F9","#F7C42A", "#FC9328"];
var fillcols = ["rgba(153, 204, 255, 0.5)","rgba(229, 204, 255, 0.5)","rgba(255, 153, 153, 0.5)","rgba(255, 153, 255, 0.5)","rgba(255, 153, 204, 0.5)","rgba(153, 153, 255, 0.5)","rgb(255, 217, 102)", "rgb(255, 179, 102)"]


function grow(currentX, col, fillcol){
function drawFlower(){

ctx.strokeStyle=col;
ctx.lineWidth=1;
ctx.fillStyle=fillcol;
ctx.beginPath();
ctx.ellipse(currentX,500, 20, 80,  Math.PI, 0, 2 * Math.PI);
ctx.ellipse(currentX,500, 20, 80,  Math.PI/5, 0, 2 * Math.PI)
ctx.ellipse(currentX,500, 20, 80,  2 * Math.PI/5, 0, 2 * Math.PI)
ctx.ellipse(currentX,500, 20, 80,  3 * Math.PI/5, 0, 2 * Math.PI)
ctx.ellipse(currentX,500, 20, 80,  4 * Math.PI/5, 0, 2 * Math.PI)
ctx.fill();
ctx.stroke();
ctx.beginPath();
ctx.arc(currentX,500,20,0,2*Math.PI);
ctx.fillStyle=col;
ctx.fill();

}

function drawLine(x1,y1,x2,y2,ratio) {

  ctx.moveTo(x1,y1);
  x2 = x1 + ratio * (x2-x1);
  y2 = y1 + ratio * (y2-y1);
  ctx.lineTo(x2,y2);
  ctx.strokeStyle="#0B8E3F";
  ctx.lineWidth=10;
  ctx.stroke();
  ctx.restore();
}

function animate(ratio) {
  ratio = ratio || 0;
  drawLine(currentX,750,currentX,580,ratio);


  if(ratio<1) {
    requestAnimationFrame(function() {
      animate(ratio + 0.01);
    });

  }

  drawFlower();
  ctx.beginPath();
    ctx.moveTo(currentX,700);
    ctx.bezierCurveTo(currentX-180, 600, currentX, 650, currentX, 670);
    ctx.stroke();
    ctx.fillStyle="#0B8E3F";
    ctx.fill();
    ctx.moveTo(currentX,700);
    ctx.bezierCurveTo(currentX, 650, currentX+100, 650, currentX + 30, 600);
    ctx.stroke();
    ctx.fillStyle="#0B8E3F";
    ctx.fill();
}
animate();
}

function garden(){
  for(var i=1;i<9;i++){
grow(200 * i,cols[i-1],fillcols[i-1]);
}
}
garden();







// ctx.fillStyle="rgba(229, 204, 255, 0.5)";//
//ctx.strokeStyle="#C489FF";

//ctx.fillStyle="rgba(255, 153, 153, 0.5)";
//ctx.strokeStyle="#DB7474";

//ctx.fillStyle="rgba(255, 153, 255, 0.5)";
//ctx.strokeStyle="#E570E5";

//ctx.fillStyle="rgba(255, 153, 204, 0.5)";
//ctx.strokeStyle="#FC80BE";

//ctx.fillStyle="rgba(153, 153, 255, 0.5)";
//ctx.strokeStyle="#8686F9";

//ctx.fillStyle="rgba(153, 204, 255, 0.5)";
//ctx.strokeStyle="#7ABAF9";
