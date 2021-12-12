
function create_board() {
  //creating a board for chess
  //cbp are the chess board pieces
  //cbt is the mask based on each piece i selected
	var cbp = new Array(8);//chess board
	var cbt = new Array(8);//chess board
	for (var i =0;i<8;i++) {
		cbp[i]=new Array(8);
		cbt[i]=new Array(8);
	}
	for (var i=0;i<8;i++) {
		for (var j=0;j<8;j++) {
			cbp[i][j]='';
			cbt[i][j]=0;
		}
	}
  //Positioning each piece in it's appropriate location
	cbp[0][0]='R11'; cbp[0][7]='R12'; cbp[7][0]='R21'; cbp[7][7]='R22';
	cbp[0][1]='N11'; cbp[0][6]='N12'; cbp[7][1]='N21'; cbp[7][6]='N22';
	cbp[0][2]='B11'; cbp[0][5]='B12'; cbp[7][2]='B21'; cbp[7][5]='B22';
	cbp[0][3]='K1';  cbp[0][4]='Q1';  cbp[7][3]='K2';  cbp[7][4]='Q2';
	//setting up the location of pawns
  for (var i=0;i<8;i++) {
		cbp[2][i]='P1'+i;
		cbp[6][i]='P2'+i;
	}
	return {cbp,cbt};
}

function create_chessboard() { 
	// Create a center tag to center all the elements
	var center = document.createElement('center');

	// Create a table element
	var ChessTable = document.createElement('table');
	for (var i = 0; i < 8; i++) {

	    // Create a row
	    var tr = document.createElement('tr');
	    for (var j = 0; j < 8; j++) {

		// Create a cell
		var td = document.createElement('td');

		// If the sum of cell coordinates is even
		// then color the cell white
		if ((i + j) % 2 == 0) {

		    // Create a class attribute for all white cells
		    td.setAttribute('class', 'cell greencell');
		    tr.appendChild(td);
		}

		// If the sum of cell coordinates is odd then
		// color the cell black
		else {

		    // Create a class attribute for all black cells
		    td.setAttribute('class', 'cell darkgreencell');
		    td.onClick=(function() {console.log("hello")});

		    // Append the cell to its row
		    tr.appendChild(td);
		}
	    }

	    // Append the row
	    ChessTable.appendChild(tr);
	}
	center.appendChild(ChessTable);

	// Modifying table attribute properties
	ChessTable.setAttribute('cellspacing', '0');
	ChessTable.setAttribute('width', '270px');
	document.body.appendChild(center);
}

function movep(cbp,cbt,i,j) {
	//Creating rules for pawn
  console.log('P');
	//console.log(cbp);
	refresh_colors(cbp,cbt);
	if ((i>=0) & (i<=7)) {
		if(cbp[i+1][j].length<2) {
			//Based on player 1, if the location below the pawn is open then cbt masks that as 1
			cbt[i+1][j]=1;
		}
	}
	if ( (i+1 < 8) & (j+1 < 8) ) {
		if ( (cbp[i+1][j+1].indexOf(1) !== cbp[i][j].indexOf(1)) & (cbp[i+1][j+1].length>1) ) {
			cbt[i+1][j+1]=1;
      //allows for moving diagnally if opposing player is present
		}		
	}
	if ( (i+1 < 8) & (j-1 >= 0) ) {
		if ( (cbp[i+1][j-1].indexOf(1) !== cbp[i][j].indexOf(1)) & (cbp[i+1][j-1].length>1) ) {
			cbt[i+1][j-1]=1;
      //allows for moving diagnally if opposing player is present
		}		
	}
	potential_moves(cbp,cbt,[i,j]);
  update_board(cbp,cbt);
}

var possiblelocs=function(event,i,j,cbp,cbt) {
	//based on string value of cbp (the chess piece of interest) 
  //I have to create rules for possible ways it can go
  if (cbp[i][j].includes('P') ) {movep(cbp,cbt,i,j);}
	else if (cbp[i][j].includes('K')) {console.log('K');}
	else if (cbp[i][j].includes('N')) {movep(cbp,cbt,i,j);}//using the function for pawn here for debugging purposes
	else if (cbp[i][j].includes('Q')) {console.log('Q');}
	else if (cbp[i][j].includes('R')) {movep(cbp,cbt,i,j);}//using the function for pawn here for debugging purposes
	else if (cbp[i][j].includes('B')) {console.log('B');}
	//console.log(cbp);
}

function update_board(cbp,cbt) {
  //fills the board with all the proper pieces
  var elem = document.getElementsByTagName('td');
  //console.log(cbp);
  for(var i=0;i<8;i++) {
  	for(var j=0;j<8;j++) {
  		elem[8*i+j].innerHTML=cbp[i][j];
  		if (elem[8*i+j].innerHTML.length > 1) {
        //create a clickable EventListener if there is a string value >1 (i.e. not-empty)
	  		elem[8*i+j].addEventListener( "click",possiblelocs.bind(event,'str',i,j,cbp,cbt) );
	  	}
  	}
  }
}

function refresh_colors(cbp,cbt) {
  //fills the board with colors
  var elem = document.getElementsByTagName('td');
  for(var i=0;i<8;i++) {
  	for(var j=0;j<8;j++) {
      //set the color based on location of cell
			if ((i + j) % 2 == 0) {
				  elem[8*i+j].setAttribute('class', 'cell greencell');
			}
			else {
				  elem[8*i+j].setAttribute('class', 'cell darkgreencell');
	  	}
	  	cbt[i][j]=0;//reset the chess board mask to 0
  	}
  }
}

var movelocs=function(event,i,j,cbp,cbt,pc) {
  //replace old location of string in cbp to the new one
  cbp[i][j]=cbp[pc[0]][pc[1]];
	cbp[pc[0]][pc[1]]='';
  update_board(cbp,cbt);
}

function potential_moves(cbp,cbt,pc) {
  //updates the board with possible location a specific piece can move (based on cbt) 
  //and makes the red cells clickable
  var elem = document.getElementsByTagName('td');
  for(var i=0;i<8;i++) {
  	for(var j=0;j<8;j++) {
  		if (cbt[i][j]==1) {
				elem[8*i+j].setAttribute('class', 'cell redcell');
        //once click move the board to the new location
				elem[8*i+j].addEventListener( "click",movelocs.bind(event,'str',i,j,cbp,cbt,pc) );
			}
		}
	}
}

let {cbp,cbt}=create_board();
create_chessboard();
update_board(cbp,cbt);
