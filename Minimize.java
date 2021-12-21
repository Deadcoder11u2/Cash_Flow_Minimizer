import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class Minimize {
    static int N = 3;
    static int counter = 0;

    static int getMin(int arr[]) {
        int minInd = 0;
        for (int i = 1; i < N; i++)
            if (arr[i] < arr[minInd])
                minInd = i;
        return minInd;
    }

    static int getMax(int arr[]) {
        int maxInd = 0;
        for (int i = 1; i < N; i++)
            if (arr[i] > arr[maxInd])
                maxInd = i;
        return maxInd;
    }

    static int minOf2(int x, int y) {
        return (x < y) ? x : y;
    }

    static void minCashFlowRec(int amount[], StringBuilder sb) {
        int mxCredit = getMax(amount), mxDebit = getMin(amount);
        if (amount[mxCredit] == 0 && amount[mxDebit] == 0)
            return;
        int min = minOf2(-amount[mxDebit], amount[mxCredit]);
        amount[mxCredit] -= min;
        amount[mxDebit] += min;
        counter++;
        sb.append(mxDebit + " " + mxCredit + " " + min + "\n");
        minCashFlowRec(amount, sb);
    }

    static StringBuilder minCashFlow(int graph[][], PrintWriter out) {
        int amount[] = new int[N];
        StringBuilder sb = new StringBuilder();
        for (int p = 0; p < N; p++)
            for (int i = 0; i < N; i++)
                amount[p] += (graph[i][p] - graph[p][i]);

        minCashFlowRec(amount, sb);
        return sb;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader("input.txt"));
        PrintWriter out = new PrintWriter("output.txt");
        StringTokenizer st = new StringTokenizer("");
        st = new StringTokenizer(br.readLine());
        int nodes = Integer.parseInt(st.nextToken());
        int graph[][] = new int[nodes][nodes];
        int edges = Integer.parseInt(st.nextToken());
        out.print(nodes + " ");
        N = nodes;
        for (int i = 0; i < edges; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());
            graph[u][v] = weight;
        }
        StringBuilder sb = minCashFlow(graph, out);
        out.println(counter);
        out.print(sb);
        br.close();
        out.close();
    }
}