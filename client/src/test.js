const json = require('./test.json')

const unitForMonth = json.unitForMonth
const unitForWeek = json.unitForWeek
const unixMapUnitForToday = json.unixMapUnitForToday
const unixMapUnitForYesterday = json.unixMapUnitForYesterday
// 获取keys
const getKeys = obj => (Object.keys(obj))

function format2Month (unitList) {
  let list = Array.isArray(unitList) ? unitList : [{data: unitList}]
  let format = {}
  let format2 = {}
  let other = {}

  unitList.forEach(month => getKeys(month.data).forEach(e => {
    format[e] = {}
    if (e === '其他') getKeys(month.data[e]).forEach(j => other[j] = 0)
    if (e !== '其他') getKeys(month.data[e]).forEach(j => format2[j] = 0)
  }))

  let keys1 = Object.keys(format)
  let keys2 = Object.keys(format2)
  let otherKey = Object.keys(other)

  unitList.forEach(month => {
    keys1.forEach(i => {
      if (i !== '其他') {
        keys2.forEach(j => {
          format[i][j] = 0
          if (format[i][j] >= 0) format[i][j] += month.data[i] && month.data[i][j] ? month.data[i][j] : 0
        })
        return
      }
      otherKey.forEach(j => {
        format[i][j] = 0
        if (format[i][j] >= 0) format[i][j] += month.data[i] && month.data[i][j] ? month.data[i][j] : 0
      })
      return
    })
  })
  console.log(format)
}

format2Month(unitForMonth)
format2Month(unitForWeek)
format2Month([{data: unixMapUnitForToday}])
format2Month([{data: unixMapUnitForYesterday}])
