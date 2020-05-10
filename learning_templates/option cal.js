cal_revenue = (amount, points, price_per_lot = 20000, months) => {
  let sum = 0
  for (let i=0 ; i<months ; i++) {
    let lots = parseInt(amount / price_per_lot);
    let profit_per_week = points * 20 * lots;
    let profit_per_month = profit_per_week * 4;
    let date = new Date()
    console.log((date.getMonth()+i)+"-"+date.getFullYear()+" \t\t"+amount
    +" \t\t"+profit_per_week+" \t\t"+profit_per_month+" \t\t"+(amount+profit_per_month))
    amount += profit_per_month
    sum += profit_per_month
  }
  return sum
};

let sum = cal_revenue(60000,10,8000,12)

console.log(sum)