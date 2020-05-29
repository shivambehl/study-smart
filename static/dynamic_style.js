// auto expand text area
//-------------------------------------------------------------------------------------------------------

var autoExpand = function (field) {

	// Reset field height
	field.style.height = 'inherit';

	// Get the computed styles for the element
	var computed = window.getComputedStyle(field);

	// Calculate the height
	var height = parseInt(computed.getPropertyValue('border-top-width'), 10)
	             + parseInt(computed.getPropertyValue('padding-top'), 10)
	             + field.scrollHeight
	             + parseInt(computed.getPropertyValue('padding-bottom'), 10)
	             + parseInt(computed.getPropertyValue('border-bottom-width'), 10);

	field.style.height = height + 'px';

};

document.addEventListener('input', function (event) {
	if (event.target.tagName.toLowerCase() !== 'textarea') return;
	autoExpand(event.target);
}, false);

//------------------------------------------------------------------------------------------------------

// Quiz
//------------------------------------------------------------------------------------------------------

function showQuestions() {
  var x = document.getElementById("myDIV");

      if (window.getComputedStyle(x).display === "none") {
        x.style.display = "block";
      } else {
        x.style.display = "none";
      }
}



score = 0;

function rightans() {
    score = score + 10;
    alert("Right answer !!!");
}

function wrongans(){
    score = score - 2;
    alert("Sorry, Wrong Answer !\nPlease Try again." + score);
}

function printScore() {
    alert("You have scored " + score + " Points\nKeep It up!");
    location.reload()
}
//------------------------------------------------------------------------------------------------------