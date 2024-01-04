export default function appendToEachArrayValue(array, appendString) {
	const newArray = [];
  
	for (let val of array) {
	  newArray.push(appendString + val);
	}
  
	return newArray;
  }