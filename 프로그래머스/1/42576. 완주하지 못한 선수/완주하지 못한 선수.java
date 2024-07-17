import java.util.HashMap;
import java.util.HashSet;

class Solution {
    public static void main(String[] args) {
        String[] pri = {"mislav", "stanko", "mislav", "ana"};
        String[] com = {"stanko", "ana", "mislav"};

        String solution = solution(pri, com);
        System.out.println(solution);
    }

    public static String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> map = new HashMap<String, Integer>();
        for (int i = 0; i < participant.length; i++) {
            if(map.containsKey(participant[i])) {
                int cnt = map.get(participant[i]) + 1;
                map.put(participant[i], cnt);
            }else{
                map.put(participant[i], 1);
            }
        }
        for(String completionPeople : completion) {
            if(map.containsKey(completionPeople)) {
                int cnt = map.get(completionPeople) - 1;
                map.put(completionPeople, cnt);
            }
            if(map.get(completionPeople) == 0) {
                map.remove(completionPeople);
            }
        }
        // hashmap에서 남은거 어떻게 접근?
        for (String key : map.keySet()){
            answer+=key;
        }

        return answer;
    }
}