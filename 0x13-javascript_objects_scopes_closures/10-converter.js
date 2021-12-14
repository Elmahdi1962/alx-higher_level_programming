#!/usr/bin/node
exports.converter = function (base) {
  return function (num) {
    num.toString(base);
  };
};
