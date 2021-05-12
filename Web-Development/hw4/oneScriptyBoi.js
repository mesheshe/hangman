function createElements(){
    var newTable = document.createElement("table");
    var newRow = document.createElement("tr");
    for (var i = 1; i <= 4; i++){
        var newHeader = document.createElement("th");
        newHeader.textContent = `Header ${i}`;
        newHeader.setAttribute("id", `${i}`);
        newRow.appendChild(newHeader);
    }
    newTable.append(newRow);
    for (var i = 1; i <= 3; i++){
        newRow = document.createElement("tr");
        for (var j = 1; j <= 4; j++){
            var newBody = document.createElement("td");
            newBody.textContent = `${i}, ${j}`;
            newBody.setAttribute("id", `${i}${j}`);
            newRow.appendChild(newBody);
        }
        newTable.appendChild(newRow)
    }
    document.body.appendChild(newTable);

    var width = document.getElementsByTagName("th")[0].offsetWidth;
    var thArray = Array.from(document.getElementsByTagName("th"));
    thArray.forEach(x => {
        x.style.borderStyle = "double";
        x.style.width = `${width * 130/100}px`;
        x.style.textAlign = "center";
    });
    var tdArray = Array.from(document.getElementsByTagName("td"));
    tdArray.forEach(x => {
        if (x.getAttribute("id") == "11"){
            x.style.borderStyle = "solid";
        }else {x.style.borderStyle = "double";}
        x.style.textAlign = "center"; 
    });
    var elementOfInterest = document.getElementById("11");//
    var newDiv = document.createElement("div");
    var someoObj = ["up", "down", "left", "right", "Mark Cell"];
     for (var e of someoObj){
        var newButton = document.createElement("button");
        newButton.textContent = e;
        newButton.addEventListener("click", function(button){   //first time through, this function will run, returning a function that
            return function(){                                  //populated the button variable with newButton. It will save as local variable via closure 
                buttonClicked(button);       //elementOfInterest is the same for all buttons, so we don't have to care about closure
            }
        }(newButton));
        if (e == "Mark Cell"){
            newButton.style.width = "80px";
        }else{
            newButton.style.width = "50px";
            newButton.style.marginRight = "10px";
        }
        newDiv.appendChild(newButton);
    }
    document.body.appendChild(newDiv);
    document.getElementsByTagName("div")[0].style.marginTop = "10px";
    return elementOfInterest;
}
// get the directional buttons working
// for the permenant mark, are we utilizing closure??? I guess not
var startElement = createElements();
function setNextElement(value){
    startElement = value;
}
//var aFunc = someFunc();
//all td elements have id that have two characters long in the 
//form of "ij" where i is the row and j is the column
function buttonClicked(button){//, currChild){
    currChild = startElement
    if (button.textContent == "up"){
        if (currChild.getAttribute("id").charAt(0) !== '1'){
            var nextChild = currChild.parentNode.previousElementSibling.firstElementChild;  //throwaway child
            var str = "" + nextChild.getAttribute("id").charAt(0)  + currChild.getAttribute("id").charAt(1);
            nextChild = document.getElementById(str);
            moveCursor(nextChild, currChild)
        }
    }else if (button.textContent == "down"){
        if (currChild.getAttribute("id").charAt(0) != '3'){
            var nextChild = currChild.parentNode.nextElementSibling.firstElementChild;  //throwaway child
            var str = "" + nextChild.getAttribute("id").charAt(0)  + currChild.getAttribute("id").charAt(1);
            nextChild = document.getElementById(str);
            moveCursor(nextChild, currChild)
        }
    }else if (button.textContent == "right"){
        if (currChild.getAttribute("id").charAt(1) != '4'){
            var nextChild = currChild.nextElementSibling;  //throwaway child
            var str = "" + currChild.getAttribute("id").charAt(0)  + nextChild.getAttribute("id").charAt(1);
            nextChild = document.getElementById(str);
            moveCursor(nextChild, currChild)
        }
    }else if (button.textContent == "left"){
        if (currChild.getAttribute("id").charAt(1) != '1'){
            var nextChild = currChild.previousElementSibling;  //throwaway child
            var str = "" + currChild.getAttribute("id").charAt(0)  + nextChild.getAttribute("id").charAt(1);
            nextChild = document.getElementById(str);
            moveCursor(nextChild, currChild)
        }
    }else if (button.textContent == "Mark Cell"){
        if (currChild.style.backgroundColor != 'yellow'){
            currChild.style.backgroundColor = "yellow";
        }
    }
}

function moveCursor(nextChild, currChild){
    boldsArray(nextChild);
    unboldsArray(currChild);
    setNextElement(nextChild);
}
function unboldsArray(arrayElement){
    arrayElement.style.borderStyle = "double";
}
function boldsArray(arrayElement){
    arrayElement.style.borderStyle = "solid";
}
