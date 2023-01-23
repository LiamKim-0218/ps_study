function solution(my_string) {
    var answer = 0;
    for(let i=0; i<my_string.length;i++)
        {
            if(Number(my_string[i])===true)
           // if(Number(my_string[i]>=0 && Number(my_string[i]<=9)))//
                //문자열을 숫자로
                {
                    answer+=Number(my_string[i]);
                
                    //answer+=Number(my_string[i]);
                }
        }
    return answer;
}
