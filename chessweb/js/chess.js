
//code: https://codepen.io/viethoang012/pen/xRNgyM

let plrOne = {
                'r11':["♜",3],
                'n11':["♞",5],
                'b11':["♝",7],
                'q11':["♛",9],
                'k11':["♚",11],
                'b12':["♝",13],
                'n12':["♞",15],
                'r12':["♜",17],
                'p11':["♟",19],
                'p12':["♟",21],
                'p13':["♟",23],
                'p14':["♟",25],
                'p15':["♟",27],
                'p16':["♟",29],
                'p17':["♟",31],
                'p18':["♟",33],
                };

let plrTwo = {
                    'p21':["♙",99],
                    'p22':["♙",101],
                    'p23':["♙",103],
                    'p24':["♙",105],
                    'p25':["♙",107],
                    'p26':["♙",109],
                    'p27':["♙",111],
                    'p28':["♙",113],
                    'r21':["♖",115],
                    'n21':["♘",117],
                    'b21':["♗",119],
                    'q21':["♕",121],
                    'k21':["♔",123],
                    'b22':["♗",125],
                    'n22':["♘",127],
                    'r22':["♖",99],
                    };

let availMoves = [];

let poi=0; //piece of interest index
let moveList=[];

function populateBoard() {
    let dv=document.getElementsByTagName('div');

    for (let i in plrOne) {
        dv[plrOne[i][1]].innerText=plrOne[i][0];
        //console.log(plrOne[i]);
    }
    debugger;
    for (let j in plrTwo) {
        dv[plrTwo[j][1]].innerText=plrTwo[j][0];
        //console.log(plrTwo[i]);
    }
}

function refreshGrid() {
    let dv=document.getElementsByTagName('div');
    for (let v=2;v<64+2;v++) {
        //debugger;
        startclr = (parseInt( ((v-2)/8) % 2)==0 ) ? 'white':'gray';
        endclr = (parseInt( ((v-2)/8) % 2)==0 ) ? 'gray':'white';
        dv[v].style.backgroundColor = (v%2==0 ) ? startclr:endclr;
        dv[v].remove
    }
    createButtons();
}

let availableMoves =  function(){
    //console.log('Available Moves hello');
    refreshGrid();
    let dv=document.getElementsByTagName('div');
    for (var i = 0;i<dv.length; i++) {
        if (window.getSelection().baseNode.parentNode == dv[i]) {
            //debugger;
            poi=i;
            dv[i+8].style.backgroundColor='red';
            dv[i+16].style.backgroundColor='red';
            availMoves.push(i+8);
            availMoves.push(i+16);
            dv[i+8].addEventListener('click',movePiece,false);
            dv[i+16].addEventListener('click',movePiece,false);
        }
    }
}

let movePiece = function() {
    //console.log('Available Moves hello');
    let dv=document.getElementsByTagName('div');
    refreshGrid();
    for (var i = 0;i<dv.length; i++) {
        if (window.getSelection().baseNode.parentNode == dv[i]) {
            //debugger;
            dv[i].innerText = dv[poi].innerText;
            //dv[poi].removeEventListener('click',availableMoves);//removing original piece
            for (let k=0;k<availMoves.length;k++){
                dv[availMoves[k]].removeEventListener('click',movePiece);
            }
        }
    }
}

function createButtons(){
    let dv=document.getElementsByTagName('div');
    for (var i = 0;i<dv.length/2;i++) {
        //debugger;
        if (dv[i]){
            if ((dv[i].innerText.length > 0) & (dv[i].innerText.length < 3)){
                if (dv[i+8].innerText.length == 0){
                    dv[i].addEventListener('click',availableMoves,false);
                }
            }
        }
    }
}

populateBoard();
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
