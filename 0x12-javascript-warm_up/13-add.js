#!/usr/bin/node
exports.add = function (a, b) {
  if (a && b) {
    return (a + b);
  }
  return NaN;
};
