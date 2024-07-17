import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;

class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        double n = Double.parseDouble(br.readLine());

        // 1. 난이도의 범위가 1~30이므로 고정크기 배열로 cnt를 추가하는 방법
        // 2. treeset에는 중복 자료가 들어가지 않음....
        // 3. ArrayList에다가 몽땅 집어넣고 오름차순 정렬 -> 개수만큼 선택
        double a = Math.round(n * 15 / 100);

        ArrayList<Integer> list = new ArrayList<Integer>();
        // 3번 방법
        for(int i = 0; i < n; i++){
            list.add(Integer.parseInt(br.readLine()));
        }
        Collections.sort(list);

        // 앞에서 a 인원 뒤에서 a 인원 빼야함.
        double summ = 0.0;
        for(int i = (int)a; i < n-a; i++ ){
            summ+=list.get(i);
        }
        summ =Math.round(summ / (n-2*a));
        System.out.println((int)summ);
    }
}