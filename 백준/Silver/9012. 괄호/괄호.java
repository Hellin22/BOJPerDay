import java.util.Arrays;
import java.util.Scanner;
import java.util.Stack;

public class Main {
    // 배운점
    // 1. sc.nextLine 외에는 개행문자를 처리하지 않는다.
    //    따라서 sc.nextInt를 한 후에 새로운 것을 받아올때는
    //    sc.nextLine으로 개행문자를 처리해주고 받아와야한다.
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();
        sc.nextLine();
        while (t-- > 0) {
            String str = sc.nextLine();
            Stack<Integer> stck = new Stack<Integer>();
            boolean flag = true;
            for(int i = 0; i < str.length(); i++) {
                if(str.charAt(i) == '(') {
                    stck.push(1);
                }
                else if(str.charAt(i) == ')') {
                    if(stck.empty()) {
                        flag = false;
                        break;
                    }
                    else{
                        stck.pop();
                    }
                }
            }
            if(!stck.empty()) flag = false;

            if(flag) System.out.println("YES");
            else System.out.println("NO");

        }
    }
}
