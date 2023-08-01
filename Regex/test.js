let pattern = new RegExp("Hello World", "g");
let text = pattern.toString();
// console.log(/(\w+)=\1/.test('rat=rat'))
// console.log(/work(shop)?/.test('work and workshop'))
// console.log(pattern.exec(text))
// console.log(text)
// console.log(text.match(pattern))


// I work at a computer
// workshop.
// Is cat=bat or rat-rat?
// SI. cat eats rat.
// Is cat=bat or rat=rat?
// I work at a computer
// workshop.
// abbe, abe
// israel.34@gma4ilcom
// htn
// hbn
// hbtn
// hbbtn
// hbtttn
// hbttttn
// hbtttttn
// hbn
// hbon
// hbtn
// hbttn
// hbtttn
// hbttttn
// h8n
// 4155049898
// I realLy hOpe VancouvEr posseSs Yummy Soft vAnilla Dupper Mint Ice Nutella cream
const result = "I realLy hOpe VancouvEr posseSs Yummy Soft vAnilla Dupper Mint Ice Nutella cream".match(/[A-Z]+/g)
console.log(result.join(''))


const from = "Feb 1 11:00:00 ip-10-0-0-11 mdr: 2016-02-01 11:00:00 Receive SMS [SMSC:SYBASE1] [SVC:] [ACT:] [BINF:] [FID:] [from:Google] [to:+16474951758] [flags:-1:0:-1:0:-1] [msg:127:This planet has - or rather had - a problem, which was this: most of the people on it were unhappy for pretty much of the time.] [udh:0:]".match(/from:\s*(\w+)/)
const to = "Feb 1 11:00:00 ip-10-0-0-11 mdr: 2016-02-01 11:00:00 Receive SMS [SMSC:SYBASE1] [SVC:] [ACT:] [BINF:] [FID:] [from:Google] [to:+16474951758] [flags:-1:0:-1:0:-1] [msg:127:This planet has - or rather had - a problem, which was this: most of the people on it were unhappy for pretty much of the time.] [udh:0:]".match(/to:\s*([+]\d+)/)
const flags = "Feb 1 11:00:00 ip-10-0-0-11 mdr: 2016-02-01 11:00:00 Receive SMS [SMSC:SYBASE1] [SVC:] [ACT:] [BINF:] [FID:] [from:Google] [to:+16474951758] [flags:-1:0:-1:0:-1] [msg:127:This planet has - or rather had - a problem, which was this: most of the people on it were unhappy for pretty much of the time.] [udh:0:]".match(/\[flags:(.*?)\]/)
console.log([from[1], to[1], flags[1]].join(','))
// console.log( to)
// console.log( flags)

https://tldp.org/LDP/abs/html/