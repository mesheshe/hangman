const SCRIPTS = require("./code/scripts");
 /*
console.log("Lets make sure JavaScript is working.");
var name = "Elias"; //Replace this with your first name
console.log("The unicode characters of your name are:")
for (var i = 0; i < name.length; i++){
	console.log(name.charCodeAt(i));
}
console.log("Copy and paste these values for activity credit.")

console.log(square(3)); // 9    works

function square(x){
	return x**2;
}

console.log(square(4));  // 16  works 
console.log(squares(3))  //     breaks code 

var squares = function(x){
	return x*x;	
}

console.log(squares(3))  // 9   works if broken code is taken out

function range(start, end, step = 1){
  let arr =  [];
  if (start <= end){
    for (let i = start; i <= end; i = i + step){
      arr.push(i);
    }
  }else{
    for (let i = start; i >= end; i = i + step){
      arr.push(i);
    }
  }
  return arr;
}
function sum(arr){
  let result = 0;
  for (let num of arr){
    result += num;
  }
  return result;
}
console.log(range(1,10));
console.log(range(5,2,-1));
console.log(sum(range(1,10)));
function reverseArray(arr){
  let newArr = [];
  for (let ele of arr){
    newArr.unshift(ele);
  }
  return newArr
}
function reverseArrayInPlace(arr){
  for(let i = 0; i < arr.length/2; i++){
    let temp = arr[i];
    arr[i] = arr[arr.length - 1 - i];
    arr[arr.length - 1 - i] = temp;
  }
}
console.log(reverseArray(["A", "B", "C"]));
let arrayValue = [1,2,3,4,5]
reverseArrayInPlace(arrayValue);
console.log(arrayValue)
*/
function arrayToList(arr){
	let returnList = {};
	function helper(arr, pos, alist){
		if (pos === arr.length - 1){
			alist.value = arr[pos];
			alist.rest = null;
			return 
	  	}
	  	alist.value = arr[pos];
		alist.rest = {};
		return helper(arr, ++pos, alist.rest)
	}
	helper(arr, 0 , returnList);
	return returnList;
}
let a =  arrayToList([1,2,3,4]);
console.log(JSON.stringify(a));
console.log(listToArray(a));
console.log(prepend(10, prepend(20, null)));
console.log(nth(arrayToList([10, 20, 30]), 1));
function listToArray(a){
	let retArray = [];
	while (a !== null){
		retArray.push(a.value);
		a = a.rest;
	}
	return retArray
}
function prepend(val, list){
	newList = {};
	newList.value = val;
	newList.rest = list;
	return newList;
}
function nth(list,query, pos = 0){
	if (list == null) return undefined;
	if (query === pos) return list.value;
	return nth(list.rest,query, ++pos)
}


function deepEqual(val1,val2){
	function size(object){
		let count  = 0;
		for (i in object){
			count++;
		}
		return count;
	}
	function deepEqualHelper(val1,val2){
		if (size(val1) != size(val2)) return false
		for (i in val1){
			if (typeof(val1[i]) == typeof(val2[i]) && typeof(val1[i]) == "object" && val1[i] !== null){
				if (!deepEqualHelper(val1[i], val2[i])) return false
			}else{
				if (val1[i] !== val2[i]) return false
			}
		}
		return true;
	}
	return deepEqualHelper(val1, val2)
}
let obj = {here:{is:"an"},object:2};
console.log();
//console.log(deepEqual(obj,obj));
//console.log(deepEqual(obj,{here:1, object: 2}));
//console.log(deepEqual(obj,{here:{is:"an"},object: 2}));

function repeat(n, action) {
	for (let i = 0; i < n; i++) {
	  action(i);
	}
}


//repeat(4, console.log);
let arr1 = [], arr2 = [];
function doSomething(i){
	arr1.push(`Units ${i+1}`)
}
repeat(4, doSomething);
console.log(arr1)

repeat(4, i => arr2.push(`Units ${i+1}`))
console.log(arr2)

function greaterThan(n){
	return m => m > n;
}
let gT10 = greaterThan(10)
console.log(gT10(11));

function noisy(f){
	return (...args) => {
		console.log("called with", args);
		let result = f(...args);
		console.log("called with", args, ", returned", result);
		return result
	}
}
noisy(Math.min)(3,2,1);

function unless(test, then){
	if (!test) then();
}
repeat(3, n => {unless(n % 2 == 1, () => console.log(n, "is even"));});

["A", "B"].forEach(l => console.log(l));

function filter(array, test){
	let passed = [];
	for (let e of array){
		if (test(e)){
			passed.push(e);
		}
	}
	return passed
}

//console.log(filter(SCRIPTS, script => script.living));
//console.log(SCRIPTS.filter(s=> s.direction == "ttb"));
function map(array, transform){
	let mapped = [];
	for (let e of array){
		mapped.push(transform(e));
	}
	return mapped;
}
let rtlScripts = SCRIPTS.filter(s => s.direction == "rtl");
console.log(map(rtlScripts, i => i.name));

