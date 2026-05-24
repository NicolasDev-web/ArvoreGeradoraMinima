public class Edge implements Comparable<Edge> {

    private final int v;
    private final int w;
    private final long weight;

    public Edge(int v, int w, long weight) {
        this.v = v;
        this.w = w;
        this.weight = weight;
    }

    public long weight() {
        return weight;
    }

    public int either() {
        return v;
    }

    public int other(int vertex) {
        if (vertex == v) {
            return w;
        } else if (vertex == w) {
            return v;
        } else {
            throw new IllegalArgumentException("Vértice inválido");
        }
    }

    @Override
    public int compareTo(Edge that) {
        return Long.compare(this.weight, that.weight);
    }
}