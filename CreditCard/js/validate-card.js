// Validate the card-number text input.


// From https://www.creditcardvalidator.org/developer
// It uses a closure [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures]
/*
	Locate card number text input element
	Locate the submit button element
	Set up a listener for the keyup event for the card-number element

	Algorithm for listener:
		-

*/

var LuhnCheck = (function()
{
	var luhnArr = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9];
	return function(str)
	{
		var counter = 0;
		var incNum;
		var odd = false;
		var temp = String(str).replace(/[^\d]/g, "");
		if ( temp.length == 0)
			return false;
		for (var i = temp.length-1; i >= 0; --i)
		{
			incNum = parseInt(temp.charAt(i), 10);
			counter += (odd = !odd)? incNum : luhnArr[incNum];
		}
		return (counter%10 == 0);
	}
})();

//alert(LuhnCheck('1234123412341238'));
const cardNumber = document.querySelector("input[name='card-number']");
const submitButton = document.querySelector("input[type=submit]");

const reg = /(^4[0-9]{12}(?:[0-9]{3})?$)|(^(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}$)|(3[47][0-9]{13})|(^3(?:0[0-5]|[68][0-9])[0-9]{11}$)|(^6(?:011|5[0-9]{2})[0-9]{12}$)|(^(?:2131|1800|35\d{3})\d{11}$)/;


function formatCC(e) {
	let value = cardNumber.value;
	if (value.test(reg)){
		if (LuhnCheck(value)){
			submitButton.disabled = false;
		}else{
			cardNumber.classList.add('invalid');
		}
		
	} 
}
document.addEventListener('keyup', formatCC);

