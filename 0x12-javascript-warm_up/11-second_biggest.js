#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length <= 1) {
  console.log(0);
}
else {
  const arr = args.map(Number);
  const max = Math.max(...arr);
  arr.splice(arr.indexOf(max), 1);
  console.log(Math.max(...arr));
}
