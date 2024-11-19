import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static ArrayList<Node>[] graph;
    static boolean[] visited;
    static int max, leaf;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        // 그래프 및 방문 배열 초기화
        graph = new ArrayList[T + 1];
        visited = new boolean[T + 1];

        for (int i = 1; i <= T; i++) {
            graph[i] = new ArrayList<>();
        }

        // 부모 및 자식 노드 연결
        while (T-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int parent = Integer.parseInt(st.nextToken());
            int child;
            while ((child = Integer.parseInt(st.nextToken())) != -1) {
                int point = Integer.parseInt(st.nextToken());
                graph[parent].add(new Node(child, point));
            }
        }
        // 길이가 가장 긴 리프 노드 탐색
        dfs(1, 0);

        // 방문 배열 및 최대값 초기화
        visited = new boolean[visited.length];
        max = 0;

        // 길이가 가장 긴 리프 노드부터 탐색 시작
        dfs(leaf, 0);

        // 최대값 출력
        System.out.println(max);
    }

    private static void dfs(int cur, int point) {
        // 현재 노드 방문 처리
        visited[cur] = true;

        // 현재 노드와 이어진 노드를 탐색
        for (int i = 0; i < graph[cur].size(); i++) {
            Node node = graph[cur].get(i);
            // 방문하지 않은 노드라면 탐색 진행
            if (!visited[node.num]) {
                dfs(node.num, point + node.point);
            }
        }

        // 탐색의 끝(리프 노드)일 경우 최대값 비교
        if (max < point) {
            leaf = cur;
            max = point;
        }
    }

    static class Node {
        int num, point;

        public Node(int num, int point) {
            this.num = num;
            this.point = point;
        }

    }
}