function reduce(array, combine, start){
	let current = start;
	for (let element of array){
		current = combine(current, element);
	}
	return current;
}
console.log(reduce([1, 2, 3, 4], (a, b) => a + b, 0));     
console.log([1,2,3,4].reduce((a, b) => a + b**2));
function characterCount(script){                         //here count acts like current and gets assigned 0. 
	return script.ranges.reduce((count, [from, to])=> {return count + (to - from);}, 0);
} //only two numbers in range, assigned from to the first one and to to the second one totals all the ranges for a specific language
 //notice how start is not specified so reduce starts at first element in list. So it grabs the first element and the second element, checks the character
// length by using characterCount() and keeps the larger one.
let biggest  = null;
console.log(SCRIPTS.reduce((a, b) => {return characterCount(a) < characterCount(b) ? b: a;}));                                                      
for (let script of SCRIPTS){
	if (biggest == null || characterCount(biggest) < characterCount(script)){
		biggest = script;
	}
}
console.log(biggest);
function average(array){
	return array.reduce((a, b) => a + b) / array.length;
}
//average(of an array that has only the living languages)
console.log(Math.round(average(SCRIPTS.filter(s=>s.living).map(s=>s.year))));
//average(of an array that has only the dead languages)
console.log(Math.round(average(SCRIPTS.filter(s=>!s.living).map(s=>s.year))));

let total = 0, count = 0;
for (let script of SCRIPTS){
	if (script.living){
		total += script.year;
		count += 1;
	}
}
console.log(Math.round(total/count));

function characterScript(code){
	for (let script of SCRIPTS){             //line below just states if code is inside the range, return script 
		if (script.ranges.some(([from, to])=> {return code >= from && code < to;})){
			return script;
		}
	}
	return null;
}
console.log(characterScript(121));

let horseShoe = "🐴👟";
console.log(horseShoe.length)
console.log(horseShoe[0]);
console.log(horseShoe.charCodeAt(0));
console.log(horseShoe.codePointAt(0));

let roseDragon = "🌹🐉";
for (let char of roseDragon){
	console.log(char);
}
function countBy(items, groupName){
	let counts = [];
	for (let item of items){
		let name = groupName(item);
		let known = counts.findIndex(c => c.name == name);
		if (known == -1){
			counts.push({name, count: 1});
		}else{
			counts[known].count++;
		}
	}
	return counts;
}
console.log(countBy([1,2,3,4,5], n => n > 2));

function textScripts(text) {
	let scripts = countBy(text, char => {
	  let script = characterScript(char.codePointAt(0));
	  return script ? script.name : "none";  // if script == -1, return "none" otherwise return script
	}).filter(({name}) => name != "none");
  
	let total = scripts.reduce((n, {count}) => n + count, 0);
	if (total == 0) return "No scripts found";
  
	return scripts.map(({name, count}) => {
	  return `${Math.round(count * 100 / total)}% ${name}`;
	}).join(", ");
}
  
console.log(textScripts('英国的狗说"woof", 俄罗斯的狗说"тяв"'));

let arrays = [[1, 2, 3], [4, 5], [6]];
console.log(arrays.reduce((a, b) => a.concat(b)));
function loop(val, test, updateFunc, bodyFunc){
	let count = 0;
	while (count != 5){
	if (!test(val)) return;
	bodyFunc(val) 
	val = updateFunc(val);  
	count++;
	}
}

loop(3, n => n > 0, n => n - 1, console.log);

function every(array, test) {
	for (let ele of array){
		if (!test(ele)) return false
	}
	return true
}
function every1(array, test) {
	if (!(array.some(n => test(n)))) return false
	return true 
}
/*
class Vec{
	constructor(x, y){
		this.x = x;
		this.y = y;
	}
	plus(vec){
		this.x += vec.x;
		this.y += vec.y;
      	return {x:this.x, y:this.y};
	}
	minus(vec){
		this.x -= vec.x;
		this.y -= vec.y;
      	return {x:this.x, y:this.y};
	}
	get length(){
		return Math.sqrt((this.x**2 + this.y**2));
	}
}



console.log(new Vec(1, 2).plus(new Vec(2, 3)));
console.log(new Vec(1, 2).minus(new Vec(2, 3)));
console.log(new Vec(3, 4).length);
class Group{
	constructor(){
		this.group = {};
	}
	add(){
		this.group.add(value);
	}
	delete(value){
		this.group.delete(value);
	}
	has(value){
		for (let e of this.group){
			if (e === value) return true;
		}
		return false;
	}
	static from(obj){
		for (let e of obj){
			this.group.add(e);
		}
	}
}
let group = Group.from([10, 20]);
console.log(group.has(10));
// → true
console.log(group.has(30));
// → false
group.add(10);
group.delete(10);
console.log(group.has(10));
*/