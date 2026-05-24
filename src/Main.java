import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        while (true) {
            int n = scanner.nextInt();
            int m = scanner.nextInt();

            if (n == 0 && m == 0) {
                break;
            }

            List<Edge> edges = new ArrayList<>();

            for (int i = 0; i < m; i++) {
                int u = scanner.nextInt();
                int v = scanner.nextInt();
                long w = scanner.nextLong();

                edges.add(new Edge(u, v, w));
            }

            HeavyCycleEdges kruskal = new HeavyCycleEdges(n, edges);
            Queue<Long> heavyEdges = kruskal.getHeavyEdges();

            if (heavyEdges.isEmpty()) {
                System.out.println("forest");
            } else {
                boolean first = true;

                for (long weight : heavyEdges) {
                    if (!first) {
                        System.out.print(" ");
                    }

                    System.out.print(weight);
                    first = false;
                }

                System.out.println();
            }
        }

        scanner.close();
    }
}