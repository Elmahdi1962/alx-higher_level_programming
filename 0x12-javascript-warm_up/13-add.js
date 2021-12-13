#!/usr/bin/node
exports.add = add;
function add (a, b) {
  if (a && b) {
    return (a + b);
  }
  return NaN;
}
