#!/usr/bin/node
const fs = require('fs');

function concatFiles(file1, file2, destination) {
    try {
        // Read content of first file
        const content1 = fs.readFileSync(file1, 'utf8');
        // Read content of second file
        const content2 = fs.readFileSync(file2, 'utf8');
        // Concatenate contents
        const concatenatedContent = `${content1}${content2}`;
        // Write concatenated content to destination file
        fs.writeFileSync(destination, concatenatedContent);
        console.log(`Concatenation successful. Output written to ${destination}`);
    } catch (error) {
        console.error('An error occurred:', error.message);
    }
}

const args = process.argv.slice(2);
if (args.length !== 3) {
    console.error('Usage: ./102-concat.js <file1> <file2> <destination>');
    process.exit(1);
}

const [file1, file2, destination] = args;
concatFiles(file1, file2, destination);
