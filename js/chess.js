

var dv = document.getElementsByTagName('div');
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
}
