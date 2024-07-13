import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] arr = new int[3];

        while(true) {
            for (int i = 0; i < 3; i++) {
                arr[i] = sc.nextInt();
            }
            if(arr[0] == 0 && arr[1] == 0 && arr[2] == 0) break;
            else{
                // 1. 양의 정수 -> 0은 안나옴.
                Arrays.sort(arr);
                if(Math.pow(arr[2], 2) == (Math.pow(arr[1], 2) + Math.pow(arr[0], 2))) {
                    System.out.println("right");
                } else{
                    System.out.println("wrong");
                }
            }
        }
    }
}//9 000 000 00