import * as fs from 'fs';
import * as path from 'path';
import * as readline from 'readline';
import { GEDCOMLine } from './GEDCOM-line';

//let _inputGEDCOM = 'proj02test.ged'; // not allowed to hardcode. for testing only
let _inputGEDCOM = '';
let _output: string = '';

process.argv.forEach(function (val, index, array) {
  if (index === 2) {
    _inputGEDCOM = val; // argument of running program must be file
  }
});
if (_inputGEDCOM && _inputGEDCOM !== '') {
  main();
}

function main() {
  let _lineReader = readline.createInterface({
    input: fs.createReadStream(_inputGEDCOM).on('error', (error) => {
      console.log('Error reading: ', error.code);
    })
  });
  _lineReader.on('line', (line: string) => {
    let processedLine: GEDCOMLine = new GEDCOMLine(line);
    let temp = "--> " + processedLine.originalLine + '\n';
    console.log(temp); // as per project guideline (last paragraph)
    _output += temp;
    let valid: string = processedLine.isValid() ? 'Y' : 'N';
    temp = "<-- " + processedLine.level + '|' + processedLine.tag + '|' + valid + '|' + processedLine.argument + '\n';
    console.log(temp); // as per project guideline (last paragraph)
    _output += temp;
  });
  _lineReader.on('close', () => {
    fs.writeFileSync(path.join(__dirname, 'output.txt'), _output);
  });
}

