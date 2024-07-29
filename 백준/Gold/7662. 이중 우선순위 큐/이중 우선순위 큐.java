
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.io.IOException;
import java.lang.StringBuilder;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        while (t-- > 0) {
            int n = Integer.parseInt(br.readLine());
            PriorityQueue<Integer> minpq = new PriorityQueue<>();
            PriorityQueue<Integer> maxpq = new PriorityQueue<>(Collections.reverseOrder());
            HashMap<Integer, Integer> map = new HashMap<>();
            for (int i = 0; i < n; i++) {
                String[] strs = br.readLine().split(" ");
                if (strs[0].equals("I")) {
                    int inputNum = Integer.parseInt(strs[1]);
                    maxpq.add(inputNum);
                    minpq.add(inputNum);
                    if(map.containsKey(inputNum)) {
                        map.put(inputNum, map.get(inputNum) + 1);
                    }else{
                        map.put(inputNum, 1);
                    }
                } else if (strs[0].equals("D")) {
                    int deleteNum = Integer.parseInt(strs[1]);
                    if (map.isEmpty()) {
                        continue;
                    } else if (deleteNum == 1) {
                        // 최대값 삭제
                        while (true) {
                            if (map.containsKey(maxpq.peek())) {
                                map.put(maxpq.peek(), map.get(maxpq.peek()) - 1);
                                if (map.get(maxpq.peek()) == 0) {
                                    map.remove(maxpq.peek());
                                }
                                maxpq.poll();
                                break;
                            } else {
                                if (maxpq.size() == 0) {
                                    break;
                                }
                                maxpq.poll();
                            }
                        }
                    } else {
                        // 최소값 삭제
                        while (true) {
                            if (map.containsKey(minpq.peek())) {
                                map.put(minpq.peek(), map.get(minpq.peek()) - 1);
                                if (map.get(minpq.peek()) == 0) {
                                    map.remove(minpq.peek());
                                }
                                minpq.poll();
                                break;
                            } else {
                                if (minpq.size() == 0) {
                                    break;
                                }
                                minpq.poll();
                            }
                        }
                    }

                }

            }
            if(map.isEmpty()){
                sb.append("EMPTY\n");
            }else{
                while(true){
                    if(map.containsKey(maxpq.peek())){
                        sb.append(maxpq.peek() + " ");
                        break;
                    }else {
                        maxpq.poll();
                    }
                }
                while(true){
                    if(map.containsKey(minpq.peek())) {
                        sb.append(minpq.peek() + "\n");
                        break;
                    }else{
                        minpq.poll();
                    }
                }
            }
        }
        System.out.println(sb);
    }
}