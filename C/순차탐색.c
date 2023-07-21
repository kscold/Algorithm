#include <stdio.h>

int main(void){
    int key, i;
    
    int list[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    
    
    
    printf("탐색할 값을 입력하시오 : ");
    
    scanf("%d", &key);
    
    
    
    for(i = 0; i < 9; i++){
        
        if(list[i] == key)
            
        {
            
            printf("찾은 값 = %d\n", list[i]);
            
            printf("탐색 인덱스 = %d\n", i);
            
            return 1; // 이걸 넣으면 반복문이 종료되나 봐
            
        }
        
    }
    
    printf("주어진 값 %d를 찾지 못했습니다.\n", i);
    
    
    return 0;
}
