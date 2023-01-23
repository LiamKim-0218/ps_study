function solution(my_string, n) {
    var answer = '';
    // let array=my_string[0];
     for(let i=0;i<my_string.length;i++)
        {
            for(let j=0; j<n;j++)
                {
                    answer+=my_string[i];
                }
        }
    return answer;
}
