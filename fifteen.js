function solution(numbers) {
    var answer = 0;
    for(let i=0; i<numbers.length; i++)
        {
            answer+=numbers[i];
        }
    answer=answer/numbers.length;
    console.log(answer);
    return answer;
}

let numbers=[10,20,30,40,50,60,70];
solution(numbers);
console.log('hello');