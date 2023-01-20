function solution(num, k) {
    var answer = 0;
    let a=String(num);
    let b=String(k);
   // let c = Praseint(b);
    //console.log(a);
    for(let i=0;i<a.length;i++)
        {
            console.log(k);
            if(a[i] === b)
                {
                    answer = i+1;
                    break;
                    
                }
            else
                answer= -1;
        }
    return answer;
}