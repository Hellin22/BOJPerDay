import java.util.Arrays;
import java.util.Scanner;
import java.util.Stack;

public class Main {
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
