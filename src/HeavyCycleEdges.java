import java.util.Collections;
import java.util.List;

public class HeavyCycleEdges {

    private Queue<Long> heavyEdges;

    public HeavyCycleEdges(int vertices, List<Edge> edges) {
        heavyEdges = new Queue<>();

        Collections.sort(edges);

        UF uf = new UF(vertices);

        for (Edge edge : edges) {
            int v = edge.either();
            int w = edge.other(v);

            if (uf.connected(v, w)) {
                heavyEdges.enqueue(edge.weight());
            } else {
                uf.union(v, w);
            }
        }
    }

    public Queue<Long> getHeavyEdges() {
        return heavyEdges;
    }
}