import { GEDCOMLevel, GEDCOMTag, GEDCOMConstants, VALID_TAGS, VALID_LEVEL_ZERO_TAGS } from './GEDCOM-constants';

export class GEDCOMLine {
  errors: Array<string> = [];
  originalLine: string;

  level: GEDCOMLevel;
  tag: GEDCOMTag;
  argument: string;

  constructor(inputLine: string) {
    this.originalLine = inputLine;
    this.parseInputLine(inputLine);
  }

  isValid(): boolean {
    return this.errors.length < 1;
  }

  isValidTag(): boolean {
    return VALID_TAGS.indexOf(this.tag) > -1;
  }

  parseInputLine(line: string) {
    let tokens: Array<string> = line.split(' ');
    if (tokens.length < 2) {
      this.errors.push('Invalid line. Minimum of 2 line arguments');
    }
    this.level = <GEDCOMLevel>Number(tokens[0]);
    if (isNaN(this.level) || [0, 1, 2].indexOf(this.level) === -1) {
      this.errors.push('First argument must be a level 0, 1 or 2');
    }

    switch (this.level) {
      case 0:
        if (
          tokens.length >= 3 &&
          (tokens[2].toUpperCase() === GEDCOMConstants.TAGS.INDI ||
            tokens[2].toUpperCase() === GEDCOMConstants.TAGS.FAM)
        ) {
          // FAM OR INDV
          this.tag = <GEDCOMTag>tokens[2].toUpperCase();
          this.argument = tokens[1];
        } else {
          this.tag = <GEDCOMTag>tokens[1].toUpperCase();
          this.argument = line.substr(line.indexOf(this.tag) + this.tag.length + 1);
          if (
            this.tag !== GEDCOMConstants.TAGS.NOTE &&
            this.tag !== GEDCOMConstants.TAGS.HEAD &&
            this.tag !== GEDCOMConstants.TAGS.TRLR
          ) {
            this.errors.push('Invalid top level line');
          }
        }
        break;
      case 1:
      case 2:
        this.tag = <GEDCOMTag>tokens[1].toUpperCase();
        this.argument = line.substr(line.indexOf(this.tag) + this.tag.length + 1);
        break;
      default:
        this.tag = <GEDCOMTag>tokens[1].toUpperCase();
        this.argument = line.substr(line.indexOf(this.tag) + this.tag.length + 1);
        break;
    }
    if (!this.isValidTag()) {
      this.errors.push('Invalid tag type: ' + this.tag);
    }
    if (VALID_LEVEL_ZERO_TAGS.indexOf(this.tag) > -1 && this.level !== 0) {
      this.errors.push('Invalid tag should be level 0');
    }
    if (VALID_LEVEL_ZERO_TAGS.indexOf(this.tag) === -1 && this.level === 0) {
      this.errors.push('Invalid level 0 tag');
    }
    if (this.tag === GEDCOMConstants.TAGS.DATE && this.level === GEDCOMConstants.LEVELS['1']) {
      this.errors.push('DATE is not a valid level 1 tag');
    }
    if (this.tag !== GEDCOMConstants.TAGS.DATE && this.level === GEDCOMConstants.LEVELS['2']) {
      this.errors.push('NAME is not a valid level 2 tag');
    }
  }
}