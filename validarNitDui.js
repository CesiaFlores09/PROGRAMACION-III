import { isMunicipalityCode } from './validarMunicipalidad.js';
import { isDate } from './validarFecha.js';

export const duiRegExp = /(^\d{8})-(\d$)/;
export const nitRegExp = /((^\d{4})-(\d{6})-(\d{3})-(\d$))|(^\d{14}$)/;
export const carPlateRegExp = /^(O|N|CD|CC|P|A|C|V|PR|T|RE|AB|MI|MB|F|M|D|PNC|E)\d{1,6}$/i;

export function isDUI(str) {
  if (!duiRegExp.test(str)) return false;

  let sum = 0;
  const [digits, verifier] = str.split('-');
  for (let i = 0; i < digits.length; i++) {
    sum += Number(digits[i]) * (digits.length + 1 - i);
  }

  return Number(verifier) === (10 - (sum % 10)) % 10 && sum > 0;
}

function calculateNitVerificationOldFormat(digits) {
    let sum = 0;
    for (let i = 0; i < digits.length; i++) {
      sum += Number(digits[i]) * (digits.length + 1 - i);
    }
    sum %= 11;
    return sum;
  }
  
  function calculateNitVerification(digits) {
    let sum = 0;
    for (let i = 0; i < digits.length; i++) {
      sum +=
        Number(digits[i]) * (3 + 6 * Math.floor(Math.abs((i + 5) / 6)) - (i + 1));
    }
    sum %= 11;
    return sum > 1 ? 11 - sum : 0;
  }
  
  function splitNIT(str) {
    const municipality = str.substring(0, 4);
    const birthdate = str.substring(4, 10);
    const correlative = str.substring(10, 13);
    const verifier = str.substring(13);
    return [municipality, birthdate, correlative, verifier];
  }
  
  export function isNIT(str) {
    if (!nitRegExp.test(str)) return false;
  
    const [municipality, birthdate, correlative, verifier] = str.includes('-')
      ? str.split('-')
      : splitNIT(str);
    if (!isMunicipalityCode(municipality) || !isDate(birthdate)) return false;
  
    const digits = municipality + birthdate + correlative;
    const sum = correlative.startsWith('0')
      ? calculateNitVerificationOldFormat(digits)
      : calculateNitVerification(digits);
  
    return Number(verifier) === sum;
  }