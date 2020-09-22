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
