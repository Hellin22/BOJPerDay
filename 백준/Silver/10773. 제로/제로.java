import java.util.Arrays;
import java.util.Scanner;
import java.util.Stack;

public class Main {
    // 배운점
    // 1. stack을 사용하지 않고 idx을 사용해도 풀 수 있는 문제
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int k = sc.nextInt();
        int[] arr = new int[k+1];
        int idx = 0;
        while (k-- > 0) {
            int input = sc.nextInt();
            if(input == 0) idx--;
            else{
                arr[idx] = input;
                idx++;
            }
        }

        int summ = 0;
        for(int i = 0; i < idx; i++){
            summ += arr[i];
        }
        System.out.println(summ);
    }
}
