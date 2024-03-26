function solution(s) {
  const answer = [];
  const map = new Map();

  [...s].map((v, i) => {
    if (!map.has(v)) answer.push(-1);
    else answer.push(i - map.get(v));
    map.set(v, i);
  });

  return answer;
}