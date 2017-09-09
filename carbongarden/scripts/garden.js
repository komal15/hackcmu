var c = document.getElementById("myCanvas");
var ctx = c.getContext("2d");
var totalpts = 100;
var increm = 5;
var cols = ["#C489FF","#7ABAF9","#DB7474","#E570E5","#FC9328","#8686F9","#F7C42A","#FC80BE" ];
var fillcols = ["rgb(229, 204, 255)","rgb(153, 204, 255)","rgb(255, 153, 153)","rgb(255, 153, 255)","rgb(255, 179, 102)","rgb(153, 153, 255)","rgb(255, 217, 102)", "rgb(255, 153, 204)"]
var width = window.innerWidth
|| document.documentElement.clientWidth
|| document.body.clientWidth;

var height = window.innerHeight
|| document.documentElement.clientHeight
|| document.body.clientHeight;
ctx.canvas.width  = width;
  ctx.canvas.height= height;



  var c = document.getElementById("myCanvas");
  var ctx = c.getContext("2d");
  var totalpts = 100;
  var increm = 5;
  var cols = ["#7ABAF9","#C489FF","#DB7474","#E570E5","#FC80BE","#8686F9","#F7C42A", "#FC9328"];
  var fillcols = ["rgb(153, 204, 255)","rgb(229, 204, 255)","rgb(255, 153, 153)","rgb(255, 153, 255)","rgb(255, 153, 204)","rgb(153, 153, 255)","rgb(255, 217, 102)", "rgb(255, 179, 102)"]
  var width = window.innerWidth
  || document.documentElement.clientWidth
  || document.body.clientWidth;

  var height = window.innerHeight
  || document.documentElement.clientHeight
  || document.body.clientHeight;
  ctx.canvas.width  = width;
    ctx.canvas.height= height;



  function grow(currentX, col, fillcol, currentY){
  function drawFlower(){

  ctx.strokeStyle=col;
  ctx.lineWidth=1;
  ctx.fillStyle=fillcol;
  ctx.beginPath();
  ctx.ellipse(currentX,currentY, 0.01*width, 0.04*width,  Math.PI, 0, 2 * Math.PI);
  ctx.ellipse(currentX,currentY,  0.01*width,  0.04*width,  Math.PI/5, 0, 2 * Math.PI)
  ctx.ellipse(currentX,currentY,  0.01*width,  0.04*width,  2 * Math.PI/5, 0, 2 * Math.PI)
  ctx.ellipse(currentX,currentY,  0.01*width,  0.04*width,  3 * Math.PI/5, 0, 2 * Math.PI)
  ctx.ellipse(currentX,currentY,  0.01*width,  0.04*width,  4 * Math.PI/5, 0, 2 * Math.PI)
  ctx.fill();
  ctx.stroke();
  ctx.beginPath();
  ctx.arc(currentX,currentY,0.01*width,0,2*Math.PI);
  ctx.fillStyle=col;
  ctx.fill();

  }

  function drawLine(x1,y1,x2,y2,ratio) {

    ctx.moveTo(x1,y1);
    x2 = x1 + ratio * (x2-x1);
    y2 = y1 + ratio * (y2-y1);
    ctx.lineTo(x2,y2);
    ctx.strokeStyle="#0B8E3F";
    ctx.lineWidth=0.006 * width;
    ctx.stroke();
    ctx.restore();
  }

  function animate(ratio) {
    ratio = ratio || 0;
    drawLine(currentX, currentY + 0.28*height,currentX,currentY + 0.07*height,ratio);


    if(ratio<1) {
      requestAnimationFrame(function() {
        animate(ratio + 0.01);
      });

    }

    drawFlower();
    ctx.beginPath();
        ctx.strokeStyle="#0B8E3F";
      ctx.moveTo(currentX,currentY + 0.25*height);
      ctx.bezierCurveTo(currentX-0.08*width, currentY + 0.15*height, currentX, currentY + 0.2 *height, currentX, currentY + 0.22* height);
      ctx.stroke();
      ctx.fillStyle="#0B8E3F";
      ctx.fill();
      ctx.moveTo(currentX,currentY + 0.25*height);
      ctx.bezierCurveTo(currentX, currentY + 0.2*height, currentX+0.05*width, currentY + 0.2*height, currentX + 0.015*width, currentY + 0.15*height);
      ctx.stroke();
      ctx.fillStyle="#0B8E3F";
      ctx.fill();
  }
  animate();
  }

  function garden(){
    for(var i=1;i<9;i++){
      if(i%2==0){
  grow(0.10*width *i ,cols[i-1],fillcols[i-1], 0.60 *height);
  }
  else{
    grow(0.10*width * i ,cols[i-1],fillcols[i-1], 0.40 *height);
  }
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
