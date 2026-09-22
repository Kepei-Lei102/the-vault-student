public class Grid {
    public static void main(String[] args) {
        int[][] g = new int[2][3];                              // 2 rows of 3: every cell 0
        g[1][2] = 7;                                            // [row][col]
        System.out.println(g.length + " rows, " + g[0].length + " columns, g[1][2] = " + g[1][2]);

        int[][] m = { {1, 2, 3}, {4, 5, 6}, {7, 8, 9} };        // an initializer list of rows
        for (int r = 0; r < m.length; r++) {                    // row-major: across each row
            for (int c = 0; c < m[r].length; c++) {
                System.out.print(m[r][c] + " ");
            }
        }
        System.out.println();
        for (int c = 0; c < m[0].length; c++) {                 // column-major: down each column
            for (int r = 0; r < m.length; r++) {
                System.out.print(m[r][c] + " ");
            }
        }
        System.out.println();

        for (int[] row : m) {                                   // enhanced: the outer variable is a whole row (an int[])
            int sum = 0;
            for (int v : row) { sum += v; }
            System.out.print(sum + " ");
        }
        System.out.println();

        int[] middle = m[1];                                    // one row is itself a 1D array, and this is a reference to it
        middle[0] = 40;
        System.out.println(m[1][0]);

        int colMax = m[0][1];                                   // max of column 1
        for (int r = 1; r < m.length; r++) {
            if (m[r][1] > colMax) { colMax = m[r][1]; }
        }
        System.out.println("column 1 max " + colMax);

        int last = m[2][m[2].length - 1];                       // rotate row 2 right by one
        for (int c = m[2].length - 1; c > 0; c--) {
            m[2][c] = m[2][c - 1];
        }
        m[2][0] = last;
        System.out.println(m[2][0] + " " + m[2][1] + " " + m[2][2]);

        System.out.println(m[3][0]);                            // there are 3 rows, 0 to 2
    }
}
