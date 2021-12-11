const municipalitiesLookup = { '01': 12, '02': 13, '03': 16, '04': 33, '05': 22, '06': 19, '07': 16, '08': 22, '09': 9, '10': 13, '11': 23, '12': 20, '13': 26, '14': 18,
};

export function isForeignCode(code) {
  return code.startsWith('9');
}

export function isNationalCode(code) {
  if (!code.startsWith('0') && !code.startsWith('1')) return false;

  const department = code.substring(0, 2);
  const municipality = code.substring(2);
  return municipalitiesLookup[department] >= Number(municipality);
}

export function isMunicipalityCode(code) {
  return code.length === 4 && (isForeignCode(code) || isNationalCode(code));
}