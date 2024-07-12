import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int v = sc.nextInt();

        int ccnt = 1;

        v-=a;
        if(v > 0){
            if((v) % (a-b) != 0){
                ccnt += ((v) / (a-b) + 1);
            }
            else ccnt += ((v) / (a-b));
        }
        System.out.println(ccnt);
    }
}
