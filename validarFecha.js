export function getFullYear(year) {
    return Number(year) >=
      Number(new Date().getFullYear().toString().substr(-2)) + 1
      ? '19'.concat(year)
      : '20'.concat(year);
  }
  
  export function isDate(str) {
    const year = getFullYear(str.substring(4));
    const month = str.substring(2, 4);
    const day = str.substring(0, 2);
    const date = new Date(`${year}/${month}/${day}`);
    return date && Number(date.getMonth()) + 1 === Number(month);
  }