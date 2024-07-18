import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.HashSet;

class Main {
    public static void main(String[] args) throws IOException {
        Object[] objArr = new Object[3];
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int i = 0; i < 3; i++) {
            Object obj = br.readLine();
            objArr[i] = obj;
        }

        int i = 0;
        int number = 0;
        for(; i < 3; i++){
            try{
                number = Integer.parseInt(objArr[i].toString());
                break;
            }catch(NumberFormatException e){
                continue;
            }
        }
        int wantNumber = 0;
        if(i == 0) wantNumber = number+3;
        else if(i == 1) wantNumber = number+2;
        else if(i == 2) wantNumber = number+1;

        if(wantNumber % 3 == 0 && wantNumber % 5 == 0){
            System.out.println("FizzBuzz");
        }else if(wantNumber % 3 == 0 && wantNumber % 5 != 0){
            System.out.println("Fizz");
        }else if(wantNumber % 3 != 0 && wantNumber % 5 == 0){
            System.out.println("Buzz");
        }else{
            System.out.println(wantNumber);
        }
    }
}