export function groupBy(array, key) {
  return array.reduce((result, current) => {
    const group = current[key];
    if (!result[group]) result[group] = [];
    result[group].push(current);
    return result;
  }, {});
}
