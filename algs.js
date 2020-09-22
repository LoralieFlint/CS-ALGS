// Print out each element of the following array ?// on a separate line:
// Print out each element of the following array
// ['Joe', 2, 'Ted', 4.98, 14, 'Sam', 'void *', '42', 'float', 'pointers', 5006]
// Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.
const list = [
  "Joe",
  2,
  "Ted",
  4.98,
  14,
  "Sam",
  "void *",
  "42",
  "float",
  "pointers",
  5006,
];
for (let i = 0; i < list.length; i++) {
  console.log(list[i]);
  // return list[i]
}

// Return Something to Me!
// Write a function that returns the string "something" joined with a space " " and the given argument a.
function giveMeSomething(a) {
  return "something " + a;
}

// Profitable Gamble
// Create a function that takes three arguments prob, prize, pay and returns true if prob * prize > pay; otherwise return false.
function profitableGamble(prob, prize, pay) {
	if (prob * prize > pay) {
		return true
	} else {
		return false
	}
}

// Return the First Element in an Array
// Create a function that takes an array and returns the first element.
function getFirstValue(arr) {
	return arr[0]
}

// Football Points
// Create a function that takes the number of wins, draws and losses and calculates the number of points a football team has obtained so far.
// wins get 3 points
// draws get 1 point
// losses get 0 points
function footballPoints(wins, draws, losses) {
	return ((wins * 3) + (draws*1))
}

