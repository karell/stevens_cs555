export type GEDCOMLevel = 0 | 1 | 2;
export type GEDCOMTag =
  'INDI' | // individual
  'NAME' | // String with surname del by '/'s
  'SEX' | // M or F
  'BIRT' | // none
  'DEAT' | // none
  'FAMC' | // FAM_ID
  'FAMS' | // FAM_ID
  'FAM' | // FAM_ID
  'MARR' | // none
  'HUSB' | // IND_ID
  'WIFE' | // IND_ID
  'CHIL' | // IND_ID
  'DIV' | // none 
  'DATE' | // day month year 
  'HEAD' | // none
  'TRLR' | // none
  'NOTE'; // any string

export const VALID_TAGS = [
  'INDI',
  'NAME',
  'SEX',
  'BIRT',
  'DEAT',
  'FAMC',
  'FAMS',
  'FAM',
  'MARR',
  'HUSB',
  'WIFE',
  'CHIL',
  'DIV',
  'DATE',
  'HEAD',
  'TRLR',
  'NOTE'
];

export const VALID_LEVEL_ZERO_TAGS = [
  'NOTE',
  'TRLR',
  'HEAD',
  'FAM',
  'INDI'
];

export const VALID_MONTHS = [
  'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'
];

export namespace GEDCOMConstants {
  export const TAGS = {
    'INDI': 'INDI',
    'NAME': 'NAME',
    'SEX': 'SEX',
    'BIRT': 'BIRT',
    'DEAT': 'DEAT',
    'FAMC': 'FAMC',
    'FAMS': 'FAMS',
    'FAM': 'FAM',
    'MARR': 'MARR',
    'HUSB': 'HUSB',
    'WIFE': 'WIFE',
    'CHIL': 'CHIL',
    'DIV': 'DIV',
    'DATE': 'DATE',
    'HEAD': 'HEAD',
    'TRLR': 'TRLR',
    'NOTE': 'NOTE'
  }

  export const LEVELS = {
    '0': 0,
    '1': 1,
    '2': 2
  }
}
