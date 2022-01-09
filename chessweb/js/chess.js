
//code: https://codepen.io/viethoang012/pen/xRNgyM

let playerpcs = {
                    'r11':["♜",1,1],
                    'n11':["♞",2,1],
                    'b11':["♝",3,1],
                    'q11':["♛",4,1],
                    'k11':["♚",5,1],
                    'b12':["♝",6,1],
                    'n12':["♞",7,1],
                    'r12':["♜",8,1],
                    'p11':["♟",9,1],
                    'p12':["♟",10,1],
                    'p13':["♟",11,1],
                    'p14':["♟",12,1],
                    'p15':["♟",13,1],
                    'p16':["♟",14,1],
                    'p17':["♟",15,1],
                    'p18':["♟",16,1],
                    'p21':["♙",49,2],
                    'p22':["♙",50,2],
                    'p23':["♙",51,2],
                    'p24':["♙",52,2],
                    'p25':["♙",53,2],
                    'p26':["♙",54,2],
                    'p27':["♙",55,2],
                    'p28':["♙",56,2],
                    'r21':["♖",57,2],
                    'n21':["♘",58,2],
                    'b21':["♗",59,2],
                    'q21':["♕",60,2],
                    'k21':["♔",61,2],
                    'b22':["♗",62,2],
                    'n22':["♘",63,2],
                    'r22':["♖",64,2],
                    };
cemetary={};
pcdict = {
  'n':knightMove,
  'b':bishopMove,
  'p':pawnMove,
  'r':rookMove,
  'k':kingMove,
  'q':queenMove,
}

let availMoves = [];

let pcidx=0; //piece of interest index
let moveList=[];
let player=1;
let movebool=false;
let keyoi='';

function populateBoard() {
    let dv=document.getElementsByTagName('div');
    refreshGrid();
    for (let i in playerpcs) {
        dv[playerpcs[i][1]].innerText=playerpcs[i][0];;
    }
}

function refreshGrid() {
    let dv=document.getElementsByTagName('div');
    for (let v=1;v<65;v++) {
        startclr = (parseInt( ((v-1)/8) % 2)==0 ) ? 'white':'gray';
        endclr = (parseInt( ((v-1)/8) % 2)==0 ) ? 'gray':'white';
        dv[v].style.backgroundColor = (v%2==0 ) ? startclr:endclr;
        dv[v].style.opacity=1;
    }
}

function getKey(idx){
  for (let i in playerpcs) {
    if(playerpcs[i][1] == idx){
      return i
    }
  }
  return -1;
}

function clearBoard(){
  let dv=document.getElementsByTagName('div');
  for (let v=1;v<dv.length;v++) {
      dv[v].innerText='';
  }
}

function updateBoard() {
  let dv=document.getElementsByTagName('div');
  refreshGrid();
  clearBoard();
  for (let i in playerpcs) {
    dv[playerpcs[i][1]].innerText=playerpcs[i][0]
  }
}

function availableMoves(z,poi){
    //find all the available moves
    refreshGrid();
    pcidx=z;
    let dv=document.getElementsByTagName('div');
    key=getKey(z);
    //if (key==-1){console.log("No key found: "+key);}
    tmp = (key==-1) ? null:pcdict[key[0]](key);
    if(dv[z].innerText != ''){
      for (let k=0;k<availMoves.length;k++) {
        dv[availMoves[k]].style.backgroundColor='red';
        dv[availMoves[k]].style.opacity=0.5;
      }
    }
}

function killpc(idx) {
  let dv=document.getElementsByTagName('div');
  for (let i in playerpcs) {
    if((playerpcs[i][1] == idx) & (playerpcs[i][2] != player)){
      cemetary[i]=playerpcs[i];
      delete playerpcs[i];
    }
  }
}

function updatedict(idx){
  let dv=document.getElementsByTagName('div');

  for (let i in playerpcs) {
    if(playerpcs[i][2]==player) {
      if(playerpcs[i][1]==pcidx){
        if(playerpcs[i][1])
        killpc(idx);
        playerpcs[i][1]=idx;
        dv[playerpcs[i][1]].innerText=playerpcs[i][0];
      }
    }
  }
}

function checkplayerpc(idx){
  
  for (let i in playerpcs) {
    if(playerpcs[i][2]==player) {
      if((playerpcs[i][2]==player) & (playerpcs[i][1]==idx) ){
        return true;
      }
    }
  }
  return false;
}

function checkpc(tdv,idx) {
  let dv=document.getElementsByTagName('div');
  if(player==1){
    if(dv[idx].style.backgroundColor=='red'){
      updatedict(idx);
      updateBoard();
      player=2;
    }
    else if ((dv[idx].innerText==tdv.innerText) & (checkplayerpc(idx)==true)){
      availableMoves(idx);
    }
  }
  else if(player==2){
    if(dv[idx].style.backgroundColor=='red'){
      updatedict(idx);
      updateBoard();
      player=1;
    }
    else if((dv[idx].innerText==tdv.innerText) & (checkplayerpc(idx)==true)){
      availableMoves(idx);
    }
  }
  console.log(pcidx)
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


/* BELOW HERE ARE FIGURING ARE THE AVAILABLE OPTIONS FOR A CERTAIN PIECE*/

function removeBoundaries(loclist){
  primedList=[];
  for(let l=0;l<loclist.length;l++){
    r=loclist[l][0];
    c=loclist[l][1];
    if ((r<8) & (r>=0) & (c<8) & (c>=0)) {
      primedList.push([r,c]);
    }
  }
  return primedList;
}

function checkPieces(boundedList){
  keepOpponentList=[];
  let dv=document.getElementsByTagName('div');
  for(let l=0;l<boundedList.length;l++){
    r=boundedList[l][0];
    c=boundedList[l][1];
    idx=8*parseInt(r)+c;
    key=getKey(idx);
    if(dv[idx].innerText!=''){
      if (playerpcs[key][2]!=player){
        keepOpponentList.push([r,c]);
      }
    }
    else {
      keepOpponentList.push([r,c]);
    }
  }
  return keepOpponentList;
}

function convertToIdx(rcList){
  finalList=[];
  for(let l=0;l<rcList.length;l++){
    r=boundedList[l][0];
    c=boundedList[l][1];
    idx=8*parseInt(r)+c;
    finalList.push(idx);
  }
  return finalList;
}

function knightMove(i){
  d=playerpcs[i];
  loc=d[1];
  r=parseInt(loc/8);
  c=loc%8;
  loclist= [
    [r+2,c+1],
    [r+2,c-1],
    [r-2,c+1],
    [r-2,c-1],
    [r-1,c+2],
    [r-1,c-2],
    [r+1,c+2],
    [r+1,c-2],
    ]
  boundedList=removeBoundaries(loclist);
  keepOpponentList=checkPieces(boundedList);
  finalList=convertToIdx(keepOpponentList);
  availMoves=finalList;
}

function bishopMove(i){
  d=playerpcs[i];
  loc=d[1];
}
function pawnMove(i){
  d=playerpcs[i];
  loc=d[1];
}
function rookMove(i){
  d=playerpcs[i];
  loc=d[1];
}
function kingMove(i){
  d=playerpcs[i];
  loc=d[1];
}
function queenMove(i){
  d=playerpcs[i];
  loc=d[1];
}