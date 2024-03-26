function solution(price, money, count) {
    var answer = 0;
    let spend = 0;
    for (let i = 1; i < count+1; i++) {
        spend += i * price;
    }
    if (spend > money) {
        answer = spend-money
    } else {
        answer = 0; 
    }
    return answer;
}