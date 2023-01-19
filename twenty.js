function solution(hp) {
    var answer = 0;
    let a=5; let b=3; let c=1;
//     for(let i=0;i<hp;i++)
//         {
//             if(hp/a!=0)
//                 {
                    
//                 }
//         }
//    answer=hp/a+(hp%a/b)+hp%a%b/c;
    
     answer=Math.floor(hp/a)+Math.floor(hp%a/b)+Math.floor(hp%a%b/c);
    return answer;
}