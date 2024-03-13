#!/usr/bin/node

module.exports = class Rectangle {
    constructor (w, h) {
        if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
        }
    }
    }
    Rectangle.prototype.print = function () {
        let i;
        let j;
        let str = '';
        for (i = 0; i < this.width; i++) {
            str += 'X';
        }
        for (j = 0; j < this.height; j++) {
            console.log(str);
        }
    };
    Rectangle.prototype.rotate = function () {
        let temp = this.width;
        this.width = this.height;
        this.height = temp;
    };
    Rectangle.prototype.double = function () {
        this.width *= 2;
        this.height *= 2;
    };
    