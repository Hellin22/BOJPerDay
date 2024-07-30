import java.util.*;


class Solution {
    public ArrayList<Integer> solution(String s) {
        StringTokenizer st = new StringTokenizer(s, "{}");
        ArrayList<String> list = new ArrayList<>();
        while(st.hasMoreTokens()){
            list.add(st.nextToken());
        }
        ArrayList<String> list1 = new ArrayList<>();

        for(int i = 0; i < list.size(); i+=2){
            list1.add(list.get(i));
        }


        Collections.sort(list1, (o1, o2) ->{
            return o1.length() - o2.length();
        });

        ArrayList<Integer>[] list2 = new ArrayList[list1.size()];
        for(int i = 0; i < list1.size(); i++){
            list2[i] = new ArrayList<>();
        }
        for(int i = 0; i < list1.size(); i++){
            String[] strs = list1.get(i).split(",");
            for(int j = 0; j < strs.length; j++){
                list2[i].add(Integer.parseInt(strs[j]));
            }
        }

        LinkedHashSet<Integer> set = new LinkedHashSet<>();

        for(int i = 0; i < list2.length; i++){
            for(int j = 0; j < list2[i].size(); j++){
                set.add(list2[i].get(j));
            }
        }
        ArrayList<Integer> answer = new ArrayList<>();

        Iterator<Integer> iterator = set.iterator();
        while(iterator.hasNext()){
            answer.add(iterator.next());
        }
        return answer;
    }
}