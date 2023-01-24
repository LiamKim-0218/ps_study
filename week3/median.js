function solution(array) {
    var answer = 0;
    let MAX=0;
    let mid=0;
    let min=0;
//     for(let i=0;i<array.length;i++)
//         {
//             for(let j=9;j<i;j++)
//                 {
//                     if(array[j]>array[j+1])
//                         {
                            
//                         }
//                 }
//              for(let j=0;j<i;j++)
//                  {
//                      if(array[i]<array[j+1])
//                          {
//                              array[j+1]=array[i]
//                          }
                        
                        
//                  }
//         }
    
    
    // let mid=0;
     let k=0;
     array.sort(function(a,b)
         {
             return a-b;
         });
 console.log(array);
     mid=Math.floor(array.length/2);
     if(array.length%2===1)
         {
             answer=array[mid];    
         }
     else{
         answer=(array[mid]+array[mid-1])/2;
         //answer=k/2;
      }
    return answer;
}