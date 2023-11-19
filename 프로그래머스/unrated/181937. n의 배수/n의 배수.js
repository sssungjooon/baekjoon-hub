function solution(num, n) {
    var result = 0
    if (num%n == 0) {
        result = 1
    } else {
        result = 0
    }
    return result;
}