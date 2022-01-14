
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
let availKingList=[];
let checkbool=false;

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

function availableMoves(z){
    //find all the available moves
    refreshGrid();
    pcidx=z;
    let dv=document.getElementsByTagName('div');
    key=getKey(z);
    //if (key==-1){console.log("No key found: "+key);}
    availMoves = (key==-1) ? null:pcdict[key[0]](key);
    //availMoves = (typeof(availMoves[0])=="number") ? [availMoves]:availMoves;
    if(dv[z].innerText != ''){
      for (let k=0;k<availMoves.length;k++) {
        dv[availMoves[k]].style.backgroundColor='blue';
        dv[availMoves[k]].style.opacity=0.5;
      }
    }
}

function availableMoves2(z){
  //find all the available moves
  refreshGrid();
  pcidx=z;
  let dv=document.getElementsByTagName('div');
  key=getKey(z);
  //if (key==-1){console.log("No key found: "+key);}
  availMoves = (key==-1) ? null:pcdict[key[0]](key);
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

function checkKing(){
  let dv=document.getElementsByTagName('div');
  let kidx=0;
  let klist=[];
  let counter=0;
  availKingList=[];
  for (let idx in playerpcs) {
    if(playerpcs[idx][2] == player){
      availableMoves2(playerpcs[idx][1]);
      for(idx2=0;idx2<availMoves.length;idx2++){
        koi = getKey(availMoves[idx2]);
        if(koi==-1) {
          continue;
        }
        else if(koi.includes('k')){
          if(playerpcs[koi][2]!=player){
            availKingList=availKingList.concat(availMoves);
            //break;
          }
        }
      }
    }
  }
  //debugger;
}

function checkintersection(kingavailmoves){
  remainingKingMoves=[];
  kingbool=false;
  for(let kidx=0;kidx<kingavailmoves.length;kidx++){
    kingbool=false;
    for(let kidx2=0;kidx2<availKingList.length;kidx2++){
      if(availKingList[kidx2]==kingavailmoves[kidx]){
        kingbool=true;
      }
    }
    if(kingbool==false){
      remainingKingMoves.push(kingavailmoves[kidx])
    }
  }
  return remainingKingMoves;
}

function checkKingBool(){
  checkKing()
  checkbool=false;
  if (availKingList.length > 0){
    player = (player==1) ? 2:1;
    //debugger;
    kingstr = 'k'+String(player)+'1';
    kingavailmoves = kingMove(kingstr);
    remainingKingMoves = checkintersection(kingavailmoves);
    if(remainingKingMoves.length==0){
      console.log("GAME OVER!!");
      let md=document.getElementsByTagName('div')[0];
      md.style.fontSize='400%';
      md.style.color='red';
      //md.='blue';
      md.innerText="GAME OVER!";
    }
    else if(availKingList.length==0){
      checkbool=false;
    }
    else{
      //debugger;
      availableMoves(playerpcs[kingstr][1]);
      checkbool=true;
    }
    player = (player==2) ? 1:2;
    //debugger;
  }
  //tempplayer = (player==1) ? 2:1;
  //console.log("Check for player "+String(tempplayer));
}

function checkpc(tdv,idx) {
  let dv=document.getElementsByTagName('div');
  if(player==1){
    if(dv[idx].style.backgroundColor=='blue'){
      updatedict(idx);
      updateBoard();
      checkKingBool();
      player=2;
    }
    else if ((dv[idx].innerText==tdv.innerText) & (checkplayerpc(idx)==true) & 
            (checkbool==false)){
              availKingList=[];
              availableMoves(idx);
    }
  }
  else if(player==2){
    if(dv[idx].style.backgroundColor=='blue'){
      updatedict(idx);
      updateBoard();
      checkKingBool();
      player=1;
    }
    else if((dv[idx].innerText==tdv.innerText) & (checkplayerpc(idx)==true) & 
           (checkbool==false)){
            availKingList=[];
            availableMoves(idx);
    }
  }
  //let dv=document.getElementsByTagName('div');
  //debugger;
  dv[dv.length-1].style.color='black';
  dv[dv.length-1].style.fontSize='large';
  dv[dv.length-1].innerHTML="Player "+String(player);
  dv[dv.length-1].innerText="Player "+String(player);
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

function checkPiecesKnight(boundedList){
  keepOpponentList=[];
  let dv=document.getElementsByTagName('div');
  for(let l=0;l<boundedList.length;l++){
    r=boundedList[l][0];
    c=boundedList[l][1];
    idx=8*parseInt(r)+c+1;
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
    r1=rcList[l][0];
    c1=rcList[l][1];
    idx=8*parseInt(r1)+c1+1;
    finalList.push(idx);
  }
  return finalList;
}

function knightMove(i){
  d=playerpcs[i];
  loc=d[1]-1;
  row=Math.floor(loc/8);
  col=(loc%8);
  loclist= [
    [row+2,col+1],
    [row+2,col-1],
    [row-2,col+1],
    [row-2,col-1],
    [row-1,col+2],
    [row-1,col-2],
    [row+1,col+2],
    [row+1,col-2],
    ]
  boundedList=removeBoundaries(loclist);
  keepOpponentList=checkPiecesKnight(boundedList);
  finalList=convertToIdx(keepOpponentList);
  return finalList;
  //debugger;
}

function bishopMove(i){
  let dv=document.getElementsByTagName('div');
  d=playerpcs[i];
  loc=d[1]-1;
  row=Math.floor(loc/8);
  col=(loc%8);
  loclist=[];
  //positive down diag
  for(let j=1;j<8;j++){
    tval=[row+j,col+j];
    if((tval[0] >=8) | (tval[1] >=8)){break;}
    temp=convertToIdx([tval]);
    keyoi=getKey(temp);
    if(dv[temp].innerText==''){
      loclist.push(tval);
    }
    else if(playerpcs[keyoi][2]!=player){
      loclist.push(tval);
      break;
    }
    else if(playerpcs[keyoi][2]==player){
      break;
    }
  }
  //diagnal going up and left
  for(let j=1;j<8;j++){
    tval=[row-j,col-j];
    if((tval[0] <0) | (tval[1] <0)){break;}
    temp=convertToIdx([tval]);
    keyoi=getKey(temp);
    if(dv[temp].innerText==''){
      loclist.push(tval);
    }
    else if(playerpcs[keyoi][2]!=player){
      loclist.push(tval);
      break;
    }
    else if(playerpcs[keyoi][2]==player){
      break;
    }
  }
  //diaganol going left and down
  for(let j=1;j<8;j++){
    tval=[row+j,col-j];
    if((tval[0] >=8) | (tval[1] <0)){break;}
    temp=convertToIdx([tval]);
    keyoi=getKey(temp);
    if(dv[temp].innerText==''){
      loclist.push(tval);
    }
    else if(playerpcs[keyoi][2]!=player){
      loclist.push(tval);
      break;
    }
    else if(playerpcs[keyoi][2]==player){
      break;
    }
  }
  //diaganol going right and up
  for(let j=1;j<8;j++){
    tval=[row-j,col+j];
    if((tval[0] <0) | (tval[1] >=8)){break;}
    temp=convertToIdx([tval]);
    keyoi=getKey(temp);
    if(dv[temp].innerText==''){
      loclist.push(tval);
    }
    else if(playerpcs[keyoi][2]!=player){
      loclist.push(tval);
      break;
    }
    else if(playerpcs[keyoi][2]==player){
      break;
    }
  }
  finalList=convertToIdx(loclist);
  return finalList;
}

function pawnMove(i){
  let dv=document.getElementsByTagName('div');
  d=playerpcs[i];
  loc=d[1]-1;
  row=Math.floor(loc/8);
  col=(loc%8);
  if (player==1){
    loclist=[
      [row+1,col],
      [row+1,col-1],
      [row+1,col+1],
    ]
  }
  else if(player==2){
    loclist=[
      [row-1,col],
      [row-1,col-1],
      [row-1,col+1],
    ]
  }
  boundedList=removeBoundaries(loclist);
  //keepOpponentList=checkPiecesKnight(boundedList);
  //debugger;
  updatedList=(dv[convertToIdx([loclist[0]])].innerText=='') ? [loclist[0]]:[];
  for(let x=0;x<boundedList.length;x++){
    tr=boundedList[x][0];
    tc=boundedList[x][1];
    if((tc==col-1) | (tc==col+1)){
      pidx=8*parseInt(tr)+tc+1;
      //debugger;
      if(dv[pidx].innerText!=''){
        //debugger;
        updatedList.push([tr,tc]);
      }
    }
  }
  keepOpponentList=checkPiecesKnight(updatedList);
  finalList=convertToIdx(keepOpponentList);
  return finalList;
}

function rookMove(i){
  let dv=document.getElementsByTagName('div');
  d=playerpcs[i];
  loc=d[1]-1;
  row=Math.floor(loc/8);
  col=(loc%8);
  loclist=[];
  //fixing x
  //fixing x to end
  for(let j=row+1;j<8;j++){
    tval=[j,col];
    temp=convertToIdx([tval]);
    keyoi=getKey(temp);
    if(dv[temp].innerText==''){
      loclist.push(tval);
    }
    else if(playerpcs[keyoi][2]!=player){
      loclist.push(tval);
      break;
    }
    else if(playerpcs[keyoi][2]==player){
      break;
    }
  }
  
  //fixing 0 to x
  for(let j=row-1;j>=0;j--){
    tval=[j,col];
    temp=convertToIdx([tval]);
    keyoi=getKey(temp);
    if(dv[temp].innerText==''){
      loclist.push(tval);
    }
    else if(playerpcs[keyoi][2]!=player){
      loclist.push(tval);
      break;
    }
    else if(playerpcs[keyoi][2]==player){
      break;
    } 
  }

  //fixing y
  //fixing y to end
  for(let j=col+1;j<8;j++){
    tval=[row,j];
    temp=convertToIdx([tval]);
    keyoi=getKey(temp);
    if(dv[temp].innerText==''){
      loclist.push(tval);
    }
    else if(playerpcs[keyoi][2]!=player){
      loclist.push(tval);
      break;
    }
    else if(playerpcs[keyoi][2]==player){
      break;
    } 
  }
  //fixing 0 to y
  for(let j=col-1;j>=0;j--){
    tval=[row,j];
    temp=convertToIdx([tval]);
    keyoi=getKey(temp);
    if(dv[temp].innerText==''){
      loclist.push(tval);
    }
    else if(playerpcs[keyoi][2]!=player){
      loclist.push(tval);
      break;
    }
    else if(playerpcs[keyoi][2]==player){
      break;
    } 
  
  }
  //debugger;
  finalList=convertToIdx(loclist);
  return finalList;

}

function kingMove(i){
  let dv=document.getElementsByTagName('div');
  d=playerpcs[i];
  loc=d[1]-1;
  row=Math.floor(loc/8);
  col=(loc%8);
  loclist=[
    [row+1,col],
    [row-1,col],
    [row+1,col+1],
    [row+1,col-1],
    [row-1,col+1],
    [row-1,col-1],
    [row,col+1],
    [row,col-1],
  ];
  boundedList=removeBoundaries(loclist);
  keepOpponentList=checkPiecesKnight(boundedList);
  finalList=convertToIdx(keepOpponentList);
  return finalList;
}

function queenMove(i){
  bMoves=bishopMove(i);
  rMoves=rookMove(i);
  finalList=bMoves.concat(rMoves);
  return finalList;
}