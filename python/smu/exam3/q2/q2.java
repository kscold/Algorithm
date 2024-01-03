import java.io.File;
import java.io.FileWriter;
import java.util.Scanner;
import java.io.IOException;
import java.util.Arrays;

public class q2
{
    public static int solution(int R, int[][] coords)
    {
        // your code is here
        // -----------------------------------
        // -----------------------------------
    }   

    public static void main(String[] args)
    {
        // DO NOT EDIT. Open files
        try {
            File input = new File("input.txt"); // input data
            FileWriter output = new FileWriter("output.txt"); // your answer
   
            long start_time = System.currentTimeMillis();
            Scanner datain = new Scanner(input);
            int R = datain.nextInt();
            int N = datain.nextInt();
            int coords[][] = new int[N][2];
            for(int i=0; i<N; i++) {
                int x = datain.nextInt();
                int y = datain.nextInt();
                coords[i][0] = x;
                coords[i][1] = y;
            }
            int result = solution(R, coords);
            System.out.println(result);
            output.write(result + "\n");
            datain.close();
            output.close();
            long end_time = System.currentTimeMillis();
            // DO NOT EDIT. Checking answers
            System.out.printf("Elapsed time: %.2f seconds.\n", (float)(end_time - start_time) / 1000);
            compare_output("output.txt", "expected.txt");
        } catch (IOException e) {
            System.out.println("FileWriter error");
            e.printStackTrace();
        }
    }

    public static void compare_output(String file1, String file2)
    {
        File f1 = new File(file1);
        File f2 = new File(file2);
        try {
            Scanner result = new Scanner(f1);
            Scanner expected = new Scanner(f2);

            int i = 1;
            Boolean success = true;

            while(result.hasNextLine() && expected.hasNextLine()) {
                String line1 = result.nextLine().trim();
                String line2 = expected.nextLine().trim();
                if (!line1.equals(line2)) {
                    System.out.println("[" + i + "] Wrong answer: Yours=\'" + line1 + "\', Expected=\'" + line2 + "\'");
                    success = false;
                    break;
                }
                i++;
            }
            if (!expected.hasNextLine() && success) System.out.println("Success!");
            result.close();
            expected.close();
        } catch (IOException e) {
           System.out.println("FileWriter error");
            e.printStackTrace();
        }
    }
}
