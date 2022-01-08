
//code: https://codepen.io/viethoang012/pen/xRNgyM

let plrOne = {
                'r11':["♜",1],
                'n11':["♞",2],
                'b11':["♝",3],
                'q11':["♛",4],
                'k11':["♚",5],
                'b12':["♝",6],
                'n12':["♞",7],
                'r12':["♜",8],
                'p11':["♟",9],
                'p12':["♟",10],
                'p13':["♟",11],
                'p14':["♟",12],
                'p15':["♟",13],
                'p16':["♟",14],
                'p17':["♟",15],
                'p18':["♟",16],
                };

let plrTwo = {
                    'p21':["♙",49],
                    'p22':["♙",50],
                    'p23':["♙",51],
                    'p24':["♙",52],
                    'p25':["♙",53],
                    'p26':["♙",54],
                    'p27':["♙",55],
                    'p28':["♙",56],
                    'r21':["♖",57],
                    'n21':["♘",58],
                    'b21':["♗",59],
                    'q21':["♕",60],
                    'k21':["♔",61],
                    'b22':["♗",62],
                    'n22':["♘",63],
                    'r22':["♖",64],
                    };

let availMoves = [];

let poi=0; //piece of interest index
let moveList=[];
player=1;

function populateBoard() {
    let dv=document.getElementsByTagName('div');
    refreshGrid();
    for (let i in plrOne) {
        dv[plrOne[i][1]].innerText=plrOne[i][0];
        //console.log(plrOne[i]);
    }

    for (let j in plrTwo) {
        dv[plrTwo[j][1]].innerText=plrTwo[j][0];
        //console.log(plrTwo[j]);
    }
}

function refreshGrid() {
    let dv=document.getElementsByTagName('div');
    for (let v=1;v<65;v++) {
        //debugger;
        startclr = (parseInt( ((v-1)/8) % 2)==0 ) ? 'white':'gray';
        endclr = (parseInt( ((v-1)/8) % 2)==0 ) ? 'gray':'white';
        dv[v].style.backgroundColor = (v%2==0 ) ? startclr:endclr;
        dv[v].style.opacity=1;
    }
}

function availableMoves(z,player){
    //find all the available moves
    refreshGrid();
    let dv=document.getElementsByTagName('div');
    availMoves=[z+8,z+16];
    for (let k=0;k<availMoves.length;k++) {
      dv[availMoves[k]].style.backgroundColor='red';
      dv[availMoves[k]].style.opacity=0.5;
    }
}

function checkpc(tdv,idx,player) {
  let dv=document.getElementsByTagName('div');
  if(player==1){
    for (let i in plrOne) {
        if(dv[plrOne[i][1]].innerText==tdv.innerText){
          availableMoves(idx,player);
        }
    }
  }
  if(player==2) {
    for (let j in plrTwo) {
      if(dv[plrOne[j][1]].innerText==tdv.innerText){
        availableMoves(idx,player);
        }
    }
  }
}

function mouseclick(event) {
  let dv=document.getElementsByTagName('div');
  clickX=event.clientX;
  clickY=event.clientY;
  for (var i=1;i<dv.length;i++){
    topoffset  = dv[i].offsetParent.offsetTop + dv[i].offsetParent.clientTop;
    leftoffset = dv[i].offsetParent.offsetLeft + dv[i].offsetParent.clientLeft
    divheight  = dv[i].offsetHeight;
    divwidth    = dv[i].offsetWidth;
    tdv=dv[i];
    if ((clickX > tdv.offsetLeft+leftoffset) & (clickX < tdv.offsetLeft+leftoffset+divwidth) &
        (clickY > tdv.offsetTop+topoffset) & (clickY < tdv.offsetTop+topoffset+divheight)) {
          checkpc(tdv,i,player);
          console.log("Div number: "+i);
        }
  }

}

populateBoard();
document.addEventListener("click",mouseclick);
//createButtons();

/*var dv = document.getElementsByTagName('div');
var idx=2;
console.log(dv[idx].innerText);

var temp=dv[idx];
var container = temp;
var dragItem=temp;
var active = false;
var currentX;
var currentY;
var initialX;
var initialY;
var xOffset = 0;
var yOffset = 0;


temp.addEventListener("touchstart", dragStart, false);
temp.addEventListener("touchend", dragEnd, false);
temp.addEventListener("touchmove", drag, false);

temp.addEventListener("mousedown", dragStart, false);
temp.addEventListener("mouseup", dragEnd, false);
temp.addEventListener("mousemove", drag, false);

function dragStart(e) {
  if (e.type === "touchstart") {
    initialX = e.touches[0].clientX - xOffset;
    initialY = e.touches[0].clientY - yOffset;
  } else {
    initialX = e.clientX - xOffset;
    initialY = e.clientY - yOffset;
  }
  

  if (e.target === temp) {
    active = true;
  }
}

function dragEnd(e) {
  initialX = currentX;
  initialY = currentY;
  console.log(e);
 
  active = false;
}

function drag(e) {
  if (active) {
  
    e.preventDefault();
  
    if (e.type === "touchmove") {
      currentX = e.touches[0].clientX - initialX;
      currentY = e.touches[0].clientY - initialY;
    } else {
      currentX = e.clientX - initialX;
      currentY = e.clientY - initialY;
    }

    xOffset = currentX;
    yOffset = currentY;

    setTranslate(currentX, currentY, temp);
  }
}

function setTranslate(xPos, yPos, el) {
  el.style.transform = "translate3d(" + xPos + "px, " + yPos + "px, 0)";
}*/
