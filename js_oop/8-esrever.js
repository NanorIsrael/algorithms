exports.esrever = function (list) {
	let reversedList = []
	for (let idx = 1; idx <= list.length; idx++) {
		reversedList.push(list[list.length - idx])
	}
	return reversedList;
}