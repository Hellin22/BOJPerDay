import java.util.Arrays;
import java.util.Scanner;

// 덩치 등수의 정의를 제대로 읽지않아서 문제
// 사람들 중 등수를 매기는게 아니라 나보다 덩치 큰사람 수+1이 덩치등수
// 어렵지 않은 문제

public class Main {
    public static class Pair{
        int x;
        int y;

        public Pair(int x, int y){
            this.x = x;
            this.y = y;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Pair[] arr = new Pair[n];

        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            arr[i] = new Pair(x, y);
        }
        int[] arr2 = new int[n];
        int[] arr3 = new int[51];
        int[] arr4 = new int[51];
        for (int i = 0; i < n; i++) {
            int summ = 1;
            for(int j = i-1; j >= 0; j--){
                if(arr[i].x < arr[j].x && arr[i].y < arr[j].y){
                    summ++;
                }
            }
            for (int j = i + 1; j < n; j++) {
                if(arr[i].x < arr[j].x  && arr[i].y < arr[j].y){
                    summ++;
                }
            }
            arr2[i] = summ;
//            arr3[summ]++;
        }
        for (int i = 0; i < n; i++) {
            System.out.print(arr2[i] + " ");
        }
//
//        int start = 1;
//        for(int i = 50; i >= 0; i--){
//            if(arr3[i] != 0){
//                arr4[i] = start;
//                start+=arr3[i];
//            }
//        }
//
//        for(int i = 0; i < arr2.length; i++){
//            System.out.print(arr4[arr2[i]] + " ");
//        }
    }
}
