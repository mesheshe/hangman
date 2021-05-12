// You are not permitted to change this in any way
function Student(name, major, yearInSchool, club) {
    this.name = name; // string, (e.g. "Jim", "Pam", "Michael")
    this.major = major; // string, (e.g. "Computer Science", "Art", "Business")
    this.yearInSchool = yearInSchool; // int, (e.g. 1, 2, 3, 4)
    this.club = club; // string, (e.g. "Improv", "Art")
}
  
var students = [
    new Student("Pam", "Art", 2, "Art"),
    new Student("Michael", "Business", 4, "Improv"),
    new Student("Dwight", "Horticulture", 1, "Karate"),
    new Student("Jim", "Sports Science", 2, "Guitar"),
    new Student("Angela", "Accounting", 4, "Cat"),
    new Student("Toby", "Human Resources", 3, "Photography")/*,
    new Student("Lizzy", "Example Job", 5, "Guitar")*/
];
  
  /* This function sorts arrays using an arbitrary comparator. You pass it a comparator 
  and an array of objects appropriate for that comparator and it will return a new array 
  which is sorted with the largest object in index 0 and the smallest in the last index*/
function sortArr(comparator, array) {
    // your code here
    returnArray = [array[0]];
    for (var i = 1; i < array.length; i++){
        var value = array[i];
        var pos = i - 1;   // line below does insertion. It checks if value > array[pos], since if it is, it gets placed earlier in the list 
        while(pos >= 0 && value.name === comparator(value, returnArray[pos]).name){
            returnArray[pos + 1] = returnArray[pos];
            pos--;
        }
        returnArray[pos + 1] = value
    }
    return returnArray;
}
  
  /* A comparator takes two arguments and uses some algorithm to compare them. If the first 
  argument is larger or greater than the 2nd it returns true, otherwise it returns false.
  Here is an example that works on integers*/
function exComparator( int1, int2){
    if (int1 > int2){
        return true;
    } else {
        return false;
    }
}
  
  /* For all comparators if students are 'tied' according to the comparison rules then the order of 
  those 'tied' students is not specified and either can come first*/
  
  /* This compares two students based on their year in school. Sort in descending order.*/
function yearComparator(student1, student2) {
    // your code here
    if (student1.yearInSchool > student2.yearInSchool){
        return student1;
    }else{
        return student2;
    }
}
  
  /* This compares two students based on their major. It should be case insensitive and 
  makes which are alphabetically earlier in the alphabet are "greater" than ones that 
  come later (from A-Z).*/
function majorComparator(student1, student2) {
    // your code here
    if (student1.major.toLowerCase() < student2.major.toLowerCase()){
        return student1;
    }else{
        return student2;
    }
}
  
  /* This compares two students based on the club they're in. The ordering from "greatest" 
  to "least" is as follows: improv, cat, art, guitar, (types not otherwise listed). 
  It should be case insensitive. If two clubs are of equal type then the student who
  has the higher year in school should be "greater."*/

  function clubAllowed(club){
    var order = ["improv", "cat", "art", "guitar"];
    for (var i = 0; i < order.length; i++){
        if (order[i] === club.toLowerCase()){
            return true;
        }
    }
    return false;
  }

function clubComparator(student1, student2) {
    // your code here
    var student1_index = -1;
    var student2_index = -1;
    var order = ["improv", "cat", "art", "guitar"]
    for (var i = 0; i < order.length; i++){
        if (student1.club.toLowerCase() === order[i]){
            student1_index = i;
        }
        if(student2.club.toLowerCase() === order[i]){
            student2_index = i;
        }
    }
    
    if (student1_index !== -1 && student2_index ===  -1){
        return student1;
    }else if (student2_index !== -1 && student1_index ===  -1){
        return student2;
    }else if (student1_index === -1 && student2_index ===  -1){
        return yearComparator(student1, student2);
    }
    // if both have valid clubs
    if (student1_index < student2_index){
        return student1;
    }else if (student1_index > student2_index){
        return student2;
    }else if (student1_index == student2_index){
        return yearComparator(student1, student2);
    }
    
}

Student.prototype.logMe = function(club = false){
    if (club === false){
        console.log(this.name + " - " + this.major + " - " + this.yearInSchool);
    }else{
        console.log(this.name + " - " + this.major + " - " + this.yearInSchool+ " - " + this.club);
    }
}

function realAnswer(){
    var yearIntroString = "The students sorted by year in school are:"
    var majorIntroString = "The students sorted by major are:"
    var clubIntroString = "The students sorted by club affiliation are:"
    printAnswerFormat(yearComparator, students, yearIntroString, false)
    printAnswerFormat(majorComparator, students, majorIntroString, false)
    printAnswerFormat(clubComparator, students, clubIntroString, true)
    console.log("**********") 
}  

function printAnswerFormat(comparator, array, introString, clubNeeded){

    console.log("**********" +'\n' + '\n' + introString) 
    var Array = sortArr(comparator, array);
    for (var e of Array){
        if (clubNeeded === true){
            e.logMe(clubAllowed(e.club))
        }else{
            e.logMe(clubNeeded);
        }
    }
    console.log();
}

realAnswer();